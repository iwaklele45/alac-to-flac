# ALAC to FLAC Converter

Batch ALAC (`.m4a`/`.alac`) to FLAC audio converter.

- **Bit-Perfect Lossless:** Keeps original sample rate and bit depth (16-bit / 24-bit Hi-Res).
- **Metadata & Tags:** Preserves title, artist, album, track number, disc, release date, etc.
- **Embedded Lyrics:** Transfers M4A lyrics (`©lyr`) to FLAC Vorbis comment tags.
- **Embedded Cover Art:** Preserves album artwork via stream copy.
- **Folder Structure:** Mirrors directory hierarchy from input to output.
- **Smart Skip:** Automatically skips existing files in output directory.
- **Zero Dependencies:** Pure Python standard library (no pip packages needed) + `ffmpeg`.

---

## Prerequisites

Python 3 and `ffmpeg` are required.

### macOS
Using [Homebrew](https://brew.sh/):
```bash
brew install ffmpeg python3
```

### Linux (Ubuntu / Debian)
```bash
sudo apt update
sudo apt install ffmpeg python3
```

### Linux (Arch Linux)
```bash
sudo pacman -S ffmpeg python
```

### Windows
Using `winget` in PowerShell / Command Prompt:
```powershell
winget install Gyan.FFmpeg Python.Python.3
```
*Note: Restart your terminal after installing to update your `PATH`.*

---

## Usage

### 1. Default Batch Conversion
Place your `.m4a` or `.alac` files/folders inside `input-dir/`.

**macOS / Linux:**
```bash
python3 convert.py
```

**Windows:**
```cmd
python convert.py
```

Converted `.flac` files will appear in `output-dir/` with the exact same subfolder structure.

---

### 2. Convert Specific File or Folder
Pass any file or folder path as an argument:

**macOS / Linux:**
```bash
python3 convert.py "/path/to/Music/Artist"
```

**Windows:**
```cmd
python convert.py "D:\Music\Artist"
```
