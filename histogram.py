#!/usr/bin/env python3

import csv
import sys
import numpy as np
import matplotlib.pyplot as plt

def del_zeros(array):
	array = [i for i in	array if i != 0]
	return array

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
	return file_array

def sort_houses(data):
	gryffindor = []
	hufflepuff = []
	ravenclaw = []
	slytherin = []

	for row in data:
		match row[1]:
			case "Gryffindor":
				gryffindor.append(row)
			case "Hufflepuff":
				hufflepuff.append(row)
			case "Ravenclaw":
				ravenclaw.append(row)
			case "Slytherin":
				slytherin.append(row)

	gryffindor = np.transpose(gryffindor)
	hufflepuff = np.transpose(hufflepuff)
	ravenclaw = np.transpose(ravenclaw)
	slytherin = np.transpose(slytherin)

	return gryffindor, hufflepuff, ravenclaw, slytherin

try:
	data_str = open_file(sys.argv[1])
except IndexError:
	print("Usage: describe.py filename")
	sys.exit(1)

			
gryffindor, hufflepuff, ravenclaw, slytherin = sort_houses(data_str)

gryffindor[gryffindor == ''] = '0'
hufflepuff[hufflepuff == ''] = '0'
ravenclaw[ravenclaw == ''] = '0'
slytherin[slytherin == ''] = '0'

gryffindor = np.array(gryffindor[6:], float)
hufflepuff = np.array(hufflepuff[6:], float)
ravenclaw = np.array(ravenclaw[6:], float)
slytherin = np.array(slytherin[6:], float)

print(gryffindor[0].size)

# gryffindor = np.delete(gryffindor, np.where(gryffindor == 0))

gryffindor[gryffindor == 0] = None
hufflepuff[hufflepuff == 0] = None
ravenclaw[ravenclaw == 0] = None
slytherin[slytherin == 0] = None


fig, axs = plt.subplots(4,4, figsize=(15, 15))

fig.delaxes(axs[3][1])
fig.delaxes(axs[3][2])
fig.delaxes(axs[3][3])

print(data_str[0][6])

for i in range (0, 13):
	axs[i // 4][i % 4].set_title(data_str[0][i + 6])
	axs[i // 4][i % 4].hist(gryffindor[i], 16, alpha = 0.6, fc=(0.8, 0, 0, 0.4))
	axs[i // 4][i % 4].hist(hufflepuff[i], 16, alpha = 0.6, fc=(0.4, 0.4, 0, 0.4))
	axs[i // 4][i % 4].hist(ravenclaw[i], 16, alpha = 0.6, fc=(0, 0, 0.8, 0.4))
	axs[i // 4][i % 4].hist(slytherin[i], 16, alpha = 0.6, fc=(0, 0.8, 0, 0.4))
	axs[i // 4][i % 4].set_xticklabels([])
	axs[i // 4][i % 4].set_yticklabels([])

plt.show()