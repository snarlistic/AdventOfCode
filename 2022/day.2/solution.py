#!/usr/bin/env python3

if __name__ == '__main__':
	# A,X = rock, B,Y = paper, C,Z = scissors.
	scores_1 = {
		'A X': 1 + 3,
		'A Y': 2 + 6,
		'A Z': 3 + 0,
		'B X': 1 + 0,
		'B Y': 2 + 3,
		'B Z': 3 + 6,
		'C X': 1 + 6,
		'C Y': 2 + 0,
		'C Z': 3 + 3
	}
	# A = rock, B = paper, C = scissors, X = lose, Y = draw, Z = win.
	scores_2 = {
		'A X': 3 + 0,
		'A Y': 1 + 3,
		'A Z': 2 + 6,
		'B X': 1 + 0,
		'B Y': 2 + 3,
		'B Z': 3 + 6,
		'C X': 2 + 0,
		'C Y': 3 + 3,
		'C Z': 1 + 6
	}
	with open('input.txt') as file:
		total_1 = 0
		total_2 = 0
		for line in file.readlines():
			result = line.strip('\n')
			total_1 += scores_1[result]
			total_2 += scores_2[result]
	print('Answer 1: {}'.format(total_1))
	print('Answer 2: {}'.format(total_2))
