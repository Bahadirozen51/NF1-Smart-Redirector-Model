"""
Module: analyze_structure.py
Description: Analyzes spatial atom coordinates from AlphaFold 3 Multimer 
crystallographic (.cif) files to quantify RNA-Protein interfaces.
"""

import os
import glob
import numpy as np
import matplotlib.pyplot as plt
from Bio.PDB.MMCIFParser import MMCIFParser
from Bio.PDB import NeighborSearch

def analyze_molecular_interaction(cif_file, rna_chain_id="B", protein_chain_id="A", distance_cutoff=5.0):
    """
    Analyzes true spatial coordinates from the AlphaFold 3 output file, 
    computing actual binding metrics and distance distributions.
    """
    # --- Klasör Kontrolü ---
    if not os.path.exists('figures'):
        os.makedirs('figures')

    print(f"\n[-] {cif_file} dosyası yükleniyor ve mekansal analiz yapılıyor...")
    
    # MMCIFParser ile moleküler yapıyı belleğe alıyoruz
    parser = MMCIFParser(QUIET=True)
    structure = parser.get_structure("NF1_Model", cif_file)
    model = structure[0]
    
    # Zincir atomlarını filtreliyoruz
    protein_atoms = [atom for chain in model if chain.id == protein_chain_id for atom in chain.get_atoms()]
    rna_atoms = [atom for chain in model if chain.id == rna_chain_id for atom in chain.get_atoms()]
    
    if not protein_atoms or not rna_atoms:
        print("[!] Hata: Belirtilen Zincir (Chain) ID'leri dosyada bulunamadı!")
        return
    
    # Komşuluk aramasıyla arayüz (interface) analizi yapıyoruz
    searcher = NeighborSearch(protein_atoms)
    interacting_residues = set()
    distances = []
    
    for rna_atom in rna_atoms:
        close_protein_atoms = searcher.search(rna_atom.coord, distance_cutoff)
        for p_atom in close_protein_atoms:
            residue = p_atom.get_parent()
            interacting_residues.add((residue.get_resname(), residue.id[1]))
            
            # Gerçek Öklid mesafesi hesaplanıyor
            dist = np.linalg.norm(rna_atom.coord - p_atom.coord)
            distances.append(dist)
            
    print(f"[+] Analiz Tamamlandı!")
    print(f"--> Belirlenen Kritik Etkileşim Noktası Sayısı: {len(interacting_residues)}")
    print(f"--> Ortalama Bağlanma Mesafesi: {np.mean(distances):.2f} Å (Angstrom)")
    
    # --- Arayüz Mesafe Dağılım Grafiği ---
    plt.figure(figsize=(8, 5))
    plt.hist(distances, bins=20, color='teal', edgecolor='black', alpha=0.7)
    plt.title("SRX-RNA01 ve Hedef Protein Arasındaki Mesafe Dağılımı")
    plt.xlabel("Mesafe (Å - Angstrom)")
    plt.ylabel("Etkileşen Atom Sayısı")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Grafik yolu figures klasörüne taşındı
    plt.savefig("figures/molecular_interaction_distances.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("[+] Etkileşim grafiği 'figures/molecular_interaction_distances.png' olarak kaydedildi.")
    
    return sorted(list(interacting_residues), key=lambda x: x[1])

if __name__ == "__main__":
    print("=" * 80)
    print("ALPHAFOLD 3 YAPI ANALİZ MOTORU: BIOPYTHON KOORDİNAT ENTEGRASYONU")
    print("=" * 80)

    # alphafold_models klasörünün içindeki ilk .cif dosyasını otomatik bulur
    cif_dosyalari = glob.glob("alphafold_models/*.cif")
    
    if cif_dosyalari:
        secilen_dosya = cif_dosyalari[0]
        analyze_molecular_interaction(secilen_dosya)
    else:
        print("\n[!] Uyarı: 'alphafold_models' klasöründe analiz edilecek '.cif' uzantılı bir AlphaFold dosyası bulunamadı.")
    print("=" * 80)

