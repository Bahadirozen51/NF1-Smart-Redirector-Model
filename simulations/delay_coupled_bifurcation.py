"""
NF1-Smart-Redirector-Model - Delay-Coupled Stochastic Attractor Model (DDE-SDE)
Author: Hls Aydemir duyma faz farkı
Year: 2026
Description: Independent simulation sandbox modeling phase lag and delay-induced 
             Hopf bifurcation boundaries without altering the core legacy ODE engines.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

def run_delay_confinement_simulation(
    T=80,
    dt=0.01,
    tau_steps=60,        # Faz gecikmesi (delay-induced lag)
    noise_sigma=0.05,
    activation_time=6.0,
    seed=2026
):
    np.random.seed(seed)
    N = int(T / dt)
    t = np.linspace(0, T, N)

    # State variables
    x = np.zeros(N)
    y = np.zeros(N)

    # Initial conditions
    x[0] = 0.2
    y[0] = 0.1

    # Parameters aligned with topological confinement bounds
    r = 1.0
    R = 1.58
    n_hill = 2.0
    K = 1.0

    for i in range(N - 1):
        current_t = t[i]

        # DELAYED STATE ACCESS (History Buffer integration)
        if i > tau_steps:
            x_tau = x[i - tau_steps]
        else:
            x_tau = x[0]

        # STOCHASTIC NOISE (Euler-Maruyama integration step)
        dWx = np.random.normal(0, np.sqrt(dt))
        dWy = np.random.normal(0, np.sqrt(dt))

        # REGIME SWITCHING MECHANICS
        if current_t < activation_time:
            # Unstable runaway oncogenic cascade simulation
            dxdt = y[i]
            dydt = 0.15 * y[i] + 0.05 * x[i]
        else:
            # Non-linear Hill activation and confinement damping
            hill = (x[i]**n_hill) / (K**n_hill + x[i]**n_hill) if x[i] > 0 else 0
            radial_term = (R**2 - x[i]**2 - y[i]**2)

            # Delay-coupled feedback implementation
            dxdt = y[i]
            dydt = -r * x_tau + radial_term * y[i] * hill

        # EULER-MARUYAMA FINITE DIFFERENCE UPDATE
        x[i+1] = x[i] + dxdt * dt + noise_sigma * dWx
        y[i+1] = y[i] + dydt * dt + noise_sigma * dWy

    return t, x, y, activation_time, R

if __name__ == "__main__":
    print("[+] Running Delay-Coupled Stochastic Attractor Simulation...")
    
    # Execute simulation with specific bifurcation constraints
    t, x, y, t_act, R_val = run_delay_confinement_simulation(
        tau_steps=60,
        noise_sigma=0.05,
        activation_time=6.0,
        seed=2026
    )

    pre = t < t_act
    post = t >= t_act

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # 1. TIME SERIES VISUALIZATION
    ax1.plot(t[pre], x[pre], color='crimson', lw=2, label='Runaway Regime')
    ax1.plot(t[post], x[post], color='royalblue', lw=1.8, label='Delay-Coupled Confinement')
    ax1.axvline(x=t_act, color='purple', linestyle='--', lw=2, label='Activation Onset')
    ax1.set_title("Delay-Coupled Stochastic Regulation")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Signal Amplitude (x)")
    ax1.grid(True, linestyle=':')
    ax1.legend()

    # 2. PHASE PORTRAIT VISUALIZATION
    ax2.plot(x[pre], y[pre], color='crimson', linestyle=':', lw=1.5, label='Runaway Trajectory')
    ax2.plot(x[post], y[post], color='royalblue', lw=1.5, alpha=0.85, label='Delayed Attractor Confinement')

    # Overlapping theoretical static boundary
    theta = np.linspace(0, 2*np.pi, 300)
    ax2.plot(R_val*np.cos(theta), R_val*np.sin(theta), 'k--', lw=2, alpha=0.6, label='Theoretical Boundary')
    ax2.set_title("Phase Portrait with Delay Coupling")
    ax2.set_xlabel("x (Signal)")
    ax2.set_ylabel("y (Flux Velocity)")
    ax2.grid(True, linestyle=':')
    ax2.legend()

    plt.tight_layout()
    
    # Automatic figure export tracking for retrospective traceability
    output_dir = "figures"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "delay_bifurcation_output.png")
    plt.savefig(output_path, dpi=120)
    print(f"[+] Simulation finished. Phase portrait successfully exported to: {output_path}")
