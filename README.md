# NF1-Smart-Redirector-Model
In Silico Exploration and Phase-II Wet-Lab Calibration Protocols for Programmable RNA-Protein Control Platforms

![TRL](https://img.shields.io/badge/TRL-2-orange)
![Status](https://img.shields.io/badge/Status-Hypothesis%20Generation-blue)
![Validation](https://img.shields.io/badge/WetLab-Preparation-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🔬 Scientific Disclaimer & TRL Status
> [!WARNING]
> **Scientific Disclaimer:** This repository presents a computational hypothesis-generation platform and exploratory structural modeling. All docking boundaries, spatial coordinates, and analytical projections are *in silico* predictions operating under idealized computational assumptions and must not be interpreted as experimentally validated therapeutic evidence.
> 
> **Technology Readiness Level (TRL):** **TRL-2** (Technology Concept Formulated). Computational models and wet-lab protocols are structured; experimental *in vitro* validation is in the readiness phase.

---

## 🚀 Quick Start
To review the computational topology pipelines and execute the analytical data simulators locally, replicate the research environment using the steps below:

```bash
# Clone the scientific repository
git clone https://github.com/Bahadirozen51/NF1-Smart-Redirector-Model.git

# Enter the research workspace
cd NF1-Smart-Redirector-Model

# Install required bio-numerical python packages
pip install -r requirements.txt
```

---

## 🎯 Project Overview & Core Hypothesis
This repository explores a novel bio-nanotechnology paradigm: **Programmable RNA-Protein Control Platform**. Moving beyond the classical RNAi (DNA → mRNA → Protein) gene silencing paradigm, this project investigates the structural potential of a de novo designed **RNA Aptamer-like miRNA fragment** to directly intercept and allosterically modulate oncoprotein cascades at the structural level.

* **Target Cascade:** Oncogenic KRAS hyperactivation induced by upstream loss-of-function variations.
* **The Vector:** Ionizable Lipid Nanoparticles (LNPs) engineered with a PEGylated stabilization layer (referred to here as the Molecular Armor™ system) intended to improve systemic stability and potentially enhance endosomal escape.

---

## 🧬 Biological Rationale: The Neurofibromin Regulatory Axis
The conceptual therapeutic premise of the Smart-Redirector model is anchored in exploring whether disrupted pathway signaling may be partially rebalanced following loss of endogenous tumor suppression mechanics:

1. **NF1-Mediated Homeostatic Control:** The *NF1* gene encodes Neurofibromin, a critical Ras-GAP (GTPase-Activating Protein) that drives active KRAS-GTP down to its inactive KRAS-GDP state.
2. **Loss-of-Function Cascade:** Loss or inactivation of NF1 obliterates this GAP-mediated catalytic switch, leaving KRAS permanently locked in its active configuration, triggering uncontrolled downstream proliferation via the MAPK (RAF-MEK-ERK) pathway.
3. **Targeted Perturbation:** The engineered synthetic RNA construct (**SRX-RNA01**) is hypothesized to function as a transient structural modulator capable of perturbing KRAS-effector recruitment dynamics independent of canonical Ras-GAP restoration, docking directly onto active KRAS configurations to sterically/allosterically disrupt downstream effector recruitment.

### 🔬 Molecular Design Philosophy
The **SRX-RNA01** construct is not intended to function as a canonical endogenous miRNA operating within the RNA-induced silencing complex (RISC) pathway. Rather, it is conceptualized as an aptamer-inspired synthetic RNA architecture incorporating miRNA-like sequence logic to engineer programmable, structure-based target selectivity against protein interfaces.

---

## 💻 Phase I: In Silico Modeling & Structural Geometry
Initial computational investigations utilizing **AlphaFold 3** multimer configurations and a local geometric analysis pipeline indicate that the engineered **SRX-RNA01** transcript exhibits spatial complementarity with the effector-binding interfaces of critical KRAS mutations (**G12C, G12D, G13D**), selected due to their high oncogenic prevalence and clinically established resistance landscapes.

* **Binding Geometry:** Structural topology snapshots suggest putative hydrogen-bond-compatible geometries in the **~2.85 Å** range at the target pockets.
* **Academic Limitation:** Static molecular docking scores are indicative of geometric fit rather than functional inhibition. Comprehensive **100–500 ns staged MD simulations** and MM-PBSA binding free energy (ΔG_binding) calculations are ongoing to analyze conformational convergence and stability under physiological ionic strength and dynamic solvent environments.

---

## 📊 Phase II: In Vitro Analytical Projections
The downstream biological efficacy and therapeutic selectivity of the LNP-encapsulated complex are benchmarked through standardized computational data models.

### 1. DLS Size Distribution & Target Selectivity Matrix
Theoretical formulation constraints optimize the carrier phase within an explicit 80–120 nm hydrodynamic radius to maximize intracellular uptake while suppressing aggregation metrics (target PDI < 0.18).
![DLS ve Western Blot Grafikleri](grafik1.png)

### 2. Dose-Response Profiles & Therapeutic Window Evaluation
Mathematical modeling using the Hill Equation projects a hypothetical IC50 = 0.45 nM against mutant cell lines, suggesting a modeled therapeutic window relative to wild-type homeostasis under idealized computational assumptions.
![Dose Response Grafiği](grafik2.png)

---

## 📁 Repository Structure
```text
├── /alphafold_models       # Raw AlphaFold 3 multimer structural PDB/CIF configurations
├── /gromacs_systems        # Solvated dynamic boxes, topology (topol.top) and coordinate (.gro) tracks
├── /wetlab_protocols       # Standard Operating Procedures (SOP) for LNP synthesis & PEGylation
├── /analytical_models      # Python / Matplotlib scripts for Hill equation and DLS simulators
├── grafik1.png             # Intensity spectrum mapping for LNP diameter and p-ERK baseline plots
├── grafik2.png             # Logarithmic sigmoidal dose-response curve simulation visualization
└── README.md               # Core hypothesis, validation framework and scientific disclosure
```

---

## ⚠️ Technical Risks, Mitigations & Expected Failure Modes
### Identified Risks & Mitigations
1. **Direct RNA-Protein Engagement (High-Risk Component):** Direct target modulation via RNA aptamer configurations remains a non-standard biological paradigm. *Mitigation:* Broad-spectrum Surface Plasmon Resonance (SPR) and Bio-Layer Interferometry (BLI) binding affinity runs are scheduled to isolate kinetic cross-reactivity.
2. **Systemic Selectivity & Toxicity:** Off-target degradation of wild-type KRAS pathways poses severe cytotoxicity hazards. *Mitigation:* Tight constraint mapping of the therapeutic window and high-throughput cell viability assays (XTT/MTT) across diverse healthy backgrounds.
3. **Delivery Failures:** Endosomal entrapment or premature PEG degradation *in vivo*. *Mitigation:* Microfluidic optimization tuning Total Flow Rates (TFR > 12 mL/min) to control particle morphology.

### Expected Failure Modes
* Insufficient KRAS binding occupancy under physiological ionic strength and dynamic solvent environments.
* Loss of RNA structural integrity/folding kinetics after complex intracellular processing.
* Inadequate endosomal escape efficiency leading to lysosomal entrapment of the payload.
* Wild-type signaling perturbation exceeding predicted biological tolerability thresholds.
* Weak reproducibility and structural variance across diverse KRAS mutational subtypes.

---

## 🗺️ Strategic Product Roadmap
* [x] **Milestone 1:** Structural Multimer Docking (AlphaFold 3 / HADDOCK Structural Envelope).
* [x] **Milestone 2:** System Topology Setup & Solvation Box Assembly (GROMACS 2021 Base Matrix).
* [ ] **Milestone 3:** 100–500 ns Production MD Run & MM-PBSA Dynamic Free Energy Analysis.
* [ ] **Milestone 4:** LNP Formulation & Dynamic Light Scattering (DLS) Calibration.
* [ ] **Milestone 5:** Structural Binding Kinetics Validation (SPR/BLI Affinity Assays).
* [ ] **Milestone 6:** Intracellular Western Blot (p-ERK/p-MEK tracking) & MTT Viability Assays.

---

## 🛡️ Reproducibility & Transparency
This repository prioritizes computational reproducibility. All analytical projections, structural assumptions, and wet-lab readiness protocols are versioned and explicitly annotated to distinguish exploratory modeling from experimentally validated observations. 

*Note: DOI issuance planned through Zenodo synchronization upon completion of reproducible in silico validation benchmarks.*

---

## 📋 Intended Research Scope
This repository is intended for computational hypothesis generation, molecular modeling reproducibility, and wet-lab readiness planning. It is not intended to represent clinical efficacy claims, therapeutic recommendations, or experimentally validated biomedical interventions.

---

## 📄 Citation
If you utilize this computational model, framework, or wet-lab protocol matrix in your research, please cite this repository using the standardized formats below:

### APA Format
Özen, B. (2026). NF1-Smart-Redirector-Model: In Silico AlphaFold 3 Simulation and LNP-Based PEGylated Encapsulation Protocols (Version 2.0.0). GitHub. https://github.com/Bahadirozen51/NF1-Smart-Redirector-Model

### BibTeX Format
```bibtex
@software{nf1_smart_redirector_2026,
  author        = {Ozen, Bahadir},
  title        = {NF1-Smart-Redirector-Model: In Silico AlphaFold 3 Simulation and LNP-Based PEGylated Encapsulation Protocols},
  month        = may,
  year         = 2026,
  publisher    = {GitHub},
  version      = {2.0.0},
  url          = {https://github.com/Bahadirozen51/NF1-Smart-Redirector-Model}
}
```



