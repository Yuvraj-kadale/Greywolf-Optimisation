import random
import math # cos() for Rast_rigin
import copy 
import sys	 
def fitness_Rast_rigin(loc):
	value_fitness = 0.0
	for i in range(len(loc)):
		xi = loc[i]
	value_fitness += (xi * xi) - (10 * math.cos(2 * math.pi * xi)) + 10
	return value_fitness

#sphere function
def fitness_sphere(loc):
	value_fitness = 0.0
	for i in range(len(loc)):
		xi = loc[i]
		value_fitness += (xi*xi);
	return value_fitness;
class wolf:
	def __init__(self, fitness, dimension, minimum_X, maximum_x, seed):
		self.rnd = random.Random(seed)
		self.loc = [0.0 for i in range(dimension)]
		for i in range(dimension):
			self.loc[i] = ((maximum_x - minimum_X) * self.rnd.random() + minimum_X)

			self.fitness = fitness(self.loc) # curr fitness



# grey wolf optimization (GWO)
def gwo(fitness, max_iter, n, dimension, minimum_X, maximum_x):
	rnd = random.Random(0)

	# create n random wolves
	population = [ wolf(fitness, dimension, minimum_X, maximum_x, i) for i in range(n)]

	# On the basis of fitness values of wolves
	# sort the population in asc order
	population = sorted(population, key = lambda temp: temp.fitness)

	# best 3 solutions will be called as
	# alpha, beta and gaama
	alpha_wolf, beta_wolf, gamma_wolf = copy.copy(population[: 3])


	# main loop of gwo
	Iter = 0
	while Iter < max_iter:

		# after every 10 iterations
		# print iteration number and best fitness value so far
		if Iter % 10 == 0 and Iter > 1:
			print("Iter = " + str(Iter) + " best fitness = %.3f" % alpha_wolf.fitness)

		# linearly decreased from 2 to 0
		a = 2*(1 - Iter/max_iter)

		# updating each population member with the help of best three members
		for i in range(n):
			A1, A2, A3 = a * (2 * rnd.random() - 1), a * (
			2 * rnd.random() - 1), a * (2 * rnd.random() - 1)
			C1, C2, C3 = 2 * rnd.random(), 2*rnd.random(), 2*rnd.random()

			X1 = [0.0 for i in range(dimension)]
			X2 = [0.0 for i in range(dimension)]
			X3 = [0.0 for i in range(dimension)]
			Xnew = [0.0 for i in range(dimension)]
			for j in range(dimension):
				X1[j] = alpha_wolf.loc[j] - A1 * abs(
				C1 * alpha_wolf.loc[j] - population[i].loc[j])
				X2[j] = beta_wolf.loc[j] - A2 * abs(
				C2 * beta_wolf.loc[j] - population[i].loc[j])
				X3[j] = gamma_wolf.loc[j] - A3 * abs(
				C3 * gamma_wolf.loc[j] - population[i].loc[j])
				Xnew[j]+= X1[j] + X2[j] + X3[j]
			
			for j in range(dimension):
				Xnew[j]/=3.0
			
			# fitness calculation of new solution
			fnew = fitness(Xnew)

			# greedy selection
			if fnew < population[i].fitness:
				population[i].loc = Xnew
				population[i].fitness = fnew
				
		# On the basis of fitness values of wolves
		# sort the population in asc order
		population = sorted(population, key = lambda temp: temp.fitness)

		# best 3 solutions will be called as
		# alpha, beta and gaama
		alpha_wolf, beta_wolf, gamma_wolf = copy.copy(population[: 3])
		
		Iter+= 1
	# end-while

	# returning the best solution
	return alpha_wolf.loc
		
#----------------------------


# Driver code for Rast_rigin function

print("\nBegin grey wolf optimization on Rast_rigin function\n")
dimension = 3
fitness = fitness_Rast_rigin


print("Goal is to minimize Rast_rigin's function in " + str(dimension) + " variables")
print("Function has known min = 0.0 at (", end="")
for i in range(dimension-1):
	print("0, ", end="")
	print("0)")

num_particles = 50
max_iter = 100

print("Setting num_particles = " + str(num_particles))
print("Setting max_iter = " + str(max_iter))
print("\nStarting GWO algorithm\n")



best_loc = gwo(fitness, max_iter, num_particles, dimension, -10.0, 10.0)

print("\nGWO completed\n")
print("\nBest solution found:")
print(["%.6f"%best_loc[k] for k in range(dimension)])
err = fitness(best_loc)
print("fitness of best solution = %.6f" % err)

print("\nEnd GWO for Rast_rigin\n")


print()
print()


# Driver code for Sphere function
print("\nBegin grey wolf optimization on sphere function\n")
dimension = 3
fitness = fitness_sphere


print("Goal is to minimize sphere function in " + str(dimension) + " variables")
print("Function has known min = 0.0 at (", end="")
for i in range(dimension-1):
	print("0, ", end="")
	print("0)")

num_particles = 50
max_iter = 100

print("Setting num_particles = " + str(num_particles))
print("Setting max_iter = " + str(max_iter))
print("\nStarting GWO algorithm\n")



best_loc = gwo(fitness, max_iter, num_particles, dimension, -10.0, 10.0)

print("\nGWO completed\n")
print("\nBest solution found:")
print(["%.6f"%best_loc[k] for k in range(dimension)])
err = fitness(best_loc)
print("fitness of best solution = %.6f" % err)

print("\nEnd GWO for sphere\n")
