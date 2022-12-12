#!/usr/bin/env python3

def move_knot(knot, leader):
	x = 0
	y = 1
	x_movement = leader[x] - knot[x]
	y_movement = leader[y] - knot[y]
	x_movement_real = x_movement / abs(x_movement) if x_movement != 0 else 0
	y_movement_real = y_movement / abs(y_movement) if y_movement != 0 else 0
	if x_movement == 2:
		new_position = ( knot[x] + 1, knot[y] + y_movement_real )
	elif x_movement == -2:
		new_position = ( knot[x] - 1, knot[y] + y_movement_real )
	elif y_movement == 2:
		new_position = ( knot[x] + x_movement_real, knot[y] + 1 )
	elif y_movement == -2:
		new_position = ( knot[x] + x_movement_real, knot[y] - 1 )
	else:
		new_position = knot
	return new_position

def move_rope(rope, knot, direction, head):
	working_knot = rope[knot][-1]
	if head:
		x = 0
		y = 1
		if direction == 'U':
			leader = ( working_knot[x], working_knot[y] - 1 )
		elif direction == 'L':
			leader = ( working_knot[x] - 1, working_knot[y] )
		elif direction == 'D':
			leader = ( working_knot[x], working_knot[y] + 1 )
		elif direction == 'R':
			leader = ( working_knot[x] + 1, working_knot[y] )
		new_position = leader
	else:
		leader = rope[knot + 1][-1]
		new_position = move_knot(working_knot, leader)
	return new_position

def print_maze(direction, steps, rope):
	print('== {} {} =='.format(direction, steps))
	print('')
	maze = []
	for i in range(21):
		maze += [ [ '.' ] * 26 ]
	x = 0
	y = 1
	s = (11, 15)
	for index, name in enumerate(list(reversed(range(1, len(rope)))) + [ 'H' ]):
		maze[s[y] + rope[index][y]][s[x] + rope[index][x]] = str(name)
	for row in maze:
		print(''.join(row))
	print('')

if __name__ == '__main__':
	with open('input.txt') as file:
		moves = [ tuple(line.rstrip('\n').split(' ')) for line in file.readlines() ]
	for answer, knots in enumerate([ 2, 10 ]):
		rope = [ [ (0, 0) ] for _ in range(knots) ]
		#DEBUG: names = list(reversed(range(1, len(rope)))) + [ 'H' ]
		head = len(rope) - 1
		#DEBUG: print_maze('Initial', 'State', [ x[-1] for x in rope ])
		for (direction, steps) in moves:
			for step in range(int(steps)):
				for knot in reversed(range(len(rope))):
					rope[knot] += [ move_rope(rope, knot, direction, knot == head) ]
					#DEBUG: print('move {} from {} to {}'.format(names[knot], rope[knot][-2], rope[knot][-1]))
				#DEBUG: print_maze('STEP:', str(step), [ x[-1] for x in rope ])
			#DEBUG: print_maze(direction, steps, [ x[-1] for x in rope ])
		print('Answer {}: {}'.format(answer + 1, len(set(rope[0]))))
