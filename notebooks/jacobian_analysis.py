import os
import sympy as sp

def derive_symbolic_jacobian():
    # --- Klasör Kontrolü ---
    if not os.path.exists('figures'):
        os.makedirs('figures')

    # --- 1. Sembolik Değişkenlerin Tanımlanması ---
    # Hücre içi durum değişkenleri (States)
    K, P, R, M = sp.symbols('KRAS pERK ROS M')
    
    # Sistem kinetik parametreleri
    Th, n, tau = sp.symbols('Theta_high n tau_m')
    k_prod, k_deg, Km = sp.symbols('k_prod k_deg K_m')
    k_act, k_fb, k_ROS, k_clear = sp.symbols('k_act k_fb k_ROS k_clear')
    
    # --- 2. Baskılama Rejim Geçiş Diferansiyelleri (Sigmoid Blending) ---
    # Biyolojik terminolojiyle süreklilik kazandırılmış rejim katsayıları
    suppression_high_weight = 1.0 / (1.0 + sp.exp(-25 * (M - 0.82)))
    suppression_low_weight = 1.0 / (1.0 + sp.exp(-18 * (M - 0.55)))
    
    # Sinyal Saptırma ve Koşullu Yıkım Dinamikleri
    diversion_coeff = 1.0 - (0.99 * suppression_high_weight)
    total_clearance = (k_deg * (1.0 + 3.0 * suppression_high_weight)) + (3.0 * suppression_low_weight)
    degradation = (total_clearance * K) / (Km + K) * M
    
    # Kompozit Stres Fonksiyonu Belirteçleri
    S_t = 0.5 * P + 0.4 * K + 0.1 * R
    Theta_S = (S_t**n) / (Th**n + S_t**n)
    
    # --- 3. Bağlı Diferansiyel Denklem Seti (Coupled f_i Functions) ---
    f1 = (k_prod * diversion_coeff) - degradation    # dKRAS/dt
    f2 = k_act * K - (k_fb * M * P)                    # dpERK/dt
    f3 = k_ROS * K - k_clear * R                       # dROS/dt
    f4 = (Theta_S - M) / tau                           # dM/dt
    
    equations = [f1, f2, f3, f4]
    states = [K, P, R, M]
    
    # --- 4. Sembolik Jacobian Matrisinin İnşası (J_ij = df_i / dx_j) ---
    print("=== Sembolik Jacobian Kısmi Türev Matrisi İnşa Ediliyor ===")
    Jacobian_matrix = sp.Matrix([[sp.diff(f, x) for x in states] for f in equations])
    
    # Raporlama için metin dosyasının hazırlanması
    report_path = 'figures/jacobian_symbolic_report.txt'
    with open(report_path, 'w', encoding='utf-8') as f_out:
        f_out.write("=== ANALYTICAL SYSTEM BIOLOGY REPORT: SYMBOLIC JACOBIAN MATRIX ===\n\n")
        for i in range(4):
            for j in range(4):
                output_str = f"J[{i}][{j}] (df_{i+1}/dx_{j+1}): {Jacobian_matrix[i, j]}"
                print(output_str)
                f_out.write(output_str + "\n")
                
    print(f"\n[SUCCESS] Sembolik matris başarıyla haritalandı ve '{report_path}' dosyasına kaydedildi.")
    return Jacobian_matrix

if __name__ == "__main__":
    derive_symbolic_jacobian()

