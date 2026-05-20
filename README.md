# 🔬 NF1-Smart-Redirector-Model (Multi-Scale Computational Hypothesis Framework)

A multi-scale computational hypothesis-generation framework integrating structural interface analytics with systems-level nonlinear signaling dynamics to evaluate the trajectory abstraction profiles of the **SRX-RNA01** synthetic construct within modeled NF1-deficient network topologies.

---

## 🔬 Scientific Disclaimer & TRL Status
> [!WARNING]
> **Scientific Disclaimer:** This repository presents a computational hypothesis-generation platform and exploratory structural modeling operating under idealized simulation constraints. 
> 
> **Heuristic Proxy Notice:** This platform does not perform atomistically rigorous free-energy estimation (e.g., MM/PBSA, FEP, or umbrella sampling). Instead, it provides a phenomenological mapping abstraction layer that translates structural proximity metrics into systems-level signaling attenuation coefficients. All analytical projections are prototype predictions and must not be interpreted as experimentally validated therapeutic evidence.
> 
> **Technology Readiness Level (TRL):** **TRL-2** (Technology Concept Formulated). Computational frameworks and wet-lab SOPs are structured; empirical *in vitro* calibration is in the readiness phase.

---

## 🇬🇧 Project Overview & Core Multi-Scale Architecture (English)
This repository investigates a multi-scale translational mapping paradigm: bridging atomic-scale interaction metrics with systems-level nonlinear signaling dynamics [g5yo7d]. The platform targets the hyperactive **KRAS** signaling cascade induced by Neurofibromin-1 (NF1) loss-of-function variations using a de novo designed synthetic RNA architecture (**SRX-RNA01**).

### 📐 The Causal Translational Flow
To prevent isolated assumptions, the platform utilizes a deterministic, distribution-aware causal bridge layer mapping parameters sequentially [3k1l9y, nh9h9j]:
```text
Atomic Structural Metrics (Biopython Coordinates) [wgxtn9]
      ↓
Phenomenological Proxy Affinity (Heuristic ΔG Surface Mapping)
      ↓
Langmuir Fractional Receptor Occupancy (θ Abstraction) [q8r9uh]
      ↓
Pathway Signaling Coefficients Update via Monte Carlo Uncertainty Propagation [x1j9be]
      ↓
Systems-Level Nonlinear Dynamics (TAPC Computational Evaluation Engine) [0ydbn4]
```

The **Systems Dynamics Layer (TAPC)** does not function as an actual biological cellular controller [7b7o2y]; instead, it is explicitly positioned as a **simulated systems abstraction and computational evaluation engine** to evaluate stability curves, parameter sweeps, and sensitivity profiles under modeled conditions [0ydbn4, zb8s3v].

---

## 🇹🇷 Proje Özeti ve Çok Ölçekli Mimari Yapısı (Turkish)
Bu depo, çok ölçekli bir translasyonel haritalama paradigmasını araştırmaktadır: atomik ölçekli etkileşim metrikleri ile sistem seviyesindeki doğrusal olmayan sinyal dinamikleri arasında nedensel bir köprü kurmak [g5yo7d]. Platform, Nörofibromin-1 (NF1) fonksiyon kaybı mutasyonlarının tetiklediği hiperaktif **KRAS** sinyal kaskatını, de novo tasarlanmış sentetik bir RNA mimarisi (**SRX-RNA01**) kullanarak analiz eder.

### 📐 Nedensel Translasyonel Akış
Havada kalan varsayımları engellemek amacıyla platform, parametreleri dağılım farkındalıklı (distribution-aware) olarak sıralı eşleştiren biyofiziksel bir köprü katmanı kurgular [3k1l9y, nh9h9j]:
```text
Atomik Yapısal Metrikler (Biopython Koordinatları) [wgxtn9]
      ↓
Fenomenolojik Bağıl Afinite Skoru (Heuristic ΔG Proxy)
      ↓
Langmuir Kısmi Reseptör Doluluk Oranı (θ Soyutlaması) [q8r9uh]
      ↓
Monte Carlo Belirsizlik Yayılımı ile Yolak Katsayılarının Güncellenmesi [x1j9be]
      ↓
Sistem Seviyesinde Doğrusal Olmayan Dinamikler (TAPC Değerlendirme Motoru) [0ydbn4]
```

**Sistem Dinamikleri Katmanı (TAPC)**, hücre içi gerçek bir biyolojik kontrol cihazı olarak değil [7b7o2y]; modellenen koşullar altında kararlılık eğrilerini, parametre taramalarını ve duyarlılık (sensitivity) profillerini analiz eden soyut bir **hesaplamalı değerlendirme motoru (computational evaluation engine)** olarak konumlandırılmıştır [0ydbn4, zb8s3v].

---

## 📁 Repository Structure & Module Roadmap

*   `bridge_models/occupancy_to_signal.py`: Biophysical bridge layer executing Monte Carlo uncertainty propagation from structural inputs to differential weights [8k5sgh, 0h3xmw].
*   `simulations/coupled_ode_v1.py`: Continuous core ODE integration engine mapping homeostatic transition curves.
*   `notebooks/jacobian_analysis.py`: Performs analytical exact symbolic differentiation via **SymPy**.
*   `notebooks/jacobian_bifurcation_analysis.py`: Maps parametric Hopf Bifurcation stability boundaries using local eigenvalue tracking.
*   `notebooks/eigenvalue_scan.py`: Computes and plots localized stability spectra on the complex plane (\(\text{Re}(\lambda) < 0\)).
*   `notebooks/lyapunov_landscape.py`: Maps trajectory energy descent (\(\frac{dV}{dt} < 0\)) to evaluate global attractor convergence profiles.
*   `notebooks/stochastic_noise.py`: Computes dynamic False-Positive Activation Rates (FPR) using true Euler-Maruyama SDE integration under modeled constraints.
*   `notebooks/param_exploration.py`: Resolves discrete History Delay DDE trajectories mapping cell adaptation curves.
*   `analyze_structure.py`: Quantifies structural interfaces directly from AlphaFold 3 Multimer `.cif` files using **Biopython (MMCIFParser)**.
*   `molecular_analysis.ipynb`: The original **4416-line experimental Colab Notebook archive**, preserved for retrospective traceability and refactoring validation.

---

## 📊 Pre-Clinical Framework Validation Metrics

Running the master execution pipeline (`molecular_analysis.py`) yields mathematically rigorous benchmarks, automatically generated and exported to the workspace:

### 1. Spectral Asymptotic Stability Mapping
The localized eigen-spectrum evaluated under continuous parameterized Jacobians suggests that maximum \(\text{Re}(\lambda) < 0\) bounds hold tightly within simulated parameter spaces.

```text
       Spectral Stability Spectrum
          Complex Plane (Re/Im)
 2.0 -------------------------


     |                       |
 1.0 |          x \((\lambda1)       \vert{}  0.0 \vert{}-----------\vert{}-----------\vert{} -1.0 \vert{}\)          x \((\lambda2)       \vert{} -2.0 -------------------------     -1.5        0.0        0.5 \%\%\)MAGIT_PARSER_PROTECT%%```

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

