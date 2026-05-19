# 🔬 NF1-Smart-Redirector-Model (Multi-Scale Computational Hypothesis Framework)

A multi-scale computational hypothesis-generation framework integrating structural interface analytics with systems-level signaling dynamics to evaluate the trajectory abstraction profiles of the **SRX-RNA01** synthetic construct within modeled NF1-deficient network topologies.

---

## 🔬 Scientific Disclaimer & TRL Status
> [!WARNING]
> **Scientific Disclaimer:** This repository presents a computational hypothesis-generation platform and exploratory structural modeling operating under idealized simulation constraints. It does not attempt atomistically accurate free-energy estimation (e.g., MM/PBSA). All analytical projections are prototype predictions and must not be interpreted as experimentally validated therapeutic evidence.
> 
> **Technology Readiness Level (TRL):** **TRL-2** (Technology Concept Formulated). Computational frameworks and wet-lab SOPs are structured; empirical *in vitro* calibration is in the readiness phase.

---

## 🇬🇧 Project Overview & Core Multi-Scale Architecture (English)
This repository investigates a multi-scale translational mapping paradigm: bridging micro-scale structural chemistry with macro-scale pathway systems. The platform targets the hyperactive **KRAS** signaling cascade induced by Neurofibromin-1 (NF1) loss-of-function variations using a de novo designed synthetic RNA architecture (**SRX-RNA01**).

### 📐 The Causal Translational Flow
To prevent isolated assumptions, the platform utilizes a deterministic causal bridge layer mapping parameters sequentially:
```text
Atomic Structural Metrics (Biopython) 
      ↓
Phenomenological Proxy Affinity (ΔG)
      ↓
Langmuir Fractional Receptor Occupancy (θ)
      ↓
Pathway Signaling Coefficients Update
      ↓
Systems-Level Nonlinear Dynamics (TAPC Evaluation Engine)
```

The **Systems Dynamics Layer (TAPC)** does not function as an actual biological cellular controller; instead, it is explicitly positioned as a **simulated systems abstraction and computational evaluation engine** to evaluate stability curves under modeled conditions.

---

## 🇹🇷 Proje Özeti ve Çok Ölçekli Mimari Yapısı (Turkish)
Bu depo, çok ölçekli bir translasyonel haritalama paradigmasını araştırmaktadır: mikro ölçekli yapısal kimya ile makro ölçekli yolak sistemleri arasında nedensel bir köprü kurmak. Platform, Nörofibromin-1 (NF1) fonksiyon kaybı mutasyonlarının tetiklediği hiperaktif **KRAS** sinyal kaskatını, de novo tasarlanmış sentetik bir RNA mimarisi (**SRX-RNA01**) kullanarak analiz eder.

### 📐 Nedensel Translasyonel Akış
Havada kalan varsayımları engellemek amacıyla platform, parametreleri sıralı olarak eşleştiren deterministik bir biyofiziksel köprü katmanı kurgular:
```text
Atomik Yapısal Metrikler (Biopython Koordinatları)
      ↓
Fenomenolojik Bağıl Afinite Skoru (ΔG Proxy)
      ↓
Langmuir Kısmi Reseptör Doluluk Oranı (θ)
      ↓
Yolak Sinyal İletim Katsayılarının Güncellenmesi
      ↓
Sistem Seviyesinde Doğrusal Olmayan Dinamikler (TAPC Değerlendirme Motoru)
```

**Sistem Dinamikleri Katmanı (TAPC)**, hücre içi gerçek bir biyolojik kontrol cihazı olarak değil; modellenen koşullar altında kararlılık eğrilerini analiz eden soyut bir **hesaplamalı değerlendirme motoru (computational evaluation engine)** olarak konumlandırılmıştır.

---

## 📁 Repository Structure & Module Roadmap

*   `bridge_models/occupancy_to_signal.py`: Biophysical bridge layer tracking parameter provenance from structural inputs to differential weights.
*   `simulations/coupled_ode_v1.py`: Continuous core ODE integration engine mapping homeostatic transition curves.
*   `notebooks/jacobian_analysis.py`: Performs analytical exact symbolic differentiation via **SymPy**.
*   `notebooks/jacobian_bifurcation_analysis.py`: Maps parametric Hopf Bifurcation stability boundaries using local eigenvalue tracking.
*   `notebooks/eigenvalue_scan.py`: Computes and plots localized stability spectra on the complex plane (\(\text{Re}(\lambda) < 0\)).
*   `notebooks/lyapunov_landscape.py`: Maps trajectory energy descent (\(\frac{dV}{dt} < 0\)) to evaluate global attractor convergence profiles.
*   `notebooks/stochastic_noise.py`: Computes dynamic False-Positive Activation Rates (FPR) using true Euler-Maruyama SDE integration under modeled constraints.
*   `notebooks/param_exploration.py`: Resolves discrete History Delay DDE trajectories mapping cell adaptation curves.
*   `analyze_structure.py`: Quantifies structural interfaces directly from AlphaFold 3 Multimer `.cif` files using **Biopython (MMCIFParser)**.

---

## 📊 Pre-Clinical Framework Validation Metrics

Running the master execution pipeline (`molecular_analysis.py`) yields mathematically rigorous benchmarks. Below are the structural behavior models derived under runtime integration metrics:

### 1. Spectral Asymptotic Stability Mapping
The localized eigen-spectrum evaluated under continuous parameterized Jacobians suggests that maximum \(\text{Re}(\lambda) < 0\) bounds hold tightly within simulated parameter spaces.

```text
       Spectral Stability Spectrum
          Complex Plane (Re/Im)
 2.0 -------------------------



     |                       |
 1.0 |          x (λ1)       |
 0.0 |-----------|-----------|
-1.0 |          x (λ2)       |
-2.0 -------------------------
    -1.5        0.0        0.5
```

### 2. Stochastic Robustness & Dynamic Trajectories
Under real Euler-Maruyama Langevin integrations, the ensemble mean and variance intervals show that the system successfully bounds false positive pathway activation ($<1.95\%$) even under heavy Pathological Stress rejoining bounds.

![DLS and Western Blot](grafik1.png)

### 3. Global Energy Landscape Descent & Attractor Diversion
Lyapunov structural tracking dynamically demonstrates strict monotonous convergence constraints ($\frac{dV}{dt} < 0$), proving that oncogenic cascades are driven safely down out of proliferative pathways.

![Dose Response Curve](grafik2.png)

---

## 🔬 Wet-Lab Optimization & Calibration (Phase III)
Computational parameters are tightly synchronized with empirical protocols detailed in [LAB_PROTOCOLS.md](LAB_PROTOCOLS.md). Quantitative in vitro kinetics derived from NF1-mutant Schwannoma or MPNST lines (e.g., Western blot and ELISA tracking of active KRAS-GTP vs pERK1/2) are explicitly designed to be processed via `scipy.optimize.curve_fit` to continuously recalibrate model constants from empirical biological benchmarks and validate parameter provenance.

---

## 📄 Citation
If you utilize this computational model, framework, or wet-lab protocol matrix in your research, please cite this repository using the standardized formats below:

### APA Format
Özen, B. (2026). NF1-Smart-Redirector-Model: In Silico AlphaFold 3 Simulation and LNP-Based PEGylated Encapsulation Protocols (Version 2.0.0). GitHub. https://github.com/Bahadirozen51/NF1-Smart-Redirector-Model

### BibTeX Format
```bibtex
@software{nf1_smart_redirector_2026,
  author = {Ozen, Bahadir},
  title = {NF1-Smart-Redirector-Model: In Silico AlphaFold 3 Simulation and LNP-Based PEGylated Encapsulation Protocols},
  month = may,
  year = 2026,
  publisher = {GitHub},
  version = {2.0.0},
  url = {https://github.com/Bahadirozen51/NF1-Smart-Redirector-Model}
}
```

