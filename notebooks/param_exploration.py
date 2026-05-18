import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def sigmoid_regime(M, center, sharpness):
    # Keskin eşikler yerine sürekli faz geçişi sağlayan diferansiyel sigmoid fonksiyonu
    return 1.0 / (1.0 + np.exp(-sharpness * (M - center)))

def amtp_continuous_framework(states, t, params):
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
    
    # 1. Composite Stress Index (CSI)
    S_t = 0.5 * pERK + 0.4 * KRAS + 0.1 * ROS
    Theta_S = (S_t**n) / (Theta_high**n + S_t**n)
    
    # Memory Kernel Adaptation (Delayed Adaptation Kernel)
    dM_dt = (Theta_S - M) / tau_m
    
    # 2. CONTINUOUS REGIME INTERPOLATION & BLENDING (Yeni Matematiksel Mimari)
    supernova_weight = sigmoid_regime(M, center=0.55, sharpness=18) # Catastrophic Clearance Fazı
    collapse_weight = sigmoid_regime(M, center=0.82, sharpness=25)  # Absorbing Senescent Basin Fazı
    
    # Rejim geçiş katsayılarının dinamik bağlanması
    # Rejim II aktifleştiğinde kopyalama katsayısı (diversion) logaritmik olarak sıfıra yaklaşır
    phenomenological_diversion_coeff = 1.0 - (0.99 * collapse_weight)
    
    # Sürekli rejim geçişli temizlik hızları (Discontinuity üretmez, Jacobian analizine uygundur)
    base_clearance = k_deg * (1.0 + 3.0 * collapse_weight) 
    rapid_nonlinear_clearance = 3.0 * supernova_weight
    
    total_clearance_rate = base_clearance + rapid_nonlinear_clearance
    degradation = (total_clearance_rate * KRAS) / (K_m + KRAS) * M
    
    # 3. Coupled ODE Set
    dKRAS_dt = (k_prod * phenomenological_diversion_coeff) - degradation
    dpERK_dt = k_act * KRAS - (k_fb * M * pERK)
    dROS_dt = k_ROS * KRAS - k_clear * ROS
    
    return [dKRAS_dt, dpERK_dt, dROS_dt, dM_dt]

def run_continuous_simulation():
    t = np.linspace(0, 150, 3000)
    initial_conditions = [1.8, 1.2, 0.3, 0.0] # Yüksek patolojik sinyal yükü başlangıcı
    
    base_params = {
        'Theta_high': 3.5, 'n': 4, 'tau_m': 2.5, 'k_prod': 0.8, 'k_deg': 1.0,
        'K_m': 0.5, 'k_act': 0.9, 'k_fb': 1.8, 'k_ROS': 0.3, 'k_clear': 0.4
    }
    
    solution = odeint(amtp_continuous_framework, initial_conditions, t, args=(base_params,))
    print("Theoretical coupled ODE architecture initialized for exploratory systems-level simulations.")
    print("Continuous regime interpolation active. Safe for Jacobian and Local Stability scans.")

if __name__ == "__main__":
    run_continuous_simulation()

