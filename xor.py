from population import Population
from network import Network
from dataconf import DataConf
import csv
import pygame

pop = Population(1000, 3, 1, False)
nets = pop.get_pop()
iterations = 100
pygame.init()

win = pygame.display.set_mode((500,500))

data_handler = DataConf(win)



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
	print(len(nets))
	arr = [""] * 100
	# for s in pop.species:
	#	arr[s.id * 2] = len(s.members)
	#	arr[s.id * 2 + 1] = s.fitness
	arr[0] = pop.species[0].fitness
	arr[1] = pop.this_to_add
	arr[2] = pop.fitness_sum
	with open('H:\\Documents\\Coding_projects\\xor\\data\\scores.csv', mode='a', newline='') as csv_file:
		csv_file = csv.writer(csv_file, delimiter=',')
		csv_file.writerow(arr)
	# print("look here", len(nets))
	# print(len(nets))
	if i == iterations - 1: break
	nets = pop.next_gen(nets)

	#data_handler.draw_net(nets[0].dna)

	should_stop = False
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			should_stop = True

	if should_stop: break

# print(nets[0].dna)
# print(nets[1].dna)



max_fit = 0
curr_i = 0
for i in range(len(nets)):
	if nets[i].fitness > max_fit:
		max_fit = nets[i].fitness
		curr_i = i

data_handler.save(nets, "save")

genome = data_handler.load("save")[1]
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
