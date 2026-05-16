# 🔬 NF1-Smart-Redirector-Model: Faz 2 Laboratuvar Protokolleri

Bu döküman, in silico ortamda 2.85 Å kilitlenme başarısı doğrulanan ve GROMACS altyapısı kurulan NF1 akıllı saptırıcı sisteminin ıslak laboratuvar (wet-lab) ortamında sentezlenmesi ve karakterizasyonu için Standart Operasyon Prosedürlerini (SOP) içerir.

---

## 🛡️ Protokol 1: Moleküler Zırh (PEGilasyon)

Amino-reaktif N-Hidroksisüksinimid (NHS) kimyası kullanılarak protein yüzeyindeki lizinsiz amino gruplarının zırhlanması hedeflenmiştir.

### Reaktif Reçetesi
*   **Ana Kompleks:** 1.0 mg/mL stok konsantrasyon (pH 7.4 sterile PBS tamponunda).
*   **Zırh Ajanı:** mPEG-NHS (5 kDa).
*   **Molar Oran:** 1:20 (Hedef Protein : PEG).

### Deneysel Basamaklar
1. 1.0 mL protein çözeltisini sterile ependorf tüpüne alın.
2. Reaksiyondan hemen önce **3.3 mg mPEG-NHS** tartarak 100 µL susuz DMSO içinde hızla çözün.
3. PEG çözeltisini protein tüpüne damla damla eklerken hafifçe vorteksleyin.
4. Karışımı 4°C sıcaklıkta, orbital çalkalayıcıda 16 saat inkübe edin.
5. Reaksiyonu durdurmak için 50 µL 1 M Tris-HCl (pH 7.5) ekleyin ve oda sıcaklığında 15 dakika bekletin.
6. Serbest PEG'leri uzaklaştırmak için 10 kDa MWCO santrifüj filtre tüplerinde, 4°C'de 4000 rpm hızda PBS ile 3 kez yıkayarak saflaştırın.

---

## 💊 Protokol 2: Lipid Nanopartikül (LNP) Kapsülleme

Zırhlanmış yapının hücresel bariyerleri aşması amacıyla mikrofluidik çip üzerinde kontrollü enkapsülasyonu sürecidir.

### 1. Lipid (Organik) Faz Bileşimi (Mutlak Alkol İçinde)
*   **DLin-MC3-DMA (İyonize Lipid):** %50 Molar
*   **DSPC (Yardımcı Lipid):** %10 Molar
*   **Kolesterol:** %38.5 Molar
*   **DMG-PEG2000 (Pegile Lipid):** %1.5 Molar

### 2. Sulu Faz Bileşimi
*   Zırhlanmış kompleks molekülü, **50 mM Sodyum Sitrat Tamponu (pH 4.0)** içerisinde çözülerek net pozitif yük kazanması sağlanır.

### 3. Mikro-Akışkan Parametreleri
*   **Akış Hızı Oranı (FRR):** Sulu Faz : Organik Faz = 3 : 1
*   **Toplam Akış Hızı (TFR):** > 12 mL/dk
*   **Nihai İşlem:** Sentezlenen LNP süspansiyonu süratle sterile 1X PBS (pH 7.4) tamponuna karşı diyaliz edilerek etanol tamamen uzaklaştırılır ve dış faz nötrleştirilir.

---

## 📊 Protokol 3: Kalite Kontrol (QC) Eşik Değerleri

Sentez sonrası ekibin onaylaması gereken kalite kriterleri:
*   **DLS Analizi:** Hidrodinamik çap = 80 - 120 nm aralığı, PDI < 0.2.
*   **Enkapsülasyon Verimi (%EE):** RiboGreen/BCA testi ile %EE > %80.
*   **Kararlılık:** Trypsin sindirim testi sonrası SDS-PAGE jelinde zırh bandının bütünlüğü.