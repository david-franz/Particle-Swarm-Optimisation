import sys

import random as r
import numpy as np

# will need to think about how I design the toplogy
# maybe just as a list of the particles closest to each other?

# Template of how to supply command line arguments
# sys.arv = ['pso.py', function_type, dimension]
# note that function type is 'rosenbrock' or 'griewanks' and dimension is an optional integer argument

NUM_GENS = 100
NUM_PARTICLES = 100
DIMENSION = 20
if len(sys.argv) > 2 && type(sys.argv[2]) == 'int' && sys.argv[2] > 0: # line that allows user to supply dimension as a command line argument
	DIMENSION = sys.argv[2]

# we are looking to minimise the function so we set our starting values to ∞
gbest = float('inf')
gbest_position = np.zeros(DIMENSION)

def rosenbrock_function(position):
	output = 0

	for i in range(DIMENSION-1):
		output += (100 * ((position[i]**2) - (position[i+1]**2)) + ((position[i] - 1)**2))

	return output

class Particle:
	# maybe make the initial positions and velocitys an input to the class
	# or generate them randomly as the particle is created?

	# we are looking to minimise the function so we set our starting values to ∞
	pbest = float('inf')
	pbest_position = np.zeros(DIMENSION)
	
	w = 0.7298 # can linearly decrease this with generations later if I want
	c1 = 1.49681 # acceleration coefficient
	c2 = 1.49681 # acceleration coefficient
	
	current_velocity = np.zeros(DIMENSION)
	current_position = np.zeros(DIMENSION)

	def calculate_new_velocity():
		return current_velocity + (c1 * r1 = r.random() * (pbest_position - current_position)) + (c2 * r2 = r.random() * (gbest_position - current_position))

	def update_position(updated_velocity):
		current_position = current_position + updated_velocity

		# check how good the new position is relative to personal best
		if function(current_position) > pbest:
			pbest_position = current_position
		
		# check how good the new position is relative to global best
		if function(current_position) > gbest:
			gbest_position = current_position

	def update():
		updated_velocity = self.calculate_new_velocity()
		current_velocity = updated_velocity
		update_position(updated_velocity)

if __name__ == 'main':
	# choose number of particles
	# choose number of generations

	particle_list = list()

	for i in range(NUM_PARTICLES):
		particle_list.append(Particle()) # make the velocity and position here

	for gen in range(NUM_GENS):
		for particle in particle_list:
			particle.update()

	print(gbest)