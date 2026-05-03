#!/usr/bin/env bash
# render-mermaid-figures.sh
#
# Renders the six Mermaid figure sources (F1, F2, F3, F4, F5, F6 and F7 sub-panel a)
# to vector PDF for IEEE Access submission.
#
# Vector PDFs do not have a "DPI" in the raster sense — they are resolution-
# independent. The output PDFs satisfy the IEEE Access "300 DPI minimum"
# requirement because they print at any DPI without quality loss.
#
# Prerequisites:
#   - Node.js 18+ and npm (you already have these)
#   - macOS or Linux with a working Chromium (mermaid-cli installs its own)
#
# Usage:
#   cd path/to/tera-agentic-rag
#   bash scripts/render-mermaid-figures.sh
#
# Output: PDF files alongside each .mmd source under figures/.
#
# License: MIT.

set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
FIG_DIR="$REPO_ROOT/figures"

cd "$FIG_DIR"

# Install mermaid-cli locally (one-time; cached after first run)
if [ ! -x "node_modules/.bin/mmdc" ]; then
  echo "Installing @mermaid-js/mermaid-cli locally..."
  npm init -y >/dev/null
  npm install --no-fund --no-audit @mermaid-js/mermaid-cli
fi

MMDC="$FIG_DIR/node_modules/.bin/mmdc"

render_one() {
  local src="$1"
  local out="${src%.mmd}.pdf"
  echo "Rendering $src -> $(basename "$out")"
  "$MMDC" \
    --input "$src" \
    --output "$out" \
    --backgroundColor "transparent" \
    --pdfFit \
    --quiet
}

# Render every .mmd in the figures directory
for src in "$FIG_DIR"/*.mmd; do
  [ -f "$src" ] || continue
  render_one "$src"
done

echo ""
echo "Done. Outputs:"
ls -la "$FIG_DIR"/*.pdf
echo ""
echo "Verify each PDF visually before submission. Captions and final"
echo "sub-panel composition for Figure 7 (b, c) and Figure 8 are produced"
echo "in draw.io and matplotlib respectively (see figures/README.md)."
