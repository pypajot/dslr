#!/usr/bin/env python3

import numpy as np
from utils import preproc, sigmoid

try:
	file = open("thetas.csv", 'w')
except PermissionError as ve:
	print("Theta file not writable")
	exit(1)

learning_rate = 0.001
epochs = 100000

train_grades, train_houses, predict = preproc()

houses = [
	'Gryffindor',
	'Slytherin',
	'Ravenclaw',
	'Hufflepuff'
]

file.write("House")
for i in range (0, train_grades[0].size):
	file.write(',theta' + str(i))
file.write('\n')

for house in houses:

	houses_onevall = np.where(train_houses == house, 1, 0)
	thetas = np.zeros(train_grades[0].shape)

	for i in range (0, epochs):
		data_theta = np.dot(train_grades, thetas)
		thetas -= learning_rate / train_grades[0].size * np.dot(data_theta - houses_onevall, train_grades)
	
	file.write(house)
	for theta in thetas:
		file.write(',' + str(theta))
	file.write('\n')



