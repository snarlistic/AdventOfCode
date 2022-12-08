#!/usr/bin/env python3

def section_sets(line):
	sections = line.rstrip('\n').split(',')
	section_sets = [ set(range(int(section.split('-')[0]), int(section.split('-')[1]) + 1)) for section in sections ]
	return section_sets

if __name__ == '__main__':
	with open('input.txt') as file:
		sections = [ section_sets(line) for line in file.readlines() ]
	overlapping_sections = [ section for section in sections if len(section[0] - section[1]) == 0 or len(section[1] - section[0]) == 0 ]
	print('Answer 1: {}'.format(len(overlapping_sections)))
	overlapping_sections = [ section for section in sections if not (len(section[0] - section[1]) == len(section[0]) or len(section[1] - section[0]) == len(section[1])) ]
	print('Answer 2: {}'.format(len(overlapping_sections)))
