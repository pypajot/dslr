#!/usr/bin/env python3

import sys
import csv
import numpy as np

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

try:
	open_file(sys.argv[1])
except IndexError:
	print("Usage: describe.py filename")
	sys.exit(1)

data = open_file(sys.argv[1])
print(data[6])
print(data[18])