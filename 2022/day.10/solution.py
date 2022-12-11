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
	crt = []
	crt_index = 0
	crt_width = 40
	with open('input.txt') as file:
		for line in file.readlines():
			( x_new, burned_cycles) = process_instruction(line, x)
			cycles +=  burned_cycles
			for burned_cycle in burned_cycles:
				crt += [ '#' if crt_index % crt_width in range(x - 1, x + 2) else '.' ]
				crt_index += 1
			x = x_new
	cycles += [ x ]
	strength = 0
	for cycle in [ 20, 60, 100, 140, 180, 220 ]:
		strength += cycle * cycles[cycle - 1]
	print('Answer 1: {}'.format(strength))
	print('Answer 2:')
	rows = range(len(crt))[0::crt_width]
	for row in rows:
		print('  {}'.format(''.join(crt[row:row + crt_width])))
