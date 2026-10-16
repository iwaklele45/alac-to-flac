# Agent Guide for alac-to-flac

Batch ALAC (`.m4a`/`.alac`) to FLAC converter preserving audio quality, metadata, cover art, and lyrics.

## Prerequisites
- Python 3
- `ffmpeg` with FLAC support in `PATH`

## Usage
- Run default (`input-dir/` -> `output-dir/`):
  ```bash
  python3 convert.py
  ```
- Run custom file or directory:
  ```bash
  python3 convert.py /path/to/folder_or_file
  ```

## Conversion Specs
- **Audio:** Bit-perfect lossless transcoding (`-c:a flac`), preserving native sample rate and bit depth (16/24-bit).
- **Metadata:** Vorbis comments mapped automatically from MP4 tags (title, artist, album, track, date).
- **Lyrics:** MP4 `©lyr` atom maps directly to FLAC Vorbis comment `lyrics`.
- **Cover Art:** Preserved via video stream copy (`-map "0:v?" -c:v copy`).
- **Hierarchy:** Preserves input directory subfolders relative to input root inside `output-dir/`.
- **Skip:** Automatically skips files already existing in output with size > 0.
