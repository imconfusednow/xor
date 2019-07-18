# takes in pop size, returns networks
# takes in ids => fitness dict. Returns new population
# creates species and networks
from network import Network
from species import Species
import math


class Population:
    def __init__(self, size, ins, outs, recurrent):
        self.size = size
        self.networks = []
        self.max_id = 0
        self.max_species_id = 1
        self.generation = 0
        self.cull = int(0.5 * self.size)
        for i in range(size):
            self.networks.append(
                Network(ins, outs, recurrent, self.max_id, {"neurons": [[], []], "connections": []}, True, False))
            self.max_id += 1
        self.species = [Species(0, self.networks[0].dna)]
        self.neuron_ids = set()
        self.connection_ids = set()

    def get_pop(self):
        return self.networks

    def next_gen(self, pop):
        self.generation += 1
        string = "////////////" + str(self.generation) + "///////////////" + str(
            len(self.species[0].members)) + " " + str(self.species[0].id)
        if len(self.species) > 1:
            string += " " + str(len(self.species[1].members))
        print(string)
        print(len(self.species))
        self.speciate(pop)
        self.extinct_species()
        self.cull_and_replace()
        self.networks = []
        for s in self.species:
            self.networks += s.members
        for p in self.networks:
            p.reset()

        self.get_unique_ids()

        return self.networks

    def cull_and_replace(self):
        fitness_sum = 0
        pass_on_extra = 0

        for s in self.species:
            fitness = s.set_fitness()
            fitness_sum += fitness

        for s in self.species:
            to_add = math.floor(s.fitness / fitness_sum * self.size) + pass_on_extra
            # print("ta", s.fitness, fitness_sum, self.size)
            # print(s.template_genome)
            if len(s.members) > 5:
                pass_on_extra = s.birth(to_add, True)
            else:
                pass_on_extra = s.birth(to_add, False)

    def speciate(self, pop):
        for s in self.species:
            s.members = []
        for p in range(len(pop)):
            matched = False
            for s in self.species:
                matched = s.matches_species(pop[p])
                if matched == True:
                    break
            if not matched:
                self.species.append(Species(self.max_species_id, pop[p].dna))
                self.max_species_id += 1
                self.species[-1].members.append(pop[p])

    def extinct_species(self):
        for i in range(len(self.species) - 1, -1, -1):
            if len(self.species[i].members) == 0:
                print("Species " + str(self.species[i].id) + " Extinct :(")
                del self.species[i]

    def get_unique_ids(self):
        self.neuron_ids.clear()
        self.connection_ids.clear()
        for n in self.networks:
            self.neuron_ids.update(n.neuron_ids)
            self.connection_ids.update(n.connection_ids)
