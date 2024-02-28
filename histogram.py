#!/usr/bin/env python3

import csv
import sys
import numpy as np
import matplotlib.pyplot as plt

def del_zeros(array):
	for i in range (0, array.size):
		if array[i] == 0:
			np.delete(array, i)

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
	data_str = open_file(sys.argv[1])
except IndexError:
	print("Usage: describe.py filename")
	sys.exit(1)

data_str[data_str=='Gryffindor'] = '1'
data_str[data_str=='Slytherin'] = '2'
data_str[data_str=='Ravenclaw'] = '3'
data_str[data_str=='Hufflepuff'] = '4'
data_str[data_str==''] = '0'

data = np.array(data_str[6:, 1:], float)
print(data[12])
for row in data:
	del_zeros(row)

fig, axs = plt.subplots(4,4)
axs[0][0].hist(data[0], 16)
fig.delaxes(axs[3][1])
fig.delaxes(axs[3][2])
fig.delaxes(axs[3][3])
plt.show()