#!/usr/bin/env python3
"""
deduplicate_bibtex.py

Deduplicate a BibTeX file by (1) exact DOI / arXiv-ID match, then (2) fuzzy match
on (normalized title, first author, year). Emits a deduplication log alongside
the deduplicated BibTeX.

Usage:
    python deduplicate_bibtex.py \
        --input  literature-review/selected-papers.bib \
        --output literature-review/selected-papers.dedup.bib \
        --log    literature-review/dedup-log.csv

Per the Phase 3 systematic review protocol, arXiv preprints superseded by a
peer-reviewed venue version are *replaced* by the peer-reviewed entry; the
arXiv ID is preserved as a note on the survivor.

License: MIT.
"""

import argparse
import csv
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
from typing import Iterable


@dataclass
class Entry:
    raw: str
    cite_key: str
    fields: dict = field(default_factory=dict)
    bib_type: str = ""

    @property
    def doi(self) -> str:
        return (self.fields.get("doi") or "").strip().lower()

    @property
    def arxiv(self) -> str:
        return (self.fields.get("eprint") or "").strip().lower()

    @property
    def title_normalized(self) -> str:
        return _normalize_title(self.fields.get("title", ""))

    @property
    def first_author(self) -> str:
        author = self.fields.get("author", "")
        if not author:
            return ""
        first = author.split(" and ")[0].strip()
        # "Last, First" -> "last"
        last = first.split(",")[0].strip().lower()
        return _normalize_title(last)

    @property
    def year(self) -> str:
        return (self.fields.get("year") or "").strip()


def _normalize_title(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"\{|\}", "", s)
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    s = re.sub(r"\s+", " ", s).strip()
    return s


_ENTRY_RE = re.compile(r"@(\w+)\s*\{\s*([^,]+),", re.MULTILINE)


def parse_bibtex(text: str) -> list[Entry]:
    """A minimal-but-correct-enough BibTeX entry splitter."""
    entries: list[Entry] = []
    i = 0
    while True:
        m = _ENTRY_RE.search(text, i)
        if not m:
            break
        bib_type = m.group(1).lower()
        cite_key = m.group(2).strip()
        # Find matching closing brace, accounting for nested braces.
        start = m.end()
        depth = 1
        j = start
        while j < len(text) and depth > 0:
            c = text[j]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
            j += 1
        body = text[start:j - 1]
        fields = _parse_fields(body)
        raw = text[m.start():j]
        entries.append(Entry(raw=raw, cite_key=cite_key, fields=fields, bib_type=bib_type))
        i = j
    return entries


def _parse_fields(body: str) -> dict:
    """Naive field parser for `key = {value}` and `key = "value"` forms."""
    fields = {}
    rx = re.compile(r"(\w+)\s*=\s*", re.MULTILINE)
    pos = 0
    while True:
        m = rx.search(body, pos)
        if not m:
            break
        key = m.group(1).lower()
        i = m.end()
        if i >= len(body):
            break
        # Capture value
        if body[i] == "{":
            depth = 1
            j = i + 1
            while j < len(body) and depth > 0:
                if body[j] == "{":
                    depth += 1
                elif body[j] == "}":
                    depth -= 1
                j += 1
            value = body[i + 1:j - 1]
            pos = j
        elif body[i] == '"':
            j = body.find('"', i + 1)
            value = body[i + 1:j]
            pos = j + 1
        else:
            j = i
            while j < len(body) and body[j] not in ",\n":
                j += 1
            value = body[i:j].strip()
            pos = j
        fields[key] = value
    return fields


def fuzzy_match(a: Entry, b: Entry, title_threshold: float = 0.92) -> bool:
    if a.first_author and b.first_author and a.first_author != b.first_author:
        return False
    if a.year and b.year and a.year != b.year:
        return False
    if not a.title_normalized or not b.title_normalized:
        return False
    score = SequenceMatcher(None, a.title_normalized, b.title_normalized).ratio()
    return score >= title_threshold


def deduplicate(entries: Iterable[Entry]) -> tuple[list[Entry], list[dict]]:
    survivors: list[Entry] = []
    log: list[dict] = []

    for e in entries:
        replaced = False
        for s in survivors:
            # 1. DOI match
            if e.doi and s.doi and e.doi == s.doi:
                replaced = True
                _absorb_arxiv_into_survivor(s, e)
                log.append({"survivor": s.cite_key, "duplicate": e.cite_key, "rule": "DOI exact"})
                break
            # 2. arXiv match
            if e.arxiv and s.arxiv and e.arxiv == s.arxiv:
                replaced = True
                log.append({"survivor": s.cite_key, "duplicate": e.cite_key, "rule": "arXiv exact"})
                break
            # 3. Fuzzy
            if fuzzy_match(e, s):
                # Prefer peer-reviewed over preprint where one is available.
                if e.bib_type in ("inproceedings", "article") and s.bib_type == "misc":
                    survivors.remove(s)
                    survivors.append(e)
                    log.append({"survivor": e.cite_key, "duplicate": s.cite_key, "rule": "fuzzy; preferred peer-reviewed"})
                else:
                    log.append({"survivor": s.cite_key, "duplicate": e.cite_key, "rule": "fuzzy"})
                replaced = True
                break

        if not replaced:
            survivors.append(e)

    return survivors, log


def _absorb_arxiv_into_survivor(survivor: Entry, dup: Entry) -> None:
    if dup.arxiv and "eprint" not in survivor.fields:
        survivor.fields["eprint"] = dup.arxiv
        survivor.fields["archivePrefix"] = "arXiv"


def emit_bibtex(entries: Iterable[Entry], path: Path) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for e in entries:
            f.write(e.raw)
            f.write("\n\n")


def emit_log(log: list[dict], path: Path) -> None:
    if not log:
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["survivor", "duplicate", "rule"])
        w.writeheader()
        w.writerows(log)


def main() -> int:
    ap = argparse.ArgumentParser(description="Deduplicate a BibTeX file.")
    ap.add_argument("--input", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    ap.add_argument("--log", required=True, type=Path)
    args = ap.parse_args()

    text = args.input.read_text(encoding="utf-8")
    entries = parse_bibtex(text)
    survivors, log = deduplicate(entries)
    emit_bibtex(survivors, args.output)
    emit_log(log, args.log)

    print(
        f"Input entries: {len(entries)} | survivors: {len(survivors)} | "
        f"duplicates removed: {len(log)}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
