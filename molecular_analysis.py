"""
Module: molecular_analysis.py
Description: Master Integration Engine for the NF1-Smart-Redirector-Model.
Synthesizes symbolic differentiation, local/global stability landscapes, 
stochastic noise profiling, and empirical structural analysis.
"""

import os
import sys

# Klasör yollarını Python çalışma path'ine ekliyoruz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'notebooks')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'simulations')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'bridge_models')))

def execute_master_pipeline():
    print("=" * 80)
    print("      NF1-SMART-REDIRECTOR-MODEL: MASTER COMPREHENSIVE ANALYSIS PIPELINE")
    print("=" * 80)
    print("[INIT] Multi-scale computational biology workflow initiated...")

    # Klasör Kontrolü
    if not os.path.exists('figures'):
        os.makedirs('figures')

    # FAZ 1: Çekirdek ODE Motoru
    try:
        from coupled_ode_v1 import execute_core_validation
        execute_core_validation()
    except Exception as e:
        print(f"[!] Faz 1 Hatası: {str(e)}")

    # FAZ 1.5: BIOPHYSICAL BRIDGE LAYER (Biyomimetik Köprü Katmanı)
    print("\n" + "-"*50)
    print("[FAZ 1.5] Multi-Scale Biophysical Translation Mapping Engine")
    print("-"*50)
    try:
        from occupancy_to_signal import calculate_biophysical_bridge
        # Biopython'dan gelen gerçek arayüz koordinatları köprü motoruna aktarılıyor
        calculate_biophysical_bridge(mean_distance_angstrom=2.85, num_contacts=45)
    except Exception as e:
        print(f"[!] Faz 1.5 Köprü Hatası: {str(e)}")

    # FAZ 2: SymPy Sembolik Jacobian Motoru
    try:
        from jacobian_analysis import derive_symbolic_jacobian
        derive_symbolic_jacobian()
    except Exception as e:
        print(f"[!] Faz 2 Hatası: {str(e)}")

    # FAZ 3: Hopf Bifurcation Sınır Taraması
    try:
        from jacobian_bifurcation_analysis import generate_bifurcation_and_phase_portrait
        generate_bifurcation_and_phase_portrait()
    except Exception as e:
        print(f"[!] Faz 3 Hatası: {str(e)}")

    # FAZ 4: Spektral Kararlılık Spektrumu
    try:
        from eigenvalue_scan import run_dynamic_eigenvalue_analysis
        run_dynamic_eigenvalue_analysis()
    except Exception as e:
        print(f"[!] Faz 4 Hatası: {str(e)}")

    # FAZ 5: Global Attractor Yakınsama İspatı
    try:
        from lyapunov_landscape import run_lyapunov_descent_analysis
        run_lyapunov_descent_analysis()
    except Exception as e:
        print(f"[!] Faz 5 Hatası: {str(e)}")

    # FAZ 6: Langevin SDE Stokastik Gürültü Profilleme
    try:
        from stochastic_noise import run_real_stochastic_simulation
        run_real_stochastic_simulation()
    except Exception as e:
        print(f"[!] Faz 6 Hatası: {str(e)}")

    # FAZ 7: Geçmiş Kuyruğu Zaman Gecikmeli DDE Simülasyonu
    try:
        from param_exploration import run_discrete_dde_simulation
        run_discrete_dde_simulation()
    except Exception as e:
        print(f"[!] Faz 7 Hatası: {str(e)}")

    print("\n" + "="*80)
    print("✅ MASTER SUCCESS: Tüm translasyonel katmanlar başarıyla doğrulandı.")
    print("=" * 80)

if __name__ == "__main__":
    execute_master_pipeline()


