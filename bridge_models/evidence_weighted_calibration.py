import numpy as np

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
