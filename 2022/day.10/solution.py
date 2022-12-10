#!/usr/bin/env python3

def process_instruction(line, x):
	instruction = line.rstrip('\n').split(' ')
	if instruction[0] == 'addx':
		cycles = [ x, x ]
		x += int(instruction[1])
	elif instruction[0] == 'noop':
		cycles = [ x ]
	return ( x, cycles )


if __name__ == '__main__':
	x = 1
	cycles = []
	with open('input.txt') as file:
		for line in file.readlines():
			( x, burned_cycles) = process_instruction(line, x)
			cycles +=  burned_cycles
	cycles += [ x ]
	strength = 0
	for cycle in [ 20, 60, 100, 140, 180, 220 ]:
		strength += cycle * cycles[cycle - 1]
	print('Answer 1: {}'.format(strength))
