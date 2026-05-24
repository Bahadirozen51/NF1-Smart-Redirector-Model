# 🎛️ Dynamic Integration Protocol: Core ODE & Attractor Manifold Bridge

This document details the architectural link and state-dependent feedback loop established between the biochemical granularity of the core system (`coupled_ode_v1.py`) and the phenomenological control constraints verified within the sandbox (`attractor_manifold_sandbox.py`).

---

## 🏗️ Architectural Topology: The Hybrid Bridge

Rather than forcing a hard-coded geometric constraint directly into the precise biochemistry of the 4D state-space ($KRAS, pERK, ROS, M$), the repository utilizes an **Asymptotic Flux Modulation Interface**. This ensures that the mathematical limit cycle boundaries safely guide the cellular trajectories without causing structural decoupling or numerical instability.

[ coupled_ode_v1.py ] (Core Biochemical Engine)│▼Composite Stress Index (S_t) ───► Threshold E (Exceeded?)│                               ││ (No: Homeostasis)             │ (Yes: Pathological)▼                               ▼[ Natural Relaxation ]          [ Trigger Manifold Switch (f_s) ]│▼[ Fetch Confinement Factor ]From: attractor_manifold_sandbox.py│▼k_prod Dynamic Attenuation│▼[ Target Attractor Confinement ]

---

## 📐 Mathematical Coupling Formulation

When the integration bridge flag `use_attractor_manifold` is enabled, the system interceptor dynamically scales the structural production velocity (\(k_{prod}\)) using the dually verified non-linear confinement factor:

\[\text{If } S_t > E \implies f_s = \frac{S_t^2}{1 + S_t^2}\]

\[\text{Confinement Factor } (\mathcal{C}) = \frac{\sqrt{\max(R_{max}^2 - S_t^2, \epsilon)}}{R_{max}}\]

The modulated production flux (\(k_{prod}^*\)) feeding the \(dKRAS/dt\) differential equation is dynamically formulated as:

\[k_{prod}^* = k_{prod} \cdot \left[1.0 - f_s \cdot (1.0 - \mathcal{C})\right]\]

### 💎 Strategic Advantages of this Coupling:
*   **Zero Singularity Risk (\(\epsilon\)-Stabilization):** The integration engine enforces an analytical floor (\(\epsilon = 10^{-6}\)), protecting the square root evaluator from complex-number collapse if stochastic colored noise pushes \(S_t > R_{max}\).
*   **Minimal Functional Disturbance:** For baseline homeostatic breathing (\(S_t \ll E\)), \(f_s \to 0\), yielding \(k_{prod}^* \approx k_{prod}\). Other vital operational cellular structures remain entirely unaffected.
*   **Phenomenological Diversion:** In hyper-activated states, the production rate is smoothly bent downward along the attractor trajectory, transforming a runaway explosion into a stable, non-toxic limit cycle.

---

## 🛠️ Implementation Parameters

To switch between the standalone biochemical model and the integrated attractor manifold regime, modify the parameter matrix inside the master evaluation script:

```python
base_params = {
    # ... Core Biological Coefficients ...
    
    # --- MANIFOLD INTEGRATION COUPLING BARS ---
    'use_attractor_manifold': True,   # Enables/Disables the sandbox interface
    'E_threshold': 1.2,              # Enhanced Regime Selectivity baseline
    'R_max_confinement': 2.5         # Target Attractor Basin radius
}
```
