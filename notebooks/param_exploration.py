import numpy as np
import matplotlib.pyplot as plt

def amtp_delay_framework(states, i, dt, params, history_delay=5):
    # i: Mevcut zaman adımı, history_delay: Transkripsiyon/Translasyon hücre gecikmesi
    KRAS, pERK, ROS, M = states[:, i]
    
    # Zaman gecikmeli pERK okuması (Hücresel mekanizma anlık çalışamaz)
    if i >= history_delay:
        pERK_delayed = states[1, i - history_delay]
    else:
        pERK_delayed = states[1, 0] # Başlangıç evresi koruması
        
    Theta_high = params['Theta_high']
    n = params['n']
    tau_m = params['tau_m']
    k_prod = params['k_prod']
    k_deg = params['k_deg']
    K_m = params['K_m']
    k_act = params['k_act']
    k_fb = params['k_fb']
    k_ROS = params['k_ROS']
    k_clear = params['k_clear']
    
    # 1. Gecikmeli Kompozit Stres İndeksi (DDE Tabanlı)
    S_t = 0.5 * pERK_delayed + 0.4 * KRAS + 0.1 * ROS
    Theta_S = (S_t**n) / (Theta_high**n + S_t**n)
    
    dM_dt = (Theta_S - M) / tau_m
    
    # 2. Rejim Harmanlaması
    collapse_weight = 1.0 / (1.0 + np.exp(-25 * (M - 0.82)))
    supernova_weight = 1.0 / (1.0 + np.exp(-18 * (M - 0.55)))
    
    phenomenological_diversion_coeff = 1.0 - (0.99 * collapse_weight)
    total_clearance = (k_deg * (1.0 + 3.0 * collapse_weight)) + (3.0 * supernova_weight)
    degradation = (total_clearance * KRAS) / (K_m + KRAS) * M
    
    dKRAS_dt = (k_prod * phenomenological_diversion_coeff) - degradation
    dpERK_dt = k_act * KRAS - (k_fb * M * pERK)
    dROS_dt = k_ROS * KRAS - k_clear * ROS
    
    return [dKRAS_dt, dpERK_dt, dROS_dt, dM_dt]

def run_discrete_dde_simulation():
    T = 150.0
    N = 3000
    dt = T / N
    t = np.linspace(0, T, N)
    
    states = np.zeros((4, N))
    states[:, 0] = [1.8, 1.2, 0.3, 0.0]
    
    base_params = {
        'Theta_high': 3.5, 'n': 4, 'tau_m': 2.5, 'k_prod': 0.8, 'k_deg': 1.0,
        'K_m': 0.5, 'k_act': 0.9, 'k_fb': 1.8, 'k_ROS': 0.3, 'k_clear': 0.4
    }
    
    for i in range(N - 1):
        derivs = amtp_delay_framework(states, i, dt, base_params)
        states[:, i+1] = states[:, i] + np.array(derivs) * dt
        states[:, i+1] = np.clip(states[:, i+1], 0, None)
        
    print("Theoretical coupled DDE architecture initialized for exploratory systems-level simulations.")
    print("Instantaneous drift error fixed using discrete history delay lines.")

if __name__ == "__main__":
    run_discrete_dde_simulation()


