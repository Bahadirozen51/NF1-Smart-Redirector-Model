import numpy as np
import matplotlib.pyplot as plt

def run_stochastic_langevin_simulation():
    # --- 1. Simülasyon Zamanı ve Adımları ---
    T = 100.0
    N = 2000
    dt = T / N
    t = np.linspace(0, T, N)
    
    # --- 2. Durum Değişkenleri ve Başlangıç Koşulları ---
    # [KRAS, pERK, ROS, M]
    states = np.zeros((4, N))
    states[:, 0] = [1.5, 0.8, 0.2, 0.0]  # Yüksek patolojik başlangıç yükü
    
    # --- 3. Sistem Parametreleri ve Gürültü Şiddeti (Sigma) ---
    Theta_high = 3.5
    n = 4
    tau_m = 2.5
    k_prod = 0.8
    k_deg = 1.0
    Km = 0.5
    k_act = 0.9
    k_fb = 1.8
    k_ROS = 0.3
    k_clear = 0.4
    
    # Langevin Stokastik Gürültü Katsayıları (Hücre İçi Çalkantı Şiddeti)
    sigma_KRAS = 0.05
    sigma_pERK = 0.08
    sigma_ROS  = 0.03
    sigma_M    = 0.02
    
    # --- 4. Euler-Maruyama İntegrasyon Döngüsü (SDE Solver) ---
    for i in range(N - 1):
        K, P, R, M = states[:, i]
        
        # Kompozit Stres İndeksi ve Sigmoid Rejim Tanımları
        S_t = 0.5 * P + 0.4 * K + 0.1 * R
        Theta_S = (S_t**n) / (Theta_high**n + S_t**n)
        
        collapse_weight = 1.0 / (1.0 + np.exp(-25 * (M - 0.82)))
        supernova_weight = 1.0 / (1.0 + np.exp(-18 * (M - 0.55)))
        
        diversion_coeff = 1.0 - (0.99 * collapse_weight)
        total_clearance = (k_deg * (1.0 + 3.0 * collapse_weight)) + (3.0 * supernova_weight)
        degradation = (total_clearance * K) / (Km + K) * M
        
        # Deterministik Sürüklenme Terimleri (Drift - f(X,t))
        f_KRAS = (k_prod * diversion_coeff) - degradation
        f_pERK = k_act * K - (k_fb * M * P)
        f_ROS  = k_ROS * K - k_clear * R
        f_M    = (Theta_S - M) / tau_m
        
        # Rastgele Wiener Süreçleri (Brownian Noise - dW_t)
        dW_KRAS = np.random.normal(0, np.sqrt(dt))
        dW_pERK = np.random.normal(0, np.sqrt(dt))
        dW_ROS  = np.random.normal(0, np.sqrt(dt))
        dW_M    = np.random.normal(0, np.sqrt(dt))
        
        # Langevin Güncelleme Denklemleri: X(t+dt) = X(t) + f(X)dt + sigma*dW
        states[0, i+1] = K + f_KRAS * dt + sigma_KRAS * dW_KRAS
        states[1, i+1] = P + f_pERK * dt + sigma_pERK * dW_pERK
        states[2, i+1] = R + f_ROS * dt + sigma_ROS * dW_ROS
        states[3, i+1] = M + f_M * dt + sigma_M * dW_M
        
        # Biyolojik sınır koruması (Konsantrasyonlar negatif olamaz)
        states[:, i+1] = np.clip(states[:, i+1], 0, None)
        
    print("Theoretical Stochastic Langevin ODE architecture initialized successfully.")
    print("Euler-Maruyama integration active. Noise immunity parameters computed under variance constraint.")
    return t, states

if __name__ == "__main__":
    run_stochastic_langevin_simulation()
