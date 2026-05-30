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
        self.population = [self._generate_random_rna() for _ in range(self.pop_size)]

    def _generate_random_rna(self):
        return ''. join(random.choice(self.nucleotides) for _ in range(self.sequence_length))

    def predict_structural_metrics(self, rna_sequence):
        """
        In silico tarama filtresi. RNA sekans özelliklerinden (GC içeriği, motifler)
        HADDOCK Skoru ve BSA tahmini yapar.
        """
        gc_content = (rna_sequence.count('G') + rna_sequence.count('C')) / len(rna_sequence)
        predicted_haddock = -40.0 - (gc_content * 60.0) - random.uniform(-5, 5)
        predicted_bsa = 800.0 + (gc_content * 600.0) + random.uniform(-5, 5)
        return min(max(predicted_haddock, -120.0), 0.0), min(max(predicted_bsa, 400.0), 1500.0)

    def evaluate_fitness(self, rna_sequence):
        """
        REVISED ACADEMIC FITNESS FUNCTION:
        Teorik denge noktası (x* = -1.8156) merkezli yörünge pürüzsüzlüğünü ve 
        asimptotik kilitlenme başarısını ölçer.
        """
        haddock_score, bsa = self.predict_structural_metrics(rna_sequence)
        constraints = self.calibration_bridge.constrain_parameter_space(haddock_score, bsa, fcc=0.75)
        
        # SDE/DDE Simülasyonu
        model = ColoredNoiseLangevinModel()
        _, trajectory = model.simulate(tau_eff=constraints["tau_constrained"], sigma_eff=constraints["sigma_constrained"])
        
        # Asimptotik Kararlı Evre Analizi (Son %40'lık kısım)
        steady_state = trajectory[int(len(trajectory) * 0.6):]
        diffs = np.diff(steady_state)
        
        # Metriklerin Türetilmesi (Confinement, TSI, Oscillation, Divergence)
        target_equilibrium = -1.8156
        confinement_error = np.mean((steady_state - target_equilibrium) ** 2)
        confinement_score = 1.0 / (1.0 + confinement_error)
        trajectory_smoothness = 1.0 / (1.0 + np.var(diffs))
        oscillation_energy = np.mean(diffs ** 2) / 0.01  # dt=0.01
        divergence_penalty = max(0.0, np.max(np.abs(trajectory)) - 3.5)
        
        # Ağırlıklandırılmış Objective Fonksiyonu
        fitness_score = (2.5 * confinement_score) + (1.5 * trajectory_smoothness) - \
                        (0.4 * oscillation_energy) - (4.0 * divergence_penalty)
        return max(0.0001, fitness_score)

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
            next_gen = self.population[:2]  # En iyi 2 elit korundu
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



