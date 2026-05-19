import os
import json
import numpy as np

def calculate_biophysical_bridge(mean_distance_angstrom, num_contacts):
    # Gaz sabiti ve fizyolojik sıcaklık tanımları
    R = 8.314e-3  
    T = 310.15     
    
    # Fenomenolojik afinite skorlaması (Proxy ΔG)
    if mean_distance_angstrom > 0:
        base_affinity = (num_contacts / mean_distance_angstrom) * 0.5
    else:
        base_affinity = 0
        
    delta_G = -base_affinity * 2.303 * (R * T)
    
    # Ayrışma sabiti ve fiziksel sınır filtreleme (Clamping)
    K_d_raw = np.exp(delta_G / (R * T))
    K_d = np.clip(K_d_raw, 1e-12, 1e-3) 
    
    # Langmuir Reseptör Doluluk Olasılığı (Occupancy θ)
    ligand_concentration = 10e-9 
    occupancy = ligand_concentration / (K_d + ligand_concentration) if (K_d + ligand_concentration) > 0 else 0
    
    # Çok Ölçekli Parametre Ağırlıklarının Güncellenmesi
    kras_weight = 0.4 * (1.0 - occupancy)
    perk_weight = 0.5 * (1.0 - occupancy)
    ros_weight  = 0.1
    
    total_w = kras_weight + perk_weight + ros_weight
    kras_weight_norm = kras_weight / total_w
    perk_weight_norm = perk_weight / total_w
    ros_weight_norm = ros_weight / total_w
    
    # Parametre Soykütüğü İzleme Matrisi (Provenance Tracking)
    parameter_trace = {
        "provenance_metadata": {
            "framework_layer": "Multi-Scale Translational Mapping Bridge"
        },
        "upstream_structural_inputs": {
            "mean_distance_angstrom": float(mean_distance_angstrom),
            "num_contacts": int(num_contacts)
        },
        "downstream_systems_outputs": {
            "fractional_occupancy_probability": float(occupancy),
            "derived_normalized_weights": {
                "KRAS_weight": float(kras_weight_norm),
                "pERK_weight": float(perk_weight_norm),
                "ROS_weight": float(ros_weight_norm)
            }
        }
    }
    
    if not os.path.exists('bridge_models'):
        os.makedirs('bridge_models')
        
    with open('bridge_models/parameter_trace.json', 'w', encoding='utf-8') as f_out:
        json.dump(parameter_trace, f_out, indent=4, ensure_ascii=False)
        
    return parameter_trace

if __name__ == "__main__":
    calculate_biophysical_bridge(mean_distance_angstrom=2.85, num_contacts=45)
