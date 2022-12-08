#!/usr/bin/env python3

def find_marker(datastream, size):
	for index in range(len(datastream[:-1 * size])):
		marker = set(datastream[index:index + size])
		if len(marker) == size:
			return index + size
	return -1

if __name__ == '__main__':
	with open('input.txt') as file:
		line = file.readline()
		datastream = line.rstrip('\n')
		for index, size in enumerate([ 4, 14 ]):
			print('Answer {}: {}'.format(index + 1, find_marker(datastream, size)))
