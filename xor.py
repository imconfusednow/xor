from population import Population
from network import Network
import csv
import pygame

pop = Population(1000, 3, 1, False)
nets = pop.get_pop()
iterations = 500
pygame.init()

with open('H:\\Documents\\Coding_projects\\xor\\data\\scores.csv', mode='w') as csv_file:
    csv_file = csv.writer(csv_file)
    csv_file.writerow(["Score"])

for i in range(iterations):
    fitness_tot = []
    for n in nets:
        answer = n.feed_forward([0, 0, 1])[0]
        n.fitness += abs(0 - answer)
        answer = n.feed_forward([1, 0, 1])[0]
        n.fitness += abs(1 - answer)
        answer = n.feed_forward([0, 1, 1])[0]
        n.fitness += abs(1 - answer)
        answer = n.feed_forward([1, 1, 1])[0]
        n.fitness += abs(0 - answer)

        n.fitness = 36 - n.fitness * n.fitness
        if i < -1:
            n.fitness += n.max_node
        fitness_tot.append(n.fitness)
    # print(n.max_node)

    print(max(fitness_tot))
    arr = [""] * 100
    #for s in pop.species:
    #    arr[s.id * 2] = len(s.members)
    #    arr[s.id * 2 + 1] = s.fitness
    arr[0] = pop.species[0].fitness
    arr[1] = pop.this_to_add
    arr[2] = pop.fitness_sum
    with open('H:\\Documents\\Coding_projects\\xor\\data\\scores.csv', mode='a', newline='') as csv_file:
        csv_file = csv.writer(csv_file, delimiter=',')
        csv_file.writerow(arr)
    # print("look here", len(nets))
    # print(len(nets))
    nets = pop.next_gen(nets)
    print(len(nets))

# print(nets[0].dna)
# print(nets[1].dna)

print(nets[0].dna)

genome = {'neurons': [[0, 1, 2], [7, 8], [12], [11], [6], [5], [9], [10], [4], [3]], 'connections': [[0, 3, -1.61068238756397, True], [1, 3, -2, True], [2, 3, -1.9016421895983942, False], [2, 4, -1.5118830463832729, False], [4, 3, 1.7783051695458865, True], [2, 5, -1.4523303362180453, False], [5, 4, 0.23992324169997953, False], [2, 6, -1.8635762792489268, False], [6, 5, 1.986641144670756, True], [1, 4, 1.9532014978519299, True], [0, 5, -1.9822767704211854, False], [2, 7, 0.0014160730375986494, True], [7, 6, -0.12877820677522253, False], [0, 8, -1.3653238043206077, True], [8, 5, 1.8320607138157814, True], [0, 4, 1.8970493679226446, True], [5, 3, -1.9146452300463124, True], [5, 9, 0.6064248931380958, True], [9, 4, -1.5727071016272092, False], [1, 6, -1.93688124366907, True], [8, 9, -0.7380437557289827, True], [9, 3, -1.7788641022960707, True], [6, 4, -1.3433278348320798, True], [7, 9, 1.4834625272034079, True], [8, 6, 1.2850806055439896, True], [9, 10, 1.013212080138252, True], [10, 4, 0.8948893064460666, True], [5, 10, -0.7599570371246905, True], [7, 11, 0.9980607914710106, False], [11, 6, -0.11543372160711206, True], [6, 10, -0.1961561271911504, True], [11, 4, -0.74727109023934, True], [11, 10, 0.10718790570432102, True], [7, 12, 1, True], [12, 11, 0.9980607914710106, True]]}
n = Network(3, 1, False, 1, genome, False, False)

answer = n.feed_forward([0, 0, 1])[0]
print(answer)

n.fitness += abs(0 - answer)
answer = n.feed_forward([1, 0, 1])[0]

print(answer)
n.fitness += abs(1 - answer)
answer = n.feed_forward([0, 1, 1])[0]

print(answer)
n.fitness += abs(1 - answer)
answer = n.feed_forward([1, 1, 1])[0]

print(answer)
n.fitness += abs(0 - answer)

print(6 - n.fitness)
