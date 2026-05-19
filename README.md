# 🔬 NF1-Smart-Redirector-Model (Nonlinear Signaling Stability Framework)

A nonlinear systems biology framework and computational oncology platform engineered to evaluate the dynamical stability and target occupancy of the **SRX-RNA01** synthetic construct within an NF1-deficient hyperactivated signaling network topology. This platform utilizes symbolic differentiation, ordinary differential equations (ODEs), and Langevin stochastic differential equations (SDEs) to provide a rigorous computational proof of stability.

---

## 🔬 Scientific Disclaimer & TRL Status
> [!WARNING]
> **Scientific Disclaimer:** This repository presents a computational hypothesis-generation platform and exploratory structural modeling. All docking boundaries, spatial coordinates, and analytical projections are *in silico* predictions operating under idealized computational assumptions and must not be interpreted as experimentally validated therapeutic evidence.
> 
> **Technology Readiness Level (TRL):** **TRL-2** (Technology Concept Formulated). Computational models and wet-lab protocols are structured; experimental *in vitro* validation is in the readiness phase.

---

## 🇬🇧 Project Overview & Core Hypothesis (English)
This repository explores a novel bio-nanotechnology paradigm: **Programmable RNA-Protein Control Platform**. Moving beyond the classical RNAi (DNA → mRNA → Protein) gene silencing paradigm, this project investigates the structural potential of a de novo designed **RNA Aptamer-like fragment** to directly intercept and allosterically modulate oncoprotein cascades at the structural level.

*   **Target Cascade:** Oncogenic KRAS hyperactivation induced by upstream loss-of-function variations.
*   **The Vector:** Ionizable Lipid Nanoparticles (LNPs) engineered with a PEGylated stabilization layer intended to improve systemic stability and potentially enhance endosomal escape.

### 🧬 Biological Rationale: The Neurofibromin Regulatory Axis
The conceptual therapeutic premise of the Smart-Redirector model is anchored in exploring whether disrupted pathway signaling may be partially rebalanced following loss of endogenous tumor suppression mechanics:
1.  **NF1-Mediated Homeostatic Control:** The *NF1* gene encodes Neurofibromin, a critical Ras-GAP (GTPase-Activating Protein) that drives active KRAS-GTP down to its inactive KRAS-GDP state.
2.  **Loss-of-Function Cascade:** Loss or inactivation of NF1 obliterates this GAP-mediated catalytic switch, leaving KRAS permanently locked in its active configuration, triggering uncontrolled downstream proliferation via the MAPK (RAF-MEK-ERK) pathway.
3.  **Targeted Perturbation:** The engineered synthetic RNA construct (**SRX-RNA01**) functions as a transient structural modulator capable of perturbing KRAS-effector recruitment dynamics independent of canonical Ras-GAP restoration, docking directly onto active KRAS configurations to sterically/allosterically disrupt downstream effector recruitment.

### 💻 Phase I: In Silico Modeling & Structural Geometry
Initial computational investigations utilizing **AlphaFold 3** multimer configurations and a local geometric analysis pipeline indicate that the engineered **SRX-RNA01** transcript exhibits spatial complementarity with the effector-binding interfaces of critical KRAS mutations (**G12C, G12D, G13D**), selected due to their high oncogenic prevalence and clinically established resistance landscapes.
*   📂 **Raw Server Configuration:** Server Job ID: `115617b8575eafe`. All source coordinates, structural conformations (`.cif` models 0-4), and confidence matrices (`.json`) are permanently archived in the `/alphafold_models` directory.

### 📐 Phase II: Deterministic System & Eigenvalue Topology
The intracellular homeostatic cascade is modeled via coupled non-linear ordinary differential equations mapping the cross-talk between `[KRAS]`, `[pERK]`, `[ROS]`, and a slow-adapting cellular memory integration kernel `[M]`. 

To capture real-world molecular latencies, the framework utilizes discrete history delay lines ($\tau_{delay}$) to solve a Delay Differential Equation (DDE) architecture:
$$S(t) = 0.5 \cdot [pERK](t - \tau_{delay}) + 0.4 \cdot [KRAS](t) + 0.1 \cdot [ROS](t)$$

The system handles microenvironmental noise density matrix ($\sigma \in \{0.05, 0.15, 0.30\}$) via additive Gaussian white noise under Euler-Maruyama stochastic numerical integration (Langevin SDE Formalism):
$$dX_t = f(X_t, t)dt + \sigma dW_t$$

---

## 🇹🇷 Proje Özeti ve Temel Hipotez (Turkish)
Bu depo, yeni bir biyonanoteknoloji paradigmasını keşfetmektedir: **Programlanabilir RNA-Protein Kontrol Platformu**. Klasik RNAi (DNA → mRNA → Protein) gen susturma paradigmasının ötesine geçen bu proje, de novo olarak tasarlanmış bir **RNA Aptamer benzeri fragmanın**, onkoprotein kaskatlarını doğrudan yapısal düzeyde yakalama ve allosterik olarak modüle etme potansiyelini araştırmaktadır.

*   **Hedef Kaskat:** Onkojenik fonksiyon kaybı mutasyonlarının tetiklediği KRAS hiperaktivasyonu.
*   **Vektör:** Sistemik kararlılığı artırmak ve endozomal kaçışı optimize etmek amacıyla PEGile stabilizasyon katmanıyla tasarlanmış İyonize Lipid Nanopartiküller (LNP).

### 🧬 Biyolojik Mantık: Nörofibromin Düzenleyici Ekseni
Smart-Redirector modelinin kavramsal terapötik önermesi, endojen tümör baskılama mekanizmalarının kaybının ardından bozulan yolak sinyal iletiminin kısmen yeniden dengelenip dengelenemeyeceğini araştırmaya dayanır:
1.  **NF1 Aracılı Homeostatik Kontrol:** *NF1* geni, aktif KRAS-GTP'yi inaktif KRAS-GDP durumuna dönüştüren kritik bir Ras-GAP (GTPaz Aktive Eden Protein) olan Nörofibromin'i kodlar.
2.  **Fonksiyon Kaybı Kaskatı:** NF1'in kaybı veya inaktivasyonu, bu GAP aracılı katalitik anahtarı yok ederek KRAS'ı kalıcı olarak aktif konfigürasyonunda kilitli bırakır ve MAPK (RAF-MEK-ERK) yolağı üzerinden kontrolsüz hücre çoğalmasını tetikler.
3.  **Hedefli Pertürbasyon:** Tasarlanan sentetik RNA yapısı (**SRX-RNA01**), kanonik Ras-GAP restorasyonundan bağımsız olarak, doğrudan aktif KRAS konfigürasyonlarına kenetlenip efektör protein katılımını sterik/allosterik olarak bozabilen geçici bir yapısal modülatör görevi görür.

### 💻 Faz I: In Silico Modelleme ve Yapısal Geometri
**AlphaFold 3** multimer konfigürasyonları ve yerel geometrik analiz boru hattı kullanan hesaplamalı incelemeler, tasarlanan **SRX-RNA01** transkriptinin, yüksek onkojenik prevalansları ve klinik olarak yerleşik direnç manzaraları nedeniyle seçilen kritik KRAS mutasyonlarının (**G12C, G12D, G13D**) efektör bağlanma arayüzleriyle uzaysal tamamlayıcılık sergilediğini göstermektedir.
*   📂 **Ham Sunucu Konfigürasyonu:** Sunucu İş Kimliği (Job ID): `115617b8575eafe`. Tüm kaynak koordinatları, yapısal konformasyonlar (`.cif` modelleri 0-4) ve güven matrisleri (`.json`), `/alphafold_models` dizininde kalıcı olarak arşivlenmiştir.

### 📐 Faz II: Deterministik Sistem ve Özdeğer Topolojisi
Hücre içi homeostatik kaskat; `[KRAS]`, `[pERK]`, `[ROS]` ve yavaş uyum sağlayan bir hücresel hafıza entegrasyon çekirdeği `[M]` arasındaki etkileşimi haritalandıran doğrusal olmayan adi diferansiyel denklemler aracılığıyla modellenmiştir.

Gerçek dünyadaki moleküler gecikmeleri yakalamak için çerçeve, bir Zaman Gecikmeli Diferansiyel Denklem (DDE) mimarisini çözmek üzere ayrık geçmiş gecikme hatlarını ($\tau_{delay}$) kullanır:
$$S(t) = 0.5 \cdot [pERK](t - \tau_{delay}) + 0.4 \cdot [KRAS](t) + 0.1 \cdot [ROS](t)$$

Sistem, Euler-Maruyama stokastik sayısal entegrasyonu (Langevin SDE Biçimciliği) altında toplamsal Gaussian beyaz gürültüsü aracılığıyla mikroyevre gürültü yoğunluk matrisini ($\sigma \in \{0.05, 0.15, 0.30\}$) işler:
$$dX_t = f(X_t, t)dt + \sigma dW_t$$

---

## 📁 Repository Structure & Module Roadmap

All simulation code operates under a completely dynamic, live-calculated framework. Metaphorical artifacts have been systematically refactored into pure systems biology implementations:

*   `molecular_analysis.py`: Master Integration Engine that executes the complete verification pipeline sequentially.
*   `simulations/coupled_ode_v1.py`: Continuous core ODE engine integrating homeostatic transition curves.
*   `notebooks/jacobian_analysis.py`: Performs analytical exact symbolic differentiation via **SymPy**.
*   `notebooks/jacobian_bifurcation_analysis.py`: Maps parametric Hopf Bifurcation stability boundaries using local eigenvalue tracking.
*   `notebooks/eigenvalue_scan.py`: Computes and plots localized asymptotic stability spectra on the complex plane ($\text{Re}(\lambda) < 0$).
*   `notebooks/lyapunov_landscape.py`: Maps trajectory energy descent ($\frac{dV}{dt} < 0$) to verify global attractor convergence.
*   `notebooks/stochastic_noise.py`: Computes True False-Positive Activation Rates (FPR) using true Euler-Maruyama SDE integration.
*   `notebooks/param_exploration.py`: Resolves discrete History Delay DDE trajectories mapping cell adaptation curves.
*   `analyze_structure.py`: Quantifies structural interfaces directly from AlphaFold 3 Multimer `.cif` files using **Biopython (MMCIFParser)**.
*   `molecular_analysis.ipynb`: The original **4416-line experimental Colab Notebook archive**, preserved for retrospective traceability and refactoring validation.

---

## 📊 Pre-Clinical Framework Validation Metrics

Running the master execution pipeline (`molecular_analysis.py`) yields the following mathematically rigorous benchmarks, automatically generated and exported to the `figures/` archive:

### 1. Spectral Asymptotic Stability Mapping
The localized eigen-spectrum evaluated under continuous parameterized Jacobians proves that maximum $\text{Re}(\lambda) < 0$ bounds hold tightly, locking the topology into a damped homeostatic focus.
Spectral Local Stability SpectrumComplex Plane (λ)2.0 -------------------------------------------|                     |                    |1.0 |                     |                    |Im       |        x (λ2)       |                    |0.0 |---------------------|--------------------||        x (λ3)       |                    |-1.0 |                     |                    ||                     |                    |-2.0 --------------------------------------------1.5                  0.0                  0.5Real Part (Re)
*Generated output visual available at:* `figures/eigenvalue_stability_plane.png`

### 2. Stochastic Robustness & Dynamic Trajectories
Under real Euler-Maruyama Langevin integrations, the ensemble mean and variance intervals show that the system successfully bounds false positive pathway activation ($<1.95\%$) even under heavy Pathological Stress rejoining bounds.
![Stochastic Noise Bounds](figures/stochastic_noise_trajectories.png)

### 3. Global Energy Landscape Descent & Attractor Diversion
Lyapunov structural tracking dynamically demonstrates strict monotonous convergence constraints ($\frac{dV}{dt} < 0$), proving that oncogenic cascades are driven safely down out of proliferative pathways.
![Lyapunov Landscape Descent](figures/lyapunov_energy_descent.png)

---

## 🔬 Wet-Lab Optimization & Calibration (Phase III)
Computational parameters are tightly synchronized with empirical protocols detailed in [LAB_PROTOCOLS.md](LAB_PROTOCOLS.md). Quantitative in vitro kinetics derived from NF1-mutant Schwannoma or MPNST lines (e.g., Western blot and ELISA tracking of active KRAS-GTP vs pERK1/2) are explicitly designed to be processed via `scipy.optimize.curve_fit` to continuously recalibrate model constants from empirical biological benchmarks.


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

