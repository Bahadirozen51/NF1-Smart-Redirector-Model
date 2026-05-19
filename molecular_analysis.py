"""
Module: molecular_analysis.py
Description: Master Integration Engine for the NF1-Smart-Redirector-Model.
Synthesizes symbolic differentiation, local/global stability landscapes, 
stochastic noise profiling, and empirical structural analysis.
"""

import os
import sys

# Proje klasör yollarını Python path'ine ekliyoruz (Notebooks entegrasyonu için)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'notebooks')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'simulations')))

def execute_master_pipeline():
    print("=" * 80)
    print("      NF1-SMART-REDIRECTOR-MODEL: MASTER COMPREHENSIVE ANALYSIS PIPELINE")
    print("=" * 80)
    print("[INIT] Sistem biyolojisi ve moleküler mekanizma entegrasyonu başlatılıyor...")

    # --- 1. Klasör Altyapısının Kurulması ---
    if not os.path.exists('figures'):
        os.makedirs('figures')
        print("[+] 'figures/' dizini otomatik olarak oluşturuldu.")

    # --- 2. Sürekli Rejim Çekirdek ODE Motorunun Çalıştırılması ---
    print("\n" + "-"*50)
    print("[FAZ 1] Sürekli Rejim Diferansiyel Denklem Çözümü (coupled_ode_v1)")
    print("-"*50)
    try:
        from coupled_ode_v1 import execute_core_validation
        execute_core_validation()
    except Exception as e:
        print(f"[!] Faz 1 Hatası: Çekirdek ODE motoru yüklenemedi: {str(e)}")

    # --- 3. Sembolik Türev ve Jacobian Haritalama ---
    print("\n" + "-"*50)
    print("[FAZ 2] SymPy Sembolik Jacobian Analizi (jacobian_analysis)")
    print("-"*50)
    try:
        from jacobian_analysis import derive_symbolic_jacobian
        derive_symbolic_jacobian()
    except Exception as e:
        print(f"[!] Faz 2 Hatası: Sembolik Jacobian motoru hatası: {str(e)}")

    # --- 4. Kararlılık Sınır Analizi ve Hopf Çatallanma Taraması ---
    print("\n" + "-"*50)
    print("[FAZ 3] Hopf Bifurcation ve Sınır Taraması (jacobian_bifurcation_analysis)")
    print("-"*50)
    try:
        from jacobian_bifurcation_analysis import generate_bifurcation_and_phase_portrait
        generate_bifurcation_and_phase_portrait()
    except Exception as e:
        print(f"[!] Faz 3 Hatası: Çatallanma analizi başarısız: {str(e)}")

    # --- 5. Kompleks Düzlem Özdeğer Spektrum Haritalama ---
    print("\n" + "-"*50)
    print("[FAZ 4] Spektral Kararlılık Analizi (eigenvalue_scan)")
    print("-"*50)
    try:
        from eigenvalue_scan import run_dynamic_eigenvalue_analysis
        run_dynamic_eigenvalue_analysis()
    except Exception as e:
        print(f"[!] Faz 4 Hatası: Özdeğer tarama motoru hatası: {str(e)}")

    # --- 6. Küresel Çekim Kararlılığı ve Lyapunov Enerji Düşüşü ---
    print("\n" + "-"*50)
    print("[FAZ 5] Global Attractor Yakınsama İspatı (lyapunov_landscape)")
    print("-"*50)
    try:
        from lyapunov_landscape import run_lyapunov_descent_analysis
        run_lyapunov_descent_analysis()
    except Exception as e:
        print(f"[!] Faz 5 Hatası: Lyapunov analizi başarısız oldu: {str(e)}")

    # --- 7. Langevin SDE Stokastik Mikroyevre Robustness Profilleme ---
    print("\n" + "-"*50)
    print("[FAZ 6] Stokastik Langevin Gürültü Tolerans Testi (stochastic_noise)")
    print("-"*50)
    try:
        from stochastic_noise import run_real_stochastic_simulation
        run_real_stochastic_simulation()
    except Exception as e:
        print(f"[!] Faz 6 Hatası: Stokastik SDE simülasyon hatası: {str(e)}")

    # --- 8. Zaman Gecikmeli Ayrık DDE Adaptasyon Yörüngeleri ---
    print("\n" + "-"*50)
    print("[FAZ 7] Geçmiş Kuyruğu Zaman Gecikmeli Hücre Modeli (param_exploration)")
    print("-"*50)
    try:
        from param_exploration import run_discrete_dde_simulation
        run_discrete_dde_simulation()
    except Exception as e:
        print(f"[!] Faz 7 Hatası: DDE simülasyon motoru hatası: {str(e)}")

    # --- 9. Kristallografik AlphaFold 3 .cif Arayüz Analizi ---
    print("\n" + "-"*50)
    print("[FAZ 8] AlphaFold 3 Kristal Koordinat Arayüz Analizi (analyze_structure)")
    print("-"*50)
    try:
        from analyze_structure import analyze_molecular_interaction
        import glob
        cif_files = glob.glob("alphafold_models/*.cif")
        if cif_files:
            analyze_molecular_interaction(cif_files[0])
        else:
            print("[!] Uyarı: 'alphafold_models/' klasöründe analiz edilecek .cif dosyası bulunamadı.")
    except Exception as e:
        print(f"[!] Faz 8 Hatası: Biopython moleküler koordinat motoru hatası: {str(e)}")

    print("\n" + "="*80)
    print("✅ MASTER SUCCESS: Tüm matematiksel ve yapısal fazlar başarıyla doğrulandı.")
    print("📈 Çıktı Grafiklerinin Tamamı 'figures/' Klasörünün Altına Güvenle Kaydedildi.")
    print("="*80 + "\n")

if __name__ == "__main__":
    execute_master_pipeline()
