import numpy as np
import json
import os

class EvidenceWeightedCalibration:
    def __init__(self, n_hill=2.0, k_half=75.0, residual_leakage=0.055):
        """
        Evidence-Weighted Parametric Calibration Framework.
        HADDOCK skorlarını Hill-Tipi saturasyon fonksiyonu ile C_eff katsayısına dönüştürür.
        """
        self.n_hill = n_hill
        self.k_half = k_half
        self.residual_leakage = residual_leakage

    def calculate_c_eff(self, haddock_score):
        abs_score = abs(haddock_score)
        saturation = (abs_score ** self.n_hill) / (self.k_half ** self.n_hill + abs_score ** self.n_hill)
        c_eff = saturation * (1.0 - self.residual_leakage)
        return c_eff

    def calibrate_parameters(self, tau_0, sigma_0, haddock_score, alpha=0.4, beta=0.3):
        """
        Prior constraint yama mantığı:
        A) tau_eff = tau_0 * (1 + alpha * C_eff)
        B) sigma_eff = sigma_0 * (1 - beta * C_eff)
        """
        c_eff = self.calculate_c_eff(haddock_score)
        tau_eff = tau_0 * (1.0 + alpha * c_eff)
        sigma_eff = sigma_0 * (1 - beta * c_eff)
        return tau_eff, sigma_eff, c_eff

# =========================================================================
# ORKESTRA ŞEFİ (MONTE CARLO) İÇİN YENİ EKLENEN VERİ VE SAF LOGISTIC MODÜLLERİ
# =========================================================================

def load_haddock_score_from_json(json_path="simulations/haddock_outputs.json"):
    """
    simulations klasoru altindaki gercek HADDOCK -62.3 skorunu okur.
    Dosya yolu projenin kok dizinine gore 'simulations/haddock_outputs.json' olarak ayarlanmistir.
    """
    if not os.path.exists(json_path):
        return -62.3, 3.0
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        wt_data = data.get("wild_type_srx", {})
        return float(wt_data.get("haddock_score", -62.3)), float(wt_data.get("haddock_std", 3.0))
    except Exception:
        return -62.3, 3.0

def compute_continuous_ceff(haddock_score, c_max=0.4519, k=0.1, s50=-62.3):
    """Kaba esik degerlerini ortadan kaldiran kesintisiz lojistik fonksiyon."""
    if haddock_score == 0: 
        return 0.0
    return c_max / (1.0 + np.exp(-k * (haddock_score - s50)))

