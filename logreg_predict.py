#!/usr/bin/env python3

import sys
import csv
import numpy as np
from utils import preproc, sigmoid

try:
	file = open('houses.csv', 'w')
except PermissionError as ve:
	print('Houses.csv has wrong permissions')
	sys.exit(1)

try:
	thetas_file = []
	f = open('thetas.csv', 'r')
	reader = csv.reader(f)
	for row in reader:
		thetas_file.append(row)
except (FileNotFoundError, PermissionError) as ve:
	print("Theta file not found or invalid permissions")
	sys.exit(1)

file.write("Index,Hogwarts House\n")

train, house_train, predict = preproc()
thetas_str = np.array(thetas_file)
houses = thetas_str.T[0, 1:]
thetas = np.array(thetas_str[1:, 1:], float)
index = 0
for row in predict:
	values = sigmoid(np.dot(row, thetas.T))
	file.write(str(index) + ',' + houses[np.where(values == max(values))[0][0]] + '\n')
	index += 1


