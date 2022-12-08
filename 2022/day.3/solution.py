#!/usr/bin/env python3

def convert(item):
	return ord(item) - ord('a') + 1 if item.islower() else ord(item) - ord('A') + 27

def priority(items):
	return [ convert(item) for item in items ]

def intersection1(rucksack):
	rucksack_splitted_size = int(len(rucksack) / 2)
	left_compartment = set(rucksack[rucksack_splitted_size:])
	right_compartment = set(rucksack[:rucksack_splitted_size])
	return priority(left_compartment.intersection(right_compartment))

def intersection2(rucksack1, rucksack2, rucksack3):
	return priority(rucksack1.intersection(rucksack2).intersection(rucksack3))

def answer(index, prioritized_items):
	priorities = [ priority for prioritized_item in prioritized_items for priority in prioritized_item ]
	print('Answer {}: {}'.format(index, sum(priorities)))

if __name__ == '__main__':
	with open('input.txt') as file:
		items = [ line.rstrip('\n') for line in file.readlines() ]
	prioritized_items = [ intersection1(item) for item in items ]
	answer('1', prioritized_items)
	rucksacks = [ items[index:index + 3] for index in range(0, len(items), 3) ]
	prioritized_items = [ intersection2(set(rucksack[0]), set(rucksack[1]), set(rucksack[2])) for rucksack in rucksacks ]
	answer('2', prioritized_items)
