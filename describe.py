#!/usr/bin/env python3

import sys
import csv
import numpy as np
import math

def open_file(file):
	file_array = []
	try:
		with open(file, 'r') as f:
			reader = csv.reader(f)
			for row in reader:
				file_array.append(row)
	except (FileNotFoundError, PermissionError) as ve:
		print("File not found or invalid permissions")
		sys.exit(1)
	data_array = np.array(file_array)
	return np.transpose(data_array)

def sort(array):
	size = array.size
	for i in range (0, size - 1):
		for j in range (0, size - 1 - i):
			if (array[j] > array[j + 1]):
				array[j], array[j + 1] = array[j + 1], array[j]

def count_non_zero(array):
	count = 0
	for elem in array:
		if elem != 0:
			count += 1
	return count

def del_zeros(array):
	for i in range (0, array.size):
		if array[i] == 0:
			np.delete(array, i)

def get_percentile(data, perc):
	size = data.size
	if perc < 0:
		return data[0]
	if perc >= 100:
		return data[size - 1]
	rank = perc / 100 * (size - 1)
	rank_int = math.floor(rank)
	rank_frac = rank - rank_int
	return data[rank_int] + rank_frac * (data[rank_int + 1] - data[rank_int])

try:
	data_str = open_file(sys.argv[1])
except IndexError:
	print("Usage: describe.py filename")
	sys.exit(1)

data_str[data_str==''] = '0'

data_float = np.array(data_str[6:, 1:], float)

stats = np.empty((13, 9), float)

index = 0
for row in data_float:

	del_zeros(row)
	sort(row)
	count = count_non_zero(row)
	mean = sum(row) / count
	var = sum((row - mean) ** 2) / count
	std_dev = math.sqrt(var)
	min = row[0]
	max = row[count - 1]
	perc_25 = get_percentile(row, 25)
	median = get_percentile(row, 50)
	perc_75 = get_percentile(row, 75)
	stats[index][0] = count
	stats[index][1] = mean
	stats[index][2] = var
	stats[index][3] = std_dev
	stats[index][4] = min
	stats[index][5] = perc_25
	stats[index][6] = median
	stats[index][7] = perc_75
	stats[index][8] = max
	# print(stats[index])
	index += 1

display = []
display.append(" " * 10)
display.append('{:10}'.format("Count"))
display.append('{:10}'.format("Mean"))
display.append('{:10}'.format("Var"))
display.append('{:10}'.format("Std"))
display.append('{:10}'.format("Min"))
display.append('{:10}'.format("25%"))
display.append('{:10}'.format("Median"))
display.append('{:10}'.format("75%"))
display.append('{:10}'.format("Max"))

for i in range (0, 13):
	display[0] += " | " +  '{:>13.13}'.format(data_str[6 + i][0])

for i in range (0, 9):
	for j in range (0, 13):
		display[1 + i] +=  " | " +  '{:13.3f}'.format(stats[j][i])

for row in display:
	print(row)
# print('{:10}'.format("count"), '{:15f}'.format(stats[0][0]))
