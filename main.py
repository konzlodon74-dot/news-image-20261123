#!/usr/bin/env python3
"""make.fun news-image-20261123 — Monday 23 November 2026 front page.

The deliverable is a single picture: a newspaper front page drawn for
today's news as it stands part-way through the day. Iran is vowing to
answer the US naval blockade with every tool it has while tankers burn
in Hormuz; the Cikande factory fire in Indonesia has now killed 24;
Bangladesh says Sheikh Hasina will be arrested the moment she returns;
emailed bomb threats have disrupted some 450 German schools; Seoul's
education minister has resigned over the AI exam-cheating fiasco; and
the Democrats hold their biggest US House majority since 1992.

This program's only job is to place that picture at the output path,
and it refuses to do so quietly if the file looks wrong: signature,
dimensions, chunk integrity and the inflated pixel data are all
examined first, using nothing beyond the Python standard library.
"""

import hashlib
import os
import shutil
import struct
import sys
import zlib
from pathlib import Path

FOLDER = Path(__file__).resolve().parent
PICTURE = FOLDER / "entry.png"
CEILING = 1_048_576
CANVAS = 1024
MAGIC = b"\x89PNG\r\n\x1a\n"
CHANNELS = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}


def die(reason):
    sys.stderr.write(f"news-image-20261123: {reason}\n")
    raise SystemExit(1)


def pieces(blob):
    """Yield (kind, payload) for each chunk, validating CRCs en route."""
    cursor = len(MAGIC)
    while cursor + 8 <= len(blob):
        (span,) = struct.unpack_from(">I", blob, cursor)
        kind = blob[cursor + 4:cursor + 8]
        payload = blob[cursor + 8:cursor + 8 + span]
        if len(payload) != span:
            die(f"chunk {kind!r} is cut short")
        (crc,) = struct.unpack_from(">I", blob, cursor + 8 + span)
        if zlib.crc32(kind + payload) & 0xFFFFFFFF != crc:
            die(f"chunk {kind!r} carries a bad checksum")
        yield kind, payload
        cursor += 12 + span
        if kind == b"IEND":
            if cursor != len(blob):
                die("junk follows the closing IEND chunk")
            return
    die("the stream ends before any IEND chunk")


def summarize(found):
    """One-line census of the chunk list, for the delivery report."""
    census = {}
    for kind, _ in found:
        label = kind.decode("ascii", "replace")
        census[label] = census.get(label, 0) + 1
    return ", ".join(f"{label}x{count}" for label, count in census.items())


def inspect(blob):
    """Return (width, height, census) once the PNG has proven itself whole."""
    if not blob.startswith(MAGIC):
        die("the file does not open with the PNG signature")
    found = list(pieces(blob))
    kinds = [kind for kind, _ in found]
    if kinds[0] != b"IHDR" or kinds[-1] != b"IEND":
        die("the chunk order is not IHDR ... IEND")
    ihdr = found[0][1]
    if len(ihdr) != 13:
        die("the IHDR payload is the wrong length")
    width, height = struct.unpack(">II", ihdr[:8])
    depth, colour = ihdr[8], ihdr[9]
    if depth != 8 or colour not in CHANNELS:
        die(f"unsupported PNG encoding: depth {depth}, colour {colour}")
    squeezed = b"".join(payload for kind, payload in found if kind == b"IDAT")
    try:
        raw = zlib.decompress(squeezed)
    except zlib.error as exc:
        die(f"the image data will not inflate: {exc}")
    stride = 1 + width * CHANNELS[colour]
    if len(raw) != stride * height:
        die(f"inflated data is {len(raw)} bytes, expected {stride * height}")
    return width, height, summarize(found)


def deliver():
    if not PICTURE.exists():
        die("entry.png is absent from this repository")
    blob = PICTURE.read_bytes()
    if len(blob) > CEILING:
        die(f"entry.png is {len(blob)} bytes; the ceiling is {CEILING}")
    width, height, census = inspect(blob)
    if width != CANVAS or height != CANVAS:
        die(f"entry.png is {width}x{height}; the canvas must be 1024x1024")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.png"
    shutil.copyfile(PICTURE, out_path)
    fingerprint = hashlib.sha256(out_path.read_bytes()).hexdigest()
    print(f"delivered {out_path}: {len(blob)} bytes, chunks {census}, "
          f"sha256 {fingerprint}")


if __name__ == "__main__":
    deliver()
