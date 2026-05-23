import numpy as np
import matplotlib.pyplot as plt
import os

# 0. ALPHAFlOLD ENTEGRASYON KÖPRÜSÜ (Eklendi)
try:
    from cif_coordinate_bridge import extract_real_theta_init
    # CIF dosyasının konumunu dinamik olarak tespit et
    cif_file_path = "../alphafold_models/fold_2026_05_15_18_38_model_0.cif"
    if not os.path.exists(cif_file_path):
        cif_file_path = "alphafold_models/fold_2026_05_15_18_38_model_0.cif"
        
    print(f"[*] AlphaFold yapısal verileri okunuyor: {cif_file_path}")
    # Yapay değer yerine gerçek koordinat açısını çekiyoruz
    theta_native = extract_real_theta_init(cif_file_path, protein_chain='A', rna_chain='B')
except Exception as e:
    print(f"[!] Köprü bağlantısı kurulamadı ({e}). Hevristik değere dönülüyor.")
    theta_native = np.radians(20) # Yedek/Fallback güvenli varsayılan değer

# 1. Zaman ve Alan Parametreleri
T = 250.0        # Simülasyon süresi (ns)
dt = 0.01        # Hassas integrasyon adımı
N = int(T / dt)
t = np.linspace(0, T, N)

A_effector = 10.0

# 2. Biyofiziksel Manzara Parametreleri (Rugged Landscape)
alpha = 1.4         # Doğal geri toparlanma gücü (Artırıldı)
beta = 0.5          # Saptırıcı tork etkisi

# Fourier Pürüzlülüğü (Ruggedness) Terimleri
c1, k1 = 0.12, 10.0  
c2, k2 = 0.06, 22.0  

# 3. Gelişmiş Ornstein-Uhlenbeck Renkli Gürültü Parametreleri (Colored Noise)
tau_memory = 0.8    # Viskoz hafıza zaman sabiti (τ) -> Dijital sıçramaları engeller
sigma_noise = 1.8   # Gürültü genliği
eta = np.zeros(N)   # Renkli gürültü dizisi

# 4. Olasılıksal Bağlanma Kinetiği (Probabilistic Occupancy Gating)
np.random.seed(88)
A_redirector_dynamic = np.zeros(N)
is_bound = True
k_on = 0.04   # Yerel konsantrasyona bağlı bağlanma hızı
k_off = 0.02  # Ayrılma hızı (Residence time)

for i in range(N):
    # Olasılıksal durum geçişi (Markovian Gillespie yaklaşımı indirgemesi)
    if is_bound:
        if np.random.rand() < k_off * dt: is_bound = False
    else:
        if np.random.rand() < k_on * dt: is_bound = True
    A_redirector_dynamic[i] = 5.5 if is_bound else 0.0

# 5. Langevin Çözücü (Memory-infused Integration)
theta_rugged = np.zeros(N)
theta_rugged[0] = theta_native # İlk adımı doğrudan gerçek koordinat açısı yapar

for i in range(1, N):
    curr_theta = theta_rugged[i-1]
    curr_A_red = A_redirector_dynamic[i-1]
    
    # Ornstein-Uhlenbeck Renkli Gürültü Adımı (Hafıza Güncellemesi)
    dW = np.random.normal(0, np.sqrt(dt))
    deta = -(1.0 / tau_memory) * eta[i-1] * dt + (sigma_noise / tau_memory) * dW
    eta[i] = eta[i-1] + deta
    
    # Potansiyel Enerji Gradyanı
    base_grad = 2 * alpha * (curr_theta - theta_native) - beta * curr_A_red * np.sin(curr_theta)
    rugged_grad = c1 * k1 * np.cos(k1 * curr_theta) + c2 * k2 * np.cos(k2 * curr_theta)
    total_gradient = base_grad + rugged_grad
    
    # Sürekli Langevin Adımı (Renkli gürültü doğrudan dt ile çarpılarak sisteme viskoz akış verir)
    dtheta = -total_gradient * dt + eta[i] * dt
    theta_rugged[i] = curr_theta + dtheta

# Fiziksel sınırları koru
theta_rugged = np.clip(theta_rugged, np.radians(2), np.radians(88))

# 6. Sinyal Akışının Anlık Hesaplanması
phi_rugged = A_effector * np.cos(theta_rugged) / (1 + A_redirector_dynamic)

# 7. Görselleştirme
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(13, 11), sharex=True)

# Üst Grafik: İnhibitör Kinetiği
ax1.plot(t, A_redirector_dynamic, 'r-', alpha=0.7, label='Olasılıksal Rezidans Kinetiği ($A_{redirector}(t)$)')
ax1.set_ylabel('İnhibitör Durumu', fontsize=10)
ax1.set_title('Probabilistic Residence Kinetics & Local Concentration Fluctuations', fontsize=12, fontweight='bold')
ax1.grid(True, linestyle=':', alpha=0.5)
ax1.legend(loc='upper right')

# Orta Grafik: Renkli Gürültülü Sürekli Akış
ax2.plot(t, np.degrees(theta_rugged), 'g-', alpha=0.8, label='Sağ Model (Memory-infused Colored Noise)')
ax2.axhline(y=75, color='gray', linestyle=':', label='Hedef Saptırma Havzası (~75°)')
ax2.set_ylabel('Etkin Erişim Açısı ($\\theta_{eff}$)', fontsize=10)
ax2.set_title('Ornstein–Uhlenbeck Renkli Gürültüsü Altında Sürekli Konformasyonel Akış', fontsize=12, fontweight='bold')
ax2.grid(True, linestyle=':', alpha=0.5)
ax2.legend(loc='lower right')

# Alt Grafik: Sinyal Profilili
ax3.plot(t, phi_rugged, 'g-', alpha=0.8, label='Efektif Sinyal Akışı ($\\Phi$)')
ax3.set_xlabel('Zaman (ns)', fontsize=11)
ax3.set_ylabel('Sinyal Yoğunluğu', fontsize=10)
ax3.set_title('Nihai Profil: Probabilistic Accessibility Landscape & Ensemble Redistribution', fontsize=12, fontweight='bold')
ax3.grid(True, linestyle=':', alpha=0.5)
ax3.legend(loc='upper right')

plt.tight_layout()

# Önbellek kilidini zorlayan v2 isimlendirmesi ile otomatik kaydetme
plt.savefig('docs/ensemble_dynamics_v2.png', dpi=300, bbox_inches='tight')
plt.show()

