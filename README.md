# NF1-Smart-Redirector-Model
In Silico Exploration and Layer-2 Wet-Lab Calibration Protocols for Programmable RNA-Protein Control Platforms

---

## 🔬 Scientific Disclaimer & TRL Status
> [!WARNING]
> **Scientific Disclaimer:** This repository presents a computational hypothesis-generation platform and exploratory structural modeling. All docking boundaries, spatial coordinates, and analytical projections are *in silico* predictions operating under idealized computational assumptions and must not be interpreted as experimentally validated therapeutic evidence.
> 
> **Technology Readiness Level (TRL):** **TRL-2** (Technology Concept Formulated). Computational models and wet-lab protocols are structured; experimental *in vitro* validation is in the readiness phase.

---

## 🎯 Project Overview & Core Hypothesis
This repository explores a novel bio-nanotechnology paradigm: **Programmable RNA-Protein Control Platform**. Moving beyond the classical RNAi (DNA → mRNA → Protein) gene silencing paradigm, this project investigates the structural potential of a de novo designed **RNA Aptamer-like miRNA fragment** to directly intercept and allosterically modulate oncoprotein cascades at the structural level.

* **Target Cascade:** Oncogenic KRAS hyperactivation induced by upstream loss-of-function variations.
* **The Vector:** Ionizable Lipid Nanoparticles (LNPs) engineered with a 5 kDa mPEG-NHS Molecular Armor intended to improve systemic stability and potentially enhance endosomal escape.

---

## 🧬 Biological Rationale: The NF1-KRAS Axis
The fundamental therapeutic premise of the Smart-Redirector model is anchored in restoring homeostatic pathway control after the disruption of natural tumor suppression mechanics:

1. **The NF1 Brake Mechanisms:** The *NF1* gene encodes Neurofibromin, a critical Ras-GAP (GTPase-Activating Protein) that drives active KRAS-GTP down to its inactive KRAS-GDP state.
2. **Loss-of-Function Cascade:** Loss or inactivation of NF1 obliterates this GAP-mediated catalytic switch, leaving KRAS permanently locked in its active configuration, triggering uncontrolled down-stream proliferation via the MAPK (RAF-MEK-ERK) pathway.
3. **Targeted Perturbation:** The engineered *Smart-Redirector* RNA transcript is hypothesized to act as a structural surrogate capable of partially perturbing KRAS-effector recruitment dynamics, bypassing the missing Ras-GAP machinery by docking directly onto active KRAS configurations to sterically/allosterically disrupt downstream effector recruitment.

---

## 💻 Phase 1: In Silico Modeling & Structural Geometry
Initial computational investigations utilizing **AlphaFold 3** multimer configurations and a local geometric analysis pipeline indicate that the engineered *Akilli_Saptirici_miRNA* transcript exhibits spatial complementarity with the effector-binding interfaces of critical KRAS mutations (**G12C, G12D, G13D**), selected due to their high oncogenic prevalence and clinically established resistance landscapes.

* **Binding Geometry:** Structural topology snapshots suggest putative hydrogen-bond-compatible geometries in the **~2.85 Å** range at the target pockets.
* **Academic Limitation:** Static molecular docking scores are indicative of geometric fit rather than functional inhibition. Comprehensive **100–500 ns staged MD simulations** and MM-PBSA binding free energy ($\Delta G_{binding}$) calculations are ongoing to analyze conformational convergence and stability under dynamic solvent conditions.

---

## 📊 Phase 2: In Vitro Analytical Projections
The downstream biological efficacy and therapeutic selectivity of the LNP-encapsulated complex are benchmarked through standardized computational data models.

### 1. DLS Size Distribution & Target Selectivity Matrix
Theoretical formulation constraints optimize the carrier phase within an explicit $80 - 120\text{ nm}$ hydrodynamic radius to maximize intracellular uptake while suppressing aggregation metrics (target PDI $< 0.18$).
![DLS ve Western Blot Grafikleri](grafik1.png)

### 2. Dose-Response Profiles & Therapeutic Window Evaluation
Mathematical modeling using the Hill Equation projects a hypothetical $IC_{50} = 0.45\text{ nM}$ against mutant cell lines, suggesting a modeled therapeutic window relative to wild-type homeostasis under idealized computational assumptions.
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
* [ ] **Milestone 3:** 100-500 ns Production MD Run & MM-PBSA Dynamic Free Energy Analysis.
* [ ] **Milestone 4:** LNP Formulation & Dynamic Light Scattering (DLS) Calibration.
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
  author        = {Ozen, Bahadir},
  title        = {NF1-Smart-Redirector-Model: In Silico AlphaFold 3 Simulation and LNP-Based Molecular Armor Encapsulation Protocols},
  month        = may,
  year         = 2026,
  publisher    = {GitHub},
  version      = {2.0.0},
  url          = {https://github.com/Bahadirozen51/NF1-Smart-Redirector-Model},
  doi          = {Pending / Sync with Zenodo}
}
```


