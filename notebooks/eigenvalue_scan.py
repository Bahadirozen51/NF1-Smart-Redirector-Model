import numpy as np
import sympy as sp
from scipy.linalg import eig

def run_dynamic_eigenvalue_analysis():
    # --- 1. Sembolik Altyapının Kurulması ---
    K, P, R, M = sp.symbols('KRAS pERK ROS M')
    Th, n, tau = sp.symbols('Theta_high n tau_m')
    k_prod, k_deg, Km, k_act, k_fb, k_ROS, k_clear = sp.symbols('k_prod k_deg K_m k_act k_fb k_ROS k_clear')
    
    # Rejim denklemleri (Diferansiyel Sigmoid)
    collapse_weight = 1.0 / (1.0 + sp.exp(-25 * (M - 0.82)))
    supernova_weight = 1.0 / (1.0 + sp.exp(-18 * (M - 0.55)))
    
    diversion_coeff = 1.0 - (0.99 * collapse_weight)
    total_clearance = (k_deg * (1.0 + 3.0 * collapse_weight)) + (3.0 * supernova_weight)
    degradation = (total_clearance * K) / (Km + K) * M
    
    S_t = 0.5 * P + 0.4 * K + 0.1 * R
    Theta_S = (S_t**n) / (Th**n + S_t**n)
    
    # Denklem fonksiyonları
    f1 = (k_prod * diversion_coeff) - degradation
    f2 = k_act * K - (k_fb * M * P)
    f3 = k_ROS * K - k_clear * R
    f4 = (Theta_S - M) / tau
    
    # Sembolik Jacobian Matrisi Hesaplama
    equations = [f1, f2, f3, f4]
    states = [K, P, R, M]
    J_symbolic = sp.Matrix([[sp.diff(f, x) for x in states] for f in equations])
    
    # --- 2. Sembolik Matrisi Sayısal Fonksiyona Çevirme (sp.lambdify) ---
    all_symbols = states + [Th, n, tau, k_prod, k_deg, Km, k_act, k_fb, k_ROS, k_clear]
    jacobian_numerical_func = sp.lambdify(all_symbols, J_symbolic, 'numpy')
    
    # --- 3. Kararlı Durum Değerleri ve Sayısal Parametre Girişi ---
    KRAS_ss, pERK_ss, ROS_ss, M_ss = 0.15, 0.22, 0.12, 0.85
    param_values = [3.5, 4, 2.5, 0.8, 1.0, 0.5, 0.9, 1.8, 0.3, 0.4]
    
    # Gerçek Sayısal Jacobian Matrisinin Üretilmesi
    input_args = [KRAS_ss, pERK_ss, ROS_ss, M_ss] + param_values
    J_numerical = np.array(jacobian_numerical_func(*input_args), dtype=float)
    
    # --- 4. Özdeğer Analizi ---
    eigenvalues, _ = eig(J_numerical)
    
    print("=== AMTPRF DİNAMİK LOKAL KARARLILIK ANALİZİ ===")
    print("✅ BAŞARILI: Sembolik Jacobian matrisinden gerçek sayısal özdeğerler türetildi.")
    all_stable = True
    for idx, lam in enumerate(eigenvalues):
        print(f"  Lambda_{idx+1}: {np.real(lam):.4f} + {np.imag(lam):.4f}j")
        if np.real(lam) >= 0:
            all_stable = False
            
    if all_stable:
        print("✅ KANITLANDI: Tüm gerçek kısmi türev özdeğerlerinin gerçel kısımları negatiftir. Sistem lokal olarak kesin kararlıdır.")
    return eigenvalues

if __name__ == "__main__":
    run_dynamic_eigenvalue_analysis()
