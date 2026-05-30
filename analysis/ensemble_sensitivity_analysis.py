import numpy as np
import pandas as pd

def simulate_dde_langevin(tau_steps, sigma, steps=2000, dt=0.01, seed=42):
    """
    Deterministik tam sayı gecikme adımı ve bağımsız seed ile çalışan SDE/DDE motoru.
    """
    np.random.seed(seed)
    x = np.zeros(steps)
    x_0 = 2.5  # Başlangıç: Kanser Havzası
    
    # Geçmiş bellek interpolasyonsuz saf tam sayı olarak atanır
    x[:tau_steps + 1] = x_0
    
    for t in range(tau_steps, steps - 1):
        x_delayed = x[t - tau_steps]
        
        # Çift kararlı potansiyel (Bistable Drift)
        drift = -(x[t]**3 - 2*x[t] - 0.3 * x_delayed) * dt
        # Stokastik Difüzyon
        diffusion = sigma * np.random.normal(0, np.sqrt(dt))
        
        x[t+1] = x[t] + drift + diffusion
        
        # Sayısal patlama koruması (Divergence check)
        if np.isnan(x[t+1]) or np.isinf(x[t+1]) or np.abs(x[t+1]) > 20.0:
            x[t+1:] = 999.0
            break
            
    return x

def calculate_confinement_score(trajectory):
    """Yörüngenin son %40'lık kararlı evresindeki hapsetme başarısı."""
    if np.max(trajectory) > 50.0: # Patlayan yörüngeler doğrudan başarısız kabul edilir
        return 0.0
    steps = len(trajectory)
    steady_state = trajectory[int(steps * 0.6):]
    # Hedef uyuşukluk havzası aralığı: [-1.5, -0.5]
    within_bounds = np.sum((steady_state >= -1.5) & (steady_state <= -0.5))
    return within_bounds / len(steady_state)

# Hakem Normlarına Uygun Tarama Uzayı
tau_integers = np.arange(2, 16, 1)        # Sahte çözünürlüğü engelleyen saf tam sayılar (2 ile 15 arası)
sigma_space = np.linspace(0.02, 0.70, 25) # Hassas volatilite adımları
seeds = np.arange(100, 120, 1)            # 20 Farklı Bağımsız Ensemble Tohumu (Multi-seed)

ensemble_results = []

print(f"{len(tau_integers) * len(sigma_space) * len(seeds)} toplam simülasyon koşturuluyor...")

for tau in tau_integers:
    for sigma in sigma_space:
        seed_confinements = []
        
        for seed in seeds:
            traj = simulate_dde_langevin(tau_steps=tau, sigma=sigma, seed=seed)
            score = calculate_confinement_score(traj)
            seed_confinements.append(score)
            
        # Ensemble istatistiklerini hesapla
        mean_conf = np.mean(seed_confinements)
        std_conf = np.std(seed_confinements)
        
        ensemble_results.append({
            "Tau": tau,
            "Sigma": sigma,
            "Confinement_Mean": mean_conf,
            "Confinement_Std": std_conf
        })

# Sonuçları matris verisi olarak diske yaz
df_ensemble = pd.DataFrame(ensemble_results)
df_ensemble.to_csv("ensemble_robustness_matrix.csv", index=False)
print("Ensemble analizi tamamlandı. Veri 'ensemble_robustness_matrix.csv' olarak kaydedildi.")
