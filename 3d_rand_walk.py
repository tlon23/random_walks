import random


def random_walk(n):
	"""Return coordinates after 'n' block random walk."""
	x,y,z = 0,0,0
	for i in range(n):
		(dx, dy, dz) = random.choice([
			(0,0,1), (0,0,-1), 
			(1,0,0), (-1,0,0),
			(0,1,0), (0,-1,0)])
		x += dx
		y += dy
		z += dz 
	return (x,y,z)


number_of_walks = 20000

for walk_length in range(1,50):
	no_transport = 0  #Number of walks 10 or fewer blocks from home
	for i in range(number_of_walks):
		(x,y,z) = random_walk(walk_length)
		distance = abs(x) + abs(y) + abs(z)
		if distance <= 5:
			no_transport += 1
	no_transport_percentage = float(no_transport) / number_of_walks
	print("Walk size = ", walk_length, " percent of no transport = ", 
		100 * no_transport_percentage)
	