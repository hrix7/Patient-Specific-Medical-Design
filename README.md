# Patient-Specific Medical Design

A privacy-safe portfolio framework describing the CT/MRI-to-model workflow used in patient-specific surgical planning and additive manufacturing.

## Workflow

1. Import and quality-check imaging data
2. Segment relevant anatomy
3. Clean and optimize the surface mesh
4. Design guides, models, or implant concepts in CAD
5. Prepare additive-manufacturing files
6. Perform geometric and documentation checks
7. Incorporate clinician feedback

## Public-repository boundary

This repository intentionally contains no patient scans, patient-derived meshes, clinical screenshots, company files, surgical plans, or proprietary CAD. Examples must be synthetic, independently created, or explicitly permission-cleared.

## Included starter utility

`src/mesh_quality.py` reports basic geometric checks for an STL/OBJ mesh. It does not determine clinical suitability.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/mesh_quality.py path/to/synthetic_mesh.stl
```

## Disclaimer

Educational portfolio only. Not a medical device and not for surgical use.

## License

MIT for original code and text.
