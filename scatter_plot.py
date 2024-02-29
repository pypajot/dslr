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


plt.scatter(gryffindor[1], gryffindor[3], color='red')
plt.scatter(ravenclaw[1], ravenclaw[3], color='blue')
plt.scatter(hufflepuff[1], hufflepuff[3], color='yellow')
plt.scatter(slytherin[1], slytherin[3], color='green')

plt.show()