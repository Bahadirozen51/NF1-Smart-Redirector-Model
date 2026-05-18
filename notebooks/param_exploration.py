import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# coupled_ode_v1 içindeki aynı fonksiyon yapısının simülasyon testi
def amtp_framework(states, t, params):
    KRAS, pERK, ROS, M = states
    
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
    
    S_t = 0.5 * pERK + 0.4 * KRAS + 0.1 * ROS
    Theta_S = (S_t**n) / (Theta_high**n + S_t**n)
    dM_dt = (Theta_S - M) / tau_m
    degradation = (k_deg * KRAS) / (K_m + KRAS) * M
    dKRAS_dt = k_prod - degradation
    dpERK_dt = k_act * KRAS - k_fb * M * pERK
    dROS_dt = k_ROS * KRAS - k_clear * ROS
    
    return [dKRAS_dt, dpERK_dt, dROS_dt, dM_dt]

def run_exploration():
    t = np.linspace(0, 100, 1000)
    initial_conditions = [1.2, 0.5, 0.1, 0.0]
    hill_scenarios = [1, 2, 4, 8]
    
    base_params = {
        'Theta_high': 3.5, 'tau_m': 2.0, 'k_prod': 0.6, 'k_deg': 1.2,
        'K_m': 0.5, 'k_act': 0.8, 'k_fb': 1.5, 'k_ROS': 0.4, 'k_clear': 0.5
    }
    
    plt.figure(figsize=(12, 8))
    for n_val in hill_scenarios:
        current_params = base_params.copy()
        current_params['n'] = n_val
        solution = odeint(lambda s, t: amtp_framework(s, t, current_params), initial_conditions, t)
        plt.plot(t, solution[:, 3], label=f'Hill Katsayisi (n) = {n_val}')
        
    plt.title('Bifurcation Analysis: Effect of Hill Coefficient on State-Transition Dynamics')
    plt.xlabel('Zaman')
    plt.ylabel('Sistem Aktivasyon Durumu / Bellek (M)')
    plt.grid(True, linestyle='--')
    plt.legend()
    plt.savefig('figures/hill_bifurcation_map.png', dpi=300)
    print("Bifurcation map simulated ready for deployment.")

if __name__ == "__main__":
    run_exploration()
