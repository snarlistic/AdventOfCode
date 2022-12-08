#!/usr/bin/env python3

if __name__ == '__main__':
	with open('input.txt') as file:
		total = 0
		max = []
		for line in file.readlines():
			calories = line.rstrip('\n')
			if len(calories) != 0:
				total += int(calories)
			else:
				max.append(total)
				total = 0
	max.sort()
	answer = max[-1]
	print('Answer 1: {}'.format(answer))
	answer = 0
	for index in range(3):
		answer += max[-1 * (index + 1)]
	print('Answer 2: {}'.format(answer))
