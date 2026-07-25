#!/usr/bin/env python3
"""
Optimize source photos for the web.

Usage:
    python scripts/optimize.py

Reads every image in photos/originals/ and writes to photos/web/:
  - <name>.webp       -> large  (max 1800px on the longest side, q=82)
  - <name>-sm.webp    -> small  (max  900px on the longest side, q=78)

The small variant is served to phones through srcset, saving bandwidth.
Re-running is safe: existing output files are overwritten.

The script also prints each image's aspect ratio, which is the value index.html
needs in the --ratio custom property of the matching tile.
"""

from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "photos" / "originals"
OUTPUT_DIR = ROOT / "photos" / "web"

# (filename suffix, max side in px, WebP quality)
VARIANTS = [
    ("", 1800, 82),
    ("-sm", 900, 78),
]

EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff"}


def convert(source: Path) -> None:
    image = Image.open(source)
    # Honour the EXIF orientation flag, otherwise portrait shots come out sideways
    image = ImageOps.exif_transpose(image)
    if image.mode not in ("RGB", "L"):
        image = image.convert("RGB")

    ratio = None
    for suffix, max_side, quality in VARIANTS:
        resized = image.copy()
        resized.thumbnail((max_side, max_side), Image.LANCZOS)
        target = OUTPUT_DIR / f"{source.stem}{suffix}.webp"
        resized.save(target, "WEBP", quality=quality, method=6)
        if ratio is None:
            ratio = resized.width / resized.height
        kb = target.stat().st_size / 1024
        print(f"  {target.name:<28} {resized.width}x{resized.height}  {kb:6.0f} KB")

    print(f"  --ratio:{ratio:.4f}")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    sources = sorted(
        path for path in SOURCE_DIR.iterdir()
        if path.is_file() and path.suffix.lower() in EXTENSIONS
    )

    if not sources:
        print(f"No images found in {SOURCE_DIR}")
        print("Drop the original photos there and run this again.")
        return

    for source in sources:
        mb = source.stat().st_size / 1024 / 1024
        print(f"\n{source.name}  ({mb:.1f} MB)")
        convert(source)

    before = sum(path.stat().st_size for path in sources) / 1024 / 1024
    after = sum(path.stat().st_size for path in OUTPUT_DIR.glob("*.webp")) / 1024 / 1024
    print(f"\nOriginals: {before:.1f} MB  ->  Web: {after:.1f} MB")


if __name__ == "__main__":
    main()
