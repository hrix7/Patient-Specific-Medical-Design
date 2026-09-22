"""Report basic mesh properties for permission-cleared or synthetic geometry."""
from __future__ import annotations
import argparse
import json
import trimesh

def inspect_mesh(path: str) -> dict:
    mesh = trimesh.load_mesh(path, process=False)
    if not isinstance(mesh, trimesh.Trimesh):
        raise ValueError("Expected a single triangular mesh")
    return {
        "vertices": int(len(mesh.vertices)),
        "faces": int(len(mesh.faces)),
        "watertight": bool(mesh.is_watertight),
        "winding_consistent": bool(mesh.is_winding_consistent),
        "volume_units_cubed": float(mesh.volume) if mesh.is_volume else None,
        "bounds": mesh.bounds.tolist(),
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mesh")
    args = parser.parse_args()
    print(json.dumps(inspect_mesh(args.mesh), indent=2))
