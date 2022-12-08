#!/usr/bin/env python3

import re

def create_stacks_of_crates(stacks):
	stacks_of_crates = [ [] for _ in range(len(stacks[0])) ]
	for stack in reversed(stacks):
		for index, crate in enumerate(stack):
			if crate != ' ':
				stacks_of_crates[index].append(crate)
	return stacks_of_crates

def rearrange_stacks_of_crates(stacks_of_crates, procedures, reverse):
	for procedure in procedures:
		size = int(procedure[0])
		src = int(procedure[1]) - 1
		dst = int(procedure[2]) - 1
		payload = stacks_of_crates[src][size * -1:]
		if reverse:
			payload.reverse()
		stacks_of_crates[dst] += payload
		stacks_of_crates[src] = stacks_of_crates[src][:size * -1]
	return stacks_of_crates

if __name__ == '__main__':
	with open('input.txt') as file:
		stacks = []
		procedures = []
		for line in file.readlines():
			stripped_line = line.rstrip('\n')
			if re.search('^\s*\[', stripped_line):
				stacks.append(list(stripped_line)[1::4])
			elif stripped_line.startswith('m'):
				procedures.append(stripped_line.split(' ')[1::2])

	for index, reverse in enumerate([True, False]):
		stacks_of_crates = create_stacks_of_crates(stacks)
		rearranged_stacks_of_crates = rearrange_stacks_of_crates(stacks_of_crates, procedures, reverse)

		top_of_stacks = ''.join([ crates[-1] for crates in rearranged_stacks_of_crates ])
		print('Answer {}: {}'.format(index + 1, top_of_stacks))
