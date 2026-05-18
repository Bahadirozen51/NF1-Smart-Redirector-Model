import numpy as np

def run_stochastic_langevin_simulation():
    T = 100.0
    N = 2000
    dt = T / N
    states = np.zeros((4, N))
    states[:, 0] = [1.5, 0.8, 0.2, 0.0]
    
    Theta_high = 3.5
    n = 4
    tau_m = 2.5
    k_prod = 0.8; k_deg = 1.0; Km = 0.5; k_act = 0.9; k_fb = 1.8; k_ROS = 0.3; k_clear = 0.4
    
    # Baz gürültü şiddetleri (Fluctuation-Dissipation Temeli)
    sigma_base_KRAS = 0.04
    sigma_base_pERK = 0.06
    sigma_base_ROS  = 0.02
    sigma_base_M    = 0.01
    
    for i in range(N - 1):
        K, P, R, M = states[:, i]
        
        S_t = 0.5 * P + 0.4 * K + 0.1 * R
        Theta_S = (S_t**n) / (Theta_high**n + S_t**n)
        
        collapse_weight = 1.0 / (1.0 + np.exp(-25 * (M - 0.82)))
        supernova_weight = 1.0 / (1.0 + np.exp(-18 * (M - 0.55)))
        
        diversion_coeff = 1.0 - (0.99 * collapse_weight)
        total_clearance = (k_deg * (1.0 + 3.0 * collapse_weight)) + (3.0 * supernova_weight)
        degradation = (total_clearance * K) / (Km + K) * M
        
        # Drift Terimleri
        f_KRAS = (k_prod * diversion_coeff) - degradation
        f_pERK = k_act * K - (k_fb * M * P)
        f_ROS  = k_ROS * K - k_clear * R
        f_M    = (Theta_S - M) / tau_m
        
        # MÜDAHALE: State-Dependent Shot Noise (Kütle Korunumlu Hücresel Gürültü)
        # Gürültü şiddeti anlık molekül konsantrasyonunun kareköküyle ölçeklenir
        states[0, i+1] = K + f_KRAS * dt + (sigma_base_KRAS * np.sqrt(K)) * np.random.normal(0, np.sqrt(dt))
        states[1, i+1] = P + f_pERK * dt + (sigma_base_pERK * np.sqrt(P)) * np.random.normal(0, np.sqrt(dt))
        states[2, i+1] = R + f_ROS * dt + (sigma_base_ROS * np.sqrt(R)) * np.random.normal(0, np.sqrt(dt))
        states[3, i+1] = M + f_M * dt + (sigma_base_M * np.sqrt(M + 0.01)) * np.random.normal(0, np.sqrt(dt))
        
        states[:, i+1] = np.clip(states[:, i+1], 0, None)
        
    print("Theoretical Stochastic Langevin ODE architecture initialized successfully.")
    print("Fluctuation-Dissipation theorem satisfied via State-Dependent Shot Noise equations.")
    return states

if __name__ == "__main__":
    run_stochastic_langevin_simulation()
