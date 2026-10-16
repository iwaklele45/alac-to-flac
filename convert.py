import os
import subprocess
import sys
from pathlib import Path

def convert_file(input_path: Path, output_path: Path) -> bool:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-i", str(input_path),
        "-map", "0:a",
        "-map", "0:v?",
        "-c:a", "flac",
        "-c:v", "copy",
        str(output_path)
    ]
    res = subprocess.run(cmd)
    return res.returncode == 0

def main():
    root = Path(__file__).resolve().parent
    target = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else root / "input-dir"
    output_base = root / "output-dir"

    if not target.exists():
        print(f"Path not found: {target}", file=sys.stderr)
        sys.exit(1)

    if target.is_file():
        files = [target]
        base_dir = target.parent
    else:
        files = [p for p in target.rglob("*") if p.is_file() and p.suffix.lower() in {".m4a", ".alac"}]
        base_dir = target

    if not files:
        print(f"No audio files found in {target}")
        return

    print(f"Found {len(files)} file(s). Converting to FLAC...")
    success = 0
    skipped = 0
    for file_path in files:
        rel = file_path.relative_to(base_dir)
        dest = (output_base / rel).with_suffix(".flac")
        if dest.exists() and dest.stat().st_size > 0:
            print(f"Skipping (already exists): {rel}")
            skipped += 1
            continue
        print(f"Converting: {rel} -> {dest.name}")
        if convert_file(file_path, dest):
            success += 1
        else:
            print(f"Failed: {rel}", file=sys.stderr)

    print(f"Completed: {success} converted, {skipped} skipped, {len(files)} total.")

if __name__ == "__main__":
    main()
