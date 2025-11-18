# Bundle Image Creator

Generate composite bundle images from a single sock photo. The script duplicates
one source image into multiple bundle sizes while keeping a clean, white
background and controlled overlap suitable for marketplace listings (e.g.
bol.com).

## Features
- Predefined bundle counts: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, and 20.
- Horizontal layout with increasing overlap (about 20% at two socks up to 80%
  near twenty socks).
- Automatic wrapping to additional rows to keep images up to 1200px wide.
- Output filenames follow `{original_filename}_{n}_paar.jpg`.
- Adjustable maximum width and bundle counts from the command line.

## Installation
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
python -m src.bundle_image_creator path/to/sock.jpg --output-dir output
```

Running the script without arguments shows the help text and an example command.

### Optional arguments
- `--counts`: Space-separated list of bundle sizes to generate. Defaults to the
  preset counts above.
- `--max-width`: Maximum canvas width (default: 1200).
- `--output-dir`: Directory for saving results (default: `./output`).

The script prints the paths of all generated files after it finishes.
