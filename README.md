# NF1-Smart-Redirector-Model
In Silico Design and Layer-2 Wet-Lab Validation Protocols for Programmable RNA-Protein Control Platforms

---

## 🔬 Scientific Disclaimer & TRL Status
> [!WARNING]
> **Scientific Disclaimer:** This repository presents a computational hypothesis-generation platform and proof-of-concept modeling. All docking distances, structural coordinates, and analytical projections are *in silico* predictions and should not be interpreted as experimentally validated therapeutic evidence.
> 
> **Technology Readiness Level (TRL):** **TRL-2** (Technology Concept Formulated). Computational models and wet-lab protocols are structured; experimental *in vitro* validation is in the readiness phase.

---

## 🎯 Project Overview & Core Hypothesis
This repository explores a novel bio-nanotechnology paradigm: **Programmable RNA-Protein Control Platform**. Moving beyond the classical RNAi (DNA → mRNA → Protein) gene silencing paradigm, this project investigates the structural potential of a de novo designed **RNA Aptamer-like miRNA fragment** to directly intercept and allosterically modulate oncoprotein cascades at the structural level.

* **Target Cascade:** Oncogenic KRAS hyperactivation (Switch I / Switch II hotspots).
* **The Vector:** Ionizable Lipid Nanopartices (LNPs) augmented with a 5 kDa mPEG-NHS Molecular Armor to ensure systemic stability and maximize endosomal escape.

---

## 💻 Phase 1: In Silico Modeling & Structural Geometry
Initial computational investigations utilizing **AlphaFold 3** multimer configurations and local geometric analysis pipeline indicate that the engineered *Akilli_Saptirici_miRNA* transcript exhibits structural compatibility with the effector-binding interfaces of KRAS mutations (G12C, G12D, G13D).

* **Binding Geometry:** Structural topology snapshots suggest a potential hydrogen-bonding envelope operating at an approximate **2.85 Å** boundary scale at the target pockets.
* **Academic Limitation:** Static molecular docking scores are indicative of spatial complementarity rather than functional inhibition. Comprehensive 500+ ns Molecular Dynamics (MD) trajectories, root-mean-square deviation (RMSD) profiles, and MM-PBSA binding free energy ($\Delta G_{binding}$) calculations are ongoing to confirm conformational stability and overcome solvent-effect limitations.

---

## 📊 Phase 2: In Vitro Analytical Projections
The downstream biological efficacy and therapeutic selectivity of the LNP-encapsulated complex are benchmarked through standardized computational data models.

### 1. DLS Size Distribution & Target Selectivity Matrix
Theoretical formulation constraints optimize the carrier phase within an explicit $80 - 120\text{ nm}$ hydrodynamic radius to maximize intracellular uptake while suppressing aggregation metrics (target PDI $< 0.18$).
![DLS and Western Blot Grafikleri](grafik1.png)

### 2. Dose-Response Profiles & Therapeutic Window Evaluation
Mathematical modeling using the Hill Equation establishes a simulated $IC_{50} = 0.45\text{ nM}$ against mutant cell lines, projecting a clear safety margin relative to wild-type homeostasis.
![Dose Response Grafiği](grafik2.png)

---

## ⚠️ Identified Technical Risks & Mitigations
1. **Direct RNA-Protein Engagement (High-Risk Component):** Direct target modulation via RNA aptamer configurations remains a non-standard biological paradigm. *Mitigation:* Broad-spectrum Surface Plasmon Resonance (SPR) and Bio-Layer Interferometry (BLI) binding affinity runs are scheduled to isolate kinetic cross-reactivity.
2. **Systemic Selectivity & Toxicity:** Off-target degradation of wild-type KRAS pathways poses severe cytotoxicity hazards. *Mitigation:* Tight constraint mapping of the therapeutic window and high-throughput cell viability assays (XTT/MTT) across diverse healthy backgrounds.
3. **Delivery Failures:** Endosomal entrapment or premature PEG degradation *in vivo*. *Mitigation:* Microfluidic optimization tuning Total Flow Rates (TFR $> 12\text{ mL/min}$) to control particle morphology.

---

## 🗺️ Strategic Product Roadmap
* [x] **Milestone 1:** Structural Multimer Docking (AlphaFold 3 / HADDOCK Structural Envelope).
* [x] **Milestone 2:** System Topology Setup & Solvation Box Assembly (GROMACS 2021 Base Matrix).
* [ ] **Milestone 3:** 500 ns Production MD Run & MM-PBSA Dynamic Free Energy Analysis.
* [ ] **Milestone 4:** LNP Synthesis and Dynamic Light Scattering (DLS) Calibration.
* [ ] **Milestone 5:** Structural Binding Kinetics Validation (SPR/BLI Affinity Assays).
* [ ] **Milestone 6:** Intracellular Western Blot (p-ERK/p-MEK tracking) & MTT Viability Assays.

---

## 📄 Citation
If you utilize this computational model, framework, or wet-lab protocol matrix in your research, please cite this repository using the standardized formats below:

### APA Format
Özen, B. (2026). NF1-Smart-Redirector-Model: In Silico AlphaFold 3 Simulation and LNP-Based Molecular Armor Encapsulation Protocols (Version 2.0.0). GitHub. https://github.com

### BibTeX Format
```bibtex
@software{nf1_smart_redirector_2026,
  author        = {Ozen, Bahadir saffat 83 84},
  title        = {NF1-Smart-Redirector-Model: In Silico AlphaFold 3 Simulation and LNP-Based Molecular Armor Encapsulation Protocols},
  month        = may,
  year         = 2026,
  publisher    = {GitHub},
  version      = {2.0.0},
  url          = {https://github.com/Bahadirozen51/NF1-Smart-Redirector-Model}
}
```


