# takes matching networks

from network import Network

import copy
import math
import numpy


class Species:

    def __init__(self, id, genome):
        self.id = id
        self.members = []
        self.template_genome = genome
        self.gene_coef = 1.0
        self.weight_coef = 0.4
        self.divergence_theshold = 4.0
        self.fitness = 0
        self.age = 0

    def birth(self, to_add, champ):
        new_pop = []
        self.sort_species(self.members)
        self.cull(self.members)
        if len(self.members) < 1:
            self.members = []
            return 1
        if champ:
            new_pop.append(Network(self.members[0].ins, self.members[0].outs, self.members[0].recurrent, 1,
                                   copy.deepcopy(self.members[0].dna), False, False))
            to_add -= 1
        for i in range(to_add):
            mem = self.choose_net()
            new_pop.append(Network(mem.ins, mem.outs, mem.recurrent, 1, copy.deepcopy(mem.dna), False, True))

        self.members = new_pop

        self.age += 1

        return 0

    def cull(self, pop):
        if self.age == 0: return
        self.members = pop[0: math.floor(len(self.members) * 0.5)]
        self.set_fitness()

    def choose_net(self):
        tot = 0
        rand = numpy.random.uniform(0, self.fitness)
        for i in self.members:
            tot += i.fitness
            if tot >= rand:
                return i

        tot = 0
        for i in self.members:
            tot += i.fitness

        # print(tot)
        # print(rand, self.fitness)
        print(self.id)

        print("No network choosen. Brace for crash!!")
        print(self.members)

    def matches_species(self, potential):
        if self.compare_genome(potential):
            self.members.append(potential)
            return True
        else:
            return False

    def compare_genome(self, potential):
        genome = potential.dna
        divergence = 0
        different_genes = 0
        weight_difference = 0
        matches = 0

        for c in genome["connections"]:
            for c2 in self.template_genome["connections"]:
                matched = False
                if c[0] == c2[0] and c[1] == c2[1]:
                    weight_difference += abs(c[2] - c2[2])
                    matches += 1
                    matched = True
                    break
            if not matched: different_genes += 1

        if matches == 0:
            return False

        weight_difference /= matches

        genome_normaliser = len(genome["connections"]) - 20.0
        if genome_normaliser < 1:
            genome_normaliser = 1

        divergence = ((self.gene_coef * different_genes) / genome_normaliser) + (self.weight_coef * weight_difference)

        return divergence < self.divergence_theshold

    def sort_species(self, curr_pop):
        self.members = sorted(curr_pop, key=lambda x: x.adj_fitness, reverse=True)

    def set_fitness(self):
        self.fitness = 0
        for m in self.members:
            m.adj_fitness = m.fitness / len(self.members)
            self.fitness += m.adj_fitness

        return self.fitness
