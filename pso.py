import sys
import math
import random as r
import numpy as np

# will need to think about how I design the toplogy
# maybe just as a list of the particles closest to each other?

# Template of how to supply command line arguments
# sys.arv = ['pso.py', function_type, dimension]
# note that function type is 'rosenbrock' or 'griewanks' and dimension is an optional positive integer argument

w = 0.7298 # can linearly decrease this with generations later if I want
c1 = 1.49681 # acceleration coefficient
c2 = 1.49681 # acceleration coefficient

NUM_GENS = 100
NUM_PARTICLES = 100
DIMENSION = 20

# line that allows user to supply dimension as a command line argument
if len(sys.argv) > 2 and type(sys.argv[2]) == 'int' and sys.argv[2] > 0: # needs to be tested
	DIMENSION = sys.argv[2]

# we are looking to minimise the function so we set our starting values to ∞
gbest = float('inf')
gbest_position = np.zeros(DIMENSION)

def rosenbrock_function(position):
	output = 0

	for i in range(DIMENSION-1):
		output += (100 * ((position[i]**2) - (position[i+1]**2)) + ((position[i] - 1)**2))

	return output

def protected_div(a, b):
	if b != 0:
		return a/b
	return float()

def griewanks_function(position):
	A = 0
	B = 1

	for i in range(DIMENSION):
		A += ((position[i])**2/4000)

	for i in range(DIMENSION):
		B *= math.cos(protected_div((position[i]), math.sqrt(i)))+1

	return A - B

if len(sys.argv) > 1:
	if sys.argv[1] == 'rosenbrock':
		function = rosenbrock_function
	elif sys.argv[1] == 'griewanks':
		function = griewanks_function
	else:
		print("Function type specified not recognised. Default of Rosenbrock's function chosen.")
		function = rosenbrock_function
else:
	print("Function type not supplied as command line argument. Default of Rosenbrock's function chosen.")
	function = rosenbrock_function	

class Particle:
	# maybe make the initial positions and velocitys an input to the class
	# or generate them randomly as the particle is created?

	# we are looking to minimise the function so we set our starting values to ∞
	pbest = float('inf')
	pbest_position = np.zeros(DIMENSION)
	
	current_velocity = np.ones(DIMENSION)
	current_position = np.ones(DIMENSION)

	def calculate_new_velocity(self):
		return self.current_velocity + (c1 * r.random() * (np.subtract(self.pbest_position, self.current_position))) + (c2 * r.random() * np.subtract(gbest_position, self.current_position))

	def update_position(self, updated_velocity):
		self.current_position = self.current_position + updated_velocity

		output = function(self.current_position)

		# check how good the new position is relative to personal best
		if output < self.pbest:
			self.pbest_position = self.current_position
			self.pbest = output
		
		# check how good the new position is relative to global best
		global gbest, gbest_position
		if output < gbest:
			gbest_position = self.current_position
			gbest = output

	def update(self):
		updated_velocity = self.calculate_new_velocity()
		self.current_velocity = updated_velocity
		self.update_position(updated_velocity)

if __name__ == '__main__':
	particle_list = list()

	for i in range(NUM_PARTICLES):
		particle_list.append(Particle()) # make the velocity and position here

	for gen in range(NUM_GENS):
		for particle in particle_list:
			particle.update()

	print(gbest)
	print(gbest_position)