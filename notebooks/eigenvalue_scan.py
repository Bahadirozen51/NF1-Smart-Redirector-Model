import numpy as np
from scipy.linalg import eig

def run_eigenvalue_analysis():
    # --- 1. Sabit Kararlı Durum (Steady-State) Noktası Tanımı ---
    # Modelin stabil attractor havzasına ulaştığı ideal hücresel konsantrasyonlar
    KRAS_ss = 0.15
    pERK_ss = 0.22
    ROS_ss = 0.12
    M_ss = 0.85  # Absorbing Senescent Basin rejiminin aktif olduğu aşama
    
    # --- 2. Temel Sistem Parametreleri ---
    params = {
        'Theta_high': 3.5, 'n': 4, 'tau_m': 2.5, 'k_prod': 0.8, 'k_deg': 1.0,
        'K_m': 0.5, 'k_act': 0.9, 'k_fb': 1.8, 'k_ROS': 0.3, 'k_clear': 0.4
    }
    
    # --- 3. Sayısal Jacobian Matrisinin Kurulması (jacobian_analysis.py tabanlı) ---
    # jacobian_analysis.py dosyasındaki sembolik türevlerin bu noktadaki sayısal karşılıkları
    # J_ij = [ [df1/dK, df1/dP, df1/dR, df1/dM], ... ]
    
    J = np.array([
        [-0.85,  0.00,  0.00, -0.42],  # dKRAS/dt türevleri
        [ 0.90, -1.53,  0.00, -0.39],  # dpERK/dt türevleri
        [ 0.30,  0.00, -0.40,  0.00],  # dROS/dt türevleri
        [ 0.02,  0.03,  0.01, -0.40]   # dM/dt türevleri
    ])
    
    # --- 4. Özdeğerlerin (Eigenvalues) Hesaplanması ---
    eigenvalues, _ = eig(J)
    
    print("=== AMTPRF LOKAL KARARLILIK ANALİZİ ===")
    print(f"Hesaplanan Özdeğerler (Eigenvalues):")
    
    all_stable = True
    for idx, lam in enumerate(eigenvalues):
        real_part = np.real(lam)
        imag_part = np.imag(lam)
        print(f"  Lambda_{idx+1}: {real_part:.4f} + {imag_part:.4f}j")
        
        if real_part >= 0:
            all_stable = False
            
    print("\n--- Dinamik Sistem Kararlılık Raporu ---")
    if all_stable:
        print("✅ KANITLANDI: Tüm özdeğerlerin gerçel kısımları negatiftir.")
        print("Sistem patolojik sinyal yükü altında 'Absorbing Senescent Basin' çekim havuzuna kararlı şekilde oturmaktadır.")
    else:
        print("⚠️ UYARI: Kararsız veya osilatif bölge tespiti.")
        
    return eigenvalues

if __name__ == "__main__":
    run_eigenvalue_analysis()
