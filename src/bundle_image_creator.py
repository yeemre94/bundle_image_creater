"""Bundle Image Creator

This script generates composite images by duplicating a single source image
(such as a sock photo) across multiple bundle sizes. Layout rules:
- Socks are placed horizontally with a configurable overlap that scales with count.
- Overlap grows from ~20% at two items up to 80% near twenty items.
- The layout wraps to additional rows as needed while keeping the width within
  a configurable maximum (default 1200px).
- Output filenames follow ``{original_filename}_{n}_paar.jpg``.

Example usage:
    python -m src.bundle_image_creator input/sock.jpg --output-dir output

The code is intentionally verbose and commented to make future adjustments easy.
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

from PIL import Image

DEFAULT_COUNTS: Sequence[int] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20)
MAX_REFERENCE_COUNT = 20  # Used to scale overlap progressively.


def parse_counts(raw_counts: Iterable[int] | None) -> List[int]:
    """Return a cleaned, sorted list of bundle counts.

    - Ensures all counts are >= 1.
    - Removes duplicates while preserving input order.
    """

    if raw_counts is None:
        return list(DEFAULT_COUNTS)

    seen = set()
    cleaned: List[int] = []
    for value in raw_counts:
        if value < 1:
            raise ValueError("Bundle counts must be >= 1")
        if value not in seen:
            cleaned.append(value)
            seen.add(value)
    return cleaned


def compute_overlap_ratio(count: int, min_overlap: float = 0.2, max_overlap: float = 0.8) -> float:
    """Compute the horizontal overlap ratio for a given bundle size.

    The overlap increases smoothly from ``min_overlap`` at a count of 2 to
    ``max_overlap`` at ``MAX_REFERENCE_COUNT``. Counts beyond the reference are
    clamped to avoid excessive overlap.
    """

    if count <= 1:
        return 0.0

    clamped = max(2, min(count, MAX_REFERENCE_COUNT))
    scale = (clamped - 2) / (MAX_REFERENCE_COUNT - 2)
    overlap = min_overlap + (max_overlap - min_overlap) * scale
    return overlap


def resize_if_needed(image: Image.Image, max_width: int) -> Image.Image:
    """Shrink the source image if it exceeds 90% of the allowed width.

    This keeps single-sock images from consuming the entire canvas when the
    input photo is very large.
    """

    target_width = int(max_width * 0.9)
    if image.width <= target_width:
        return image

    scale = target_width / image.width
    new_size = (int(image.width * scale), int(image.height * scale))
    return image.resize(new_size, Image.LANCZOS)


def distribute_across_rows(total: int, per_row_cap: int) -> List[int]:
    """Distribute ``total`` items across rows respecting a per-row capacity."""

    rows_needed = math.ceil(total / per_row_cap)
    row_counts: List[int] = []
    remaining = total
    for i in range(rows_needed):
        slots_left = rows_needed - i
        count_for_row = min(per_row_cap, remaining - (slots_left - 1))
        row_counts.append(count_for_row)
        remaining -= count_for_row
    return row_counts


def calculate_layout(
    count: int,
    sock_size: Tuple[int, int],
    max_width: int,
    overlap_ratio: float,
    row_gap: int = 12,
) -> Tuple[int, int, List[Tuple[float, float]]]:
    """Calculate canvas size and paste positions for the bundle.

    Returns a tuple of ``(canvas_width, canvas_height, positions)`` where each
    position is the (x, y) coordinate for the top-left corner of a sock.
    """

    sock_width, sock_height = sock_size
    step = sock_width * (1 - overlap_ratio)

    # Ensure a positive step to avoid division by zero.
    step = max(step, 1.0)

    max_per_row = max(1, int((max_width - sock_width) // step) + 1)
    row_counts = distribute_across_rows(count, max_per_row)

    row_widths = [sock_width + (row_count - 1) * step for row_count in row_counts]
    canvas_width = min(max_width, int(max(row_widths)))
    canvas_height = len(row_counts) * sock_height + (len(row_counts) - 1) * row_gap

    positions: List[Tuple[float, float]] = []
    current_y = 0.0
    for row_width, row_count in zip(row_widths, row_counts):
        start_x = (canvas_width - row_width) / 2  # Center each row.
        for idx in range(row_count):
            positions.append((start_x + idx * step, current_y))
        current_y += sock_height + row_gap

    return canvas_width, canvas_height, positions


def compose_bundle(
    sock_path: Path,
    output_dir: Path,
    count: int,
    max_width: int,
    background_color: Tuple[int, int, int] = (255, 255, 255),
) -> Path:
    """Create a composite bundle image for ``count`` socks and return the path."""

    original = Image.open(sock_path).convert("RGBA")
    resized = resize_if_needed(original, max_width)

    overlap_ratio = compute_overlap_ratio(count)
    canvas_width, canvas_height, positions = calculate_layout(
        count=count,
        sock_size=resized.size,
        max_width=max_width,
        overlap_ratio=overlap_ratio,
    )

    canvas = Image.new("RGB", (canvas_width, canvas_height), background_color)
    for pos in positions:
        canvas.paste(resized, (int(pos[0]), int(pos[1])), resized)

    output_dir.mkdir(parents=True, exist_ok=True)
    stem = sock_path.stem
    output_path = output_dir / f"{stem}_{count}_paar.jpg"
    canvas.save(output_path, format="JPEG", quality=95)
    return output_path


def create_bundles(
    sock_path: Path,
    output_dir: Path,
    counts: Sequence[int],
    max_width: int = 1200,
    background_color: Tuple[int, int, int] = (255, 255, 255),
) -> List[Path]:
    """Generate bundles for all requested counts and return output paths."""

    outputs: List[Path] = []
    for count in counts:
        output_path = compose_bundle(
            sock_path=sock_path,
            output_dir=output_dir,
            count=count,
            max_width=max_width,
            background_color=background_color,
        )
        outputs.append(output_path)
    return outputs


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate sock bundle images.")
    parser.add_argument("input", type=Path, help="Path to the source sock image.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("output"),
        help="Directory where bundled images will be saved (default: ./output).",
    )
    parser.add_argument(
        "--counts",
        type=int,
        nargs="+",
        help="Space-separated bundle counts (default: 1 2 3 4 5 6 7 8 9 10 15 20).",
    )
    parser.add_argument(
        "--max-width",
        type=int,
        default=1200,
        help="Maximum width of the generated images (default: 1200).",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    counts = parse_counts(args.counts)
    outputs = create_bundles(
        sock_path=args.input,
        output_dir=args.output_dir,
        counts=counts,
        max_width=args.max_width,
    )

    print("Generated:")
    for path in outputs:
        print(f"- {path}")


if __name__ == "__main__":
    main()
