from population import Population
from network import Network
import csv

pop = Population(1000, 3, 1, False)
nets = pop.get_pop()
iterations = 500

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

        n.fitness = 6 - n.fitness * n.fitness
        if i < -1:
            n.fitness += n.max_node
        fitness_tot.append(n.fitness)
    # print(n.max_node)

    print(max(fitness_tot))
    arr = [""] * 100
    for s in pop.species:
        arr[s.id] = len(s.members)
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

genome = {'neurons': [[0, 1, 2], [8, 9], [13], [4, 5, 7], [11, 12], [6, 10], [3]],
          'connections': [[0, 3, -0.944025792542572, False], [1, 3, -1.2634873977934096, True],
                          [2, 3, -0.14839070192572384, True], [0, 4, -1.9211266404134486, False],
                          [4, 3, -0.9679015794005192, False], [2, 4, 0.06520460170364722, True],
                          [0, 5, 1.5992794573645839, True], [5, 3, 0.8829214991259409, False],
                          [5, 6, 0.1487934081536685, True], [6, 3, 1.8208899468186164, True],
                          [0, 7, 1.8745131876932912, True], [7, 3, 1.9322625170948406, True],
                          [1, 5, 1.110674367958645, False], [7, 6, -1.500792240990762, False],
                          [1, 8, 1.7776852738685187, True], [8, 5, 1.3940525087584785, True],
                          [8, 6, -0.9480528832577763, True], [8, 7, 1.5223272663513745, False],
                          [0, 9, 1.5597532976392283, True], [9, 4, -1.9748654925210387, True],
                          [9, 5, 0.6754943045420753, True], [4, 10, 1.7099518618590717, True],
                          [10, 3, 1.3312691267455685, True], [7, 11, 0.30213201705968384, True],
                          [11, 6, 1.1048353273848155, True], [7, 12, 0.9529117975956825, True],
                          [12, 6, 1.0985448494612005, True], [1, 9, -0.7459263502912232, True],
                          [8, 13, 0.7201690814723064, True], [13, 7, 1.9068678641588592, True],
                          [1, 13, 1.0014376355396628, True], [9, 13, 0.029616329966523844, True]]}
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
