"""Inventory de-identified DICOM series without reading or exporting pixel data."""
from __future__ import annotations
import argparse
import json
from collections import Counter
from pathlib import Path
import pydicom

TAGS = ["Modality", "StudyDescription", "SeriesDescription", "Rows", "Columns"]

def inventory(root: str) -> dict:
    folder = Path(root)
    if not folder.is_dir():
        raise NotADirectoryError(folder)
    series = Counter()
    details = {}
    skipped = 0
    for path in folder.rglob("*"):
        if not path.is_file():
            continue
        try:
            dataset = pydicom.dcmread(path, stop_before_pixels=True,
                                      specific_tags=["SeriesInstanceUID", *TAGS])
        except Exception:
            skipped += 1
            continue
        uid = str(dataset.get("SeriesInstanceUID", "UNKNOWN"))
        series[uid] += 1
        details.setdefault(uid, {tag: str(dataset.get(tag, "")) for tag in TAGS})
    return {"series": [{"uid": uid, "files": count, **details[uid]}
                       for uid, count in sorted(series.items())],
            "skipped_files": skipped}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("folder")
    args = parser.parse_args()
    print(json.dumps(inventory(args.folder), indent=2))
