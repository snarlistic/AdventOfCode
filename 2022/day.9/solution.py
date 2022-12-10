#!/usr/bin/env python3

def move(H, T, H_current):
	x = 0
	y = 1
	x_movement = abs(H[x] - T[x])
	y_movement = abs(H[y] - T[y])
	if x_movement == 2 or y_movement ==2:
		T = H_current
	return T

def series_of_moves(direction, steps, H, T):
	x = 0
	y = 1
	visited = []
	for step in range(steps):
		H_current = H
		if direction == 'U':
			H = ( H[x], H[y] - 1 )
		elif direction == 'L':
			H = ( H[x] - 1, H[y] )
		elif direction == 'D':
			H = ( H[x], H[y] + 1 )
		elif direction == 'R':
			H = ( H[x] + 1, H[y] )
		T = move(H, T, H_current)
		visited += [ T ]
	return ( visited, H, T )

if __name__ == '__main__':
	with open('input.txt') as file:
		moves = [ tuple(line.rstrip('\n').split(' ')) for line in file.readlines() ]
	H = T = ( 0, 0 )
	visited = [ H, T ]
	for (direction, steps) in moves:
		( visited_move, H, T ) = series_of_moves(direction, int(steps), H, T)
		visited += visited_move
	print('Answer 1: {}'.format(len(set(visited))))
	#print('Answer 2: {}'.format(max_score))
