# Patient-Specific Medical Design

I worked as an Operations Engineer at Steroviz Pixels Pvt. Ltd. from December 2022 to May 2024. This repository presents a sanitized version of the workflow I used for CT/MRI-based anatomical reconstruction, pre-surgical planning, and patient-specific implant design.

## Work I completed

- Led more than 10 CT/MRI-based anatomical reconstruction cases.
- Segmented clinical image data and created three-dimensional anatomical models.
- Designed patient-specific CMF and orthopedic implants for mandible, zygoma, rib, and cranial cases.
- Cleaned, repaired, and optimized STL meshes.
- Incorporated surgeon feedback into design revisions.
- Checked geometry, fit, and manufacturability before additive manufacturing.
- Prepared models for 3D printing and documented case progress.

## Workflow represented here

1. Review the image series and confirm reconstruction quality.
2. Segment the relevant anatomy in 3D Slicer.
3. Export and clean the surface mesh.
4. Design the patient-specific model or implant in CAD.
5. Review fit, clearances, thickness, and printability.
6. Incorporate clinical feedback and prepare the approved manufacturing file.

## Repository code

- `src/mesh_quality.py` reports mesh size, watertightness, winding consistency, bounds, and volume.
- `src/dicom_series_inventory.py` inventories non-pixel DICOM series metadata for a local case folder.
- `docs/WORKFLOW.md` describes the sanitized end-to-end process.
- `docs/SAFE_SHARING_CHECKLIST.md` records the privacy and intellectual-property checks I apply before publishing examples.

## Run the tools

```bash
python -m pip install -r requirements.txt
python src/mesh_quality.py model.stl
python src/dicom_series_inventory.py /path/to/deidentified/dicom
```

## Tools

3D Slicer, DICOM, STL, SolidWorks/CAD, Meshmixer, anatomical reconstruction, additive manufacturing, geometric quality control.

## Confidentiality

No patient scans, identifiable information, company-owned implant files, surgical plans, or proprietary case material are included. Public examples must be synthetic or independently recreated.

## Author and Professional Setting

**Author:** Hritika Adhikary  
**Role:** Operations Engineer  
**Company:** Steroviz Pixels Pvt. Ltd.  
**Period:** December 2022 - May 2024

## Rights

Copyright (c) 2026 Hritika Adhikary. All rights reserved. See [LICENSE](LICENSE).
