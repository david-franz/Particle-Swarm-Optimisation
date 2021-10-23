import random as r

# need to investigate to find best way of storing vectors- numpy fastest?

class Particle:
	# maybe make the initial positions and velocitys an input to the class

	# we are looking to minimise the function so we set our starting values to ∞
	pbest = float('inf')
	gbest = float('inf') # maybe I should store this outside of the class (global variable)

	pbest_position = (0,0,0)
	gbest_position = (0,0,0) # maybe I should store this outside of the class (global variable)
	
	w = 0.7298
	c1 = 1.49681 # acceleration coefficient
	c2 = 1.49681 # acceleration coefficient
	
	current_velocity = 0 # should be a vector
	current_position = (0,0,0) # need this to be D dimensional

	def calculate_new_velocity():
		r1 = r.random()
		r2 = r.random()

		return current_velocity + (c1 * r1 * (pbest_position - current_position)) + (c2 * r2 * (gbest_position - current_position))

	def update_velocity():
		pass

	def update_position():
		pass

	def update():
		updated_velocity = self.calculate_new_velocity()

		pass

if __name__ == 'main':
	# choose number of particles
	# choose number of generations

	particle_list = list()

	for i in range(NUM_PARTICLES):
		particle_list.append(Particle()) # make the velocity and position here

	for gen in range(NUM_GENS):
		for particle in particle_list:
			particle.update()

	# print(gbest)

