# AlphaFold 3 Model Results

## Fold Information
- **Fold ID:** 115617b8575eafe
- **Date:** 2026-05-15
- **Source:** AlphaFold Server (https://alphafoldserver.com)

## Contents
This directory contains the complete AlphaFold 3 computational modeling results for the NF1-Smart-Redirector protein complex:

### Model Files
- `fold_2026_05_15_18_38_model_*.cif` - Structural coordinates in mmCIF format for models 0-4

### Data Files
- `fold_2026_05_15_18_38_full_data_*.json` - Complete prediction data including pLDDT scores and PAE matrices
- `fold_2026_05_15_18_38_summary_confidences_*.json` - Summary confidence metrics for each model
- `fold_2026_05_15_18_38_job_request.json` - Original job request parameters

### Documentation
- `terms_of_use.md` - AlphaFold Server terms of use

## Quality Metrics
- **pLDDT Scores:** Confidence per residue (0-100)
- **PAE (Predicted Aligned Error):** Estimated error in Ångströms
- **Multiple Models:** 5 different structural predictions provided

## Usage
These files are ready for:
1. Molecular dynamics simulations (GROMACS input preparation)
2. Structural validation and quality assessment
3. Docking studies with target proteins
4. Downstream computational analysis

## Citation
If using these AlphaFold predictions, cite:
- Abramson, J., et al. (2024). Accurate structure prediction of biomolecular interactions with AlphaFold 3. Nature.
