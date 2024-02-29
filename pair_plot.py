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


# gryffindor = np.delete(gryffindor, np.where(gryffindor == 0))

gryffindor[gryffindor == 0] = None
hufflepuff[hufflepuff == 0] = None
ravenclaw[ravenclaw == 0] = None
slytherin[slytherin == 0] = None

fig, axs = plt.subplots(13, 13, figsize=(20, 20))

for i in range(13):
	for j in range(13):
		if i == j:
			axs[i, j].hist(gryffindor[i], bins=10, alpha=0.5, color='red')
			axs[i, j].hist(hufflepuff[i], bins=10, alpha=0.5, color='yellow')
			axs[i, j].hist(ravenclaw[i], bins=10, alpha=0.5, color='blue')
			axs[i, j].hist(slytherin[i], bins=10, alpha=0.5, color='green')
		else:
			axs[i, j].scatter(gryffindor[i], gryffindor[j], color='red', s = 0.1)
			axs[i, j].scatter(hufflepuff[i], hufflepuff[j], color='yellow', s = 0.1)
			axs[i, j].scatter(ravenclaw[i], ravenclaw[j], color='blue', s = 0.1)
			axs[i, j].scatter(slytherin[i], slytherin[j], color='green', s = 0.1)
		axs[i][j].set_xticklabels([])
		axs[i][j].set_yticklabels([])

plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05, wspace=0.1, hspace=0.1)
plt.show()