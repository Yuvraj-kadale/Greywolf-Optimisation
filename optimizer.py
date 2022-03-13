from GWO import *
import random
import math    
import copy    
import sys     
 
 
print("\nBegin grey wolf optimization on rastrigin function\n")
dim = 3
fitness = fitness_rastrigin
 
 
print("Goal is to minimize Rastrigin's function in " + str(dim) + " variables")
print("Function has known min = 0.0 at (", end="")
for i in range(dim-1):
  print("0, ", end="")
print("0)")
 
num_particles = 50
max_iter = 100
 
print("Setting num_particles = " + str(num_particles))
print("Setting max_iter    = " + str(max_iter))
print("\nStarting GWO algorithm\n")
 
 
 
best_position = gwo(fitness, max_iter, num_particles, dim, -10.0, 10.0)
 
print("\nGWO completed\n")
print("\nBest solution found:")
print(["%.6f"%best_position[k] for k in range(dim)])
err = fitness(best_position)
print("fitness of best solution = %.6f" % err)
 
print("\nEnd GWO for rastrigin\n")
 
 
print()
print()
 
 
# Driver code for Sphere function
print("\nBegin grey wolf optimization on sphere function\n")
dim = 3
fitness = fitness_sphere
 
 
print("Goal is to minimize sphere function in " + str(dim) + " variables")
print("Function has known min = 0.0 at (", end="")
for i in range(dim-1):
  print("0, ", end="")
print("0)")
 
num_particles = 50
max_iter = 100
 
print("Setting num_particles = " + str(num_particles))
print("Setting max_iter    = " + str(max_iter))
print("\nStarting GWO algorithm\n")
 
 
 
best_position = gwo(fitness, max_iter, num_particles, dim, -10.0, 10.0)
 
print("\nGWO completed\n")
print("\nBest solution found:")
print(["%.6f"%best_position[k] for k in range(dim)])
err = fitness(best_position)
print("fitness of best solution = %.6f" % err)
 
print("\nEnd GWO for sphere\n")