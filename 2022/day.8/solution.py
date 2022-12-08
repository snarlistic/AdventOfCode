#!/usr/bin/env python3

def visible(row_trees, column_trees, tree, row, column, row_max, column_max):
	if row == 0 or column == 0 or row == row_max or column == column_max:
		return 1
	row_visible = tree > max(row_trees[:column]) or tree > max(row_trees[column + 1:])
	column_visible = tree > max(column_trees[:row]) or tree > max(column_trees[row + 1:])
	return 1 if row_visible or column_visible else 0

def scenic_score(tree, trees):
	scenic_score = 0
	for neighbor in trees:
		scenic_score += 1
		if tree <= neighbor:
			break
	return scenic_score

def max_scenic_score(row_trees, column_trees, tree, row, column, row_max, column_max):
	if row == 0 or column == 0 or row == row_max or column == column_max:
		return 0
	up_trees = column_trees[:row]
	up_trees.reverse()
	up_view = scenic_score(tree, up_trees)
	left_trees = row_trees[:column]
	left_trees.reverse()
	left_view = scenic_score(tree, left_trees)
	down_view = scenic_score(tree, column_trees[row + 1:])
	right_view = scenic_score(tree, row_trees[column + 1:])
	return up_view * left_view * down_view * right_view

def convert(line):
	return [ int(number) for number in line ]

if __name__ == '__main__':
	with open('input.txt') as file:
		forest = [ convert(line.rstrip('\n')) for line in file.readlines() ]
	row_max = len(forest) - 1
	column_max = len(forest[0]) - 1
	count = 0
	max_score = 0
	for row, row_of_trees in enumerate(forest):
		row_trees = row_of_trees
		for column, tree in enumerate(row_of_trees):
			column_trees = [ columns[column] for columns in forest ]
			count += visible(row_trees, column_trees, tree, row, column, row_max, column_max)
			max_score = max(max_score, max_scenic_score(row_trees, column_trees, tree, row, column, row_max, column_max))
	print('Answer 1: {}'.format(count))
	print('Answer 2: {}'.format(max_score))
