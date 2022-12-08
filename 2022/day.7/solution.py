#!/usr/bin/env python3

import re

def parent_directory(directory):
	directories = directory.split('/')[:-2]
	parent_directory = '/'.join(directories) + '/'
	return parent_directory

if __name__ == '__main__':
	with open('input.txt') as file:
		terminal_output = [ line.rstrip('\n') for line in file.readlines() ]
	filesystem = {}
	cwd = '/'
	for output in terminal_output:
		match = re.match('^\$ cd (.*)$', output)
		if match:
			directory = match.group(1)
			if directory == '..':
				cwd = parent_directory(cwd)
			else:
				cwd += directory + '/' if directory != '/' else ''
				filesystem[cwd] = { 'size': 0, 'total': 0 }
		else:
			match = re.match('^(\d+) (.*)$', output)
			if match:
				size = int(match.group(1))
				filename = match.group(2)
				filesystem[cwd]['size'] += size
	directories = sorted(list(filesystem.keys()), key = len, reverse = True)
	for directory in directories:
		filesystem[directory]['total'] += filesystem[directory]['size']
		parent = parent_directory(directory)
		if parent != directory:
			filesystem[parent]['total'] += filesystem[directory]['total']
	directories_answer_1 = [ filesystem[directory]['total'] for directory in directories if filesystem[directory]['total'] <= 100000 ]
	print('Answer 1: {}'.format(sum(directories_answer_1)))
	size_required = 30000000 - (70000000 - filesystem['/']['total'])
	directories_answer_2 = [ filesystem[directory]['total'] for directory in directories if filesystem[directory]['total'] >= size_required ]
	directories_answer_2.sort()
	print('Answer 2: {}'.format(directories_answer_2[0]))
