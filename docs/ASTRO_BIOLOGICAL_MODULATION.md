# 🌌 Adaptive Multi-Threshold Proteostatic Regulation Framework (AMTPRF)
*Astrophysics-inspired state-transition modeling for theoretical systems biology.*

⚠️ **CRITICAL DISCLAIMER:** This module represents a non-validated, conceptual, and exploratory systems-biology architecture intended solely for theoretical modeling and computational simulations. It contains no biochemical data, wet-lab validation, or clinical parametric fitting.

## 1. Giriş ve Konsept Konumlandırması
The framework explores whether adaptive threshold-governed signaling control architectures can theoretically stabilize pathological signaling loads without requiring continuous inhibitory pressure. 

Klasik tek-hedef/tek-inhibitör modellerinin aksine, duruma ve yoğunluğa duyarlı, feedback kontrollü bir **Conceptual Adaptive Signaling Control Architecture** modelidir. Sistem, sürekli baskılama yapmak yerine hücre içi gürültüyü filtreleyerek sadece kritik stres eşiklerinde otonom kararlar alan bir hücresel otomat (state machine) gibi kurgulanmıştır.

*Conceptually inspired by gravitational collapse limits (Chandrasekhar and Schwarzschild limits),* bu modelde biyokimyasal sinyal yüklerinin lineer olmayan faz geçişleri (nonlinear state-transitions) matematiksel olarak soyutlanmıştır. Metaforlar mekanizmanın kendisi değil, matematiksel davranış biçiminin birer soyutlama aracıdır.

---

## 2. İleri Seviye Matematiksel Mimari ve Denklemler

### 📊 A. Kompozit Stres İndeksi (Composite Stress Index - CSI)
Sinyal ağlarındaki anlık piklerin (transient spikes) sistemi yanlışlıkla aktive etmesini önlemek amacıyla, çoklu sensör entegrasyonu sunan bir stres fonksiyonu kurgulanmıştır:
\[S(t) = \alpha [pERK] + \beta [KRAS\text{-}GTP] + \gamma [ROS]\]

### 🔄 B. Diferansiyel Histerezis ve Bellek Çekirdeği (Memory Kernel)
Sistemde yapay bir küresel değişken (global state) kullanmak yerine, biyolojik histerezis ve gürültü direnci (noise immunity) diferansiyel bir hafıza değişkeni ($M$) ve gecikme sabiti ($\tau_m$) ile modellenmiştir:
\[\tau_m \frac{dM}{dt} = \Theta(S) - M\]

### 🧫 C. Doygunluğa Ulaşan Koşullu Yıkım (Saturating Degradation)
Sistemin geri dönüşümsüz geçiş eşiği (*irreversible transition threshold*) aşılıp temizlik fazına geçildiğinde hücreyi kontrolsüz bir çöküşe (rebound activation) sokmamak adına, yıkım mekanizması Michaelis-Menten tipi doygunluğa ulaşan bir kinetikle sınırlandırılmıştır:
\[\frac{d[KRAS]}{dt} = k_{prod} - \left( \frac{k_{deg} \cdot [KRAS]}{K_m + [KRAS]} \right) \cdot M\]

### 📉 D. Metabolik Bağlı Negatif Feedback ve ROS Dinamiği
ROS (Oksidatif Stres) davranışı doğrudan hücre içi metabolik yüke ve KRAS aktivasyonuna bağlanarak sistemin kendi kendini söndüren (self-extinguishing) bir iç döngü kurması sağlanmıştır:
\[\frac{d[ROS]}{dt} = k_{ROS}[KRAS] - k_{clear}[ROS]\]
\[\frac{d[pERK]}{dt} = k_{act}[KRAS] - k_{fb} \cdot M \cdot [pERK]\]

---

## 3. Parametre Uzayı Keşfi ve Bifurcation Sınırları
Sistemin kararlılığı, parametrelerin duyarlılık analizine (parameter sensitivity analysis) bağlıdır.
*   **Ultra-sensitivity Regülasyonu ($n$):** $n=1$ durumunda sistem lineer ve yumuşak bir tepki verirken, $n \geq 4$ durumunda ani bir faz geçişi (bifurcation) göstererek "Chandrasekhar Çöküş Limiti" davranışını taklit eder.
*   **Kararlılık Rejimleri (Stability Landscape):** $k_{fb}$ (feedback gücü) ve $\tau_m$ (bellek gecikmesi) arasındaki oran, sistemin kararlı bir sönümlenmeye mi (attractor state) yoksa kronik osilasyonlara mı (limit cycle) gireceğini belirler.
