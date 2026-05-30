import random
import numpy as np
from bridge_models.evidence_weighted_calibration import EvidenceWeightedCalibration
from simulations.colored_noise_langevin_model import ColoredNoiseLangevinModel

class RNAGeneticOptimizer:
    def __init__(self, sequence_length=30, pop_size=20, mutation_rate=0.05):
        self.sequence_length = sequence_length
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate
        self.nucleotides = ['A', 'U', 'G', 'C']
        self.calibration_bridge = EvidenceWeightedCalibration()
        
        # Popülasyonu rastgele RNA dizilimleriyle başlat
        self.population = [self._generate_random_rna() for _ in range(self.pop_size)]

    def _generate_random_rna(self):
        return ''.join(random.choice(self.nucleotides) for _ in range(self.sequence_length))

    def predict_structural_metrics(self, rna_sequence):
        """
        In silico tarama filtresi. RNA sekans özelliklerinden (GC içeriği, motifler)
        HADDOCK Skoru ve BSA tahmini yapar (ViyanaRNA veya ampirik matris modeli).
        """
        # Biyofiziksel varsayım: GC içeriği ve uzunluk, yapısal arayüz alanını (BSA) artırır.
        gc_content = (rna_sequence.count('G') + rna_sequence.count('C')) / len(rna_sequence)
        
        # HADDOCK Score tahmini (-120 ile 0 arası sınırlandırılmış)
        predicted_haddock = -40.0 - (gc_content * 60.0) - random.uniform(-5, 5)
        # BSA tahmini (400 ile 1500 Å² arası sınırlandırılmış)
        predicted_bsa = 800.0 + (gc_content * 600.0) + random.uniform(-50, 50)
        
        return min(max(predicted_haddock, -120.0), 0.0), min(max(predicted_bsa, 400.0), 1500.0)

    def evaluate_fitness(self, rna_sequence):
        """
        FITNESS FUNCTION: RNA'nın dinamik sistem üzerindeki sönümleme başarısı.
        """
        # 1. Yapısal metrik tahmini
        haddock_score, bsa = self.predict_structural_metrics(rna_sequence)
        
        # 2. Köprü modelinden sınırlayıcı parametreleri (tau ve sigma) çekme
        constraints = self.calibration_bridge.constrain_parameter_space(haddock_score, bsa, fcc=0.75)
        
        # 3. SDE/DDE Simülasyon Motorunu test etme
        # Motor, atanan tau ve sigma parametreleriyle sistemi çözer
        model = ColoredNoiseLangevinModel()
        time, trajectory = model.simulate(
            tau_eff=constraints["tau_constrained"], 
            sigma_eff=constraints["sigma_constrained"]
        )
        
        # 4. Amplitüd Sönümleme Ölçümü (Oscillation Amplitude / Variance)
        # Sinyal varyansı ne kadar düşükse, hücre uyuşukluk havzasına o kadar iyi sabitlenmiştir.
        trajectory_variance = np.var(trajectory[-200:]) # Son 200 adımdaki kararlılık
        
        # Fitness Skoru: Varyansı minimize, C_eff'i maksimize eden formül
        fitness = constraints["C_eff"] / (1.0 + trajectory_variance)
        return fitness

    def evolve(self, generations=10):
        """
        Popülasyonu nesiller boyu evrimleştirerek en ideal RNA dizisini bulur.
        """
        for gen in range(generations):
            scores = [self.evaluate_fitness(ind) for ind in self.population]
            
            # Seçim ve Elitizm (En iyi bireyleri koru)
            sorted_indices = np.argsort(scores)[::-1]
            self.population = [self.population[i] for i in sorted_indices]
            
            # Yeni nesli oluştur (Crossover & Mutation)
            next_gen = self.population[:2] # En iyi 2 elit korundu
            
            while len(next_gen) < self.pop_size:
                p1, p2 = random.choice(self.population[:5]), random.choice(self.population[:5])
                # Tek noktalı çaprazlama (Crossover)
                cut = random.randint(5, self.sequence_length - 5)
                child = p1[:cut] + p2[cut:]
                
                # Mutasyon
                child_list = list(child)
                for i in range(len(child_list)):
                    if random.random() < self.mutation_rate:
                        child_list[i] = random.choice(self.nucleotides)
                
                next_gen.append(''.join(child_list))
                
            self.population = next_gen
            print(f"Generation {gen+1} | Max Fitness: {max(scores):.4f} | Best RNA: {self.population[0][:10]}...")
            
        return self.population[0]

