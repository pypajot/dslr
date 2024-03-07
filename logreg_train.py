#!/usr/bin/env python3

import numpy as np
import random
import sys
from utils import preproc

try:
	file = open("thetas.csv", 'w')
except PermissionError as ve:
	print("Theta file not writable")
	exit(1)

train_grades, train_houses, predict = preproc()

learning_rate = 0.01
epochs = 1000
batch_size = train_houses.size
# print(train_houses.size)

if len(sys.argv) > 1:
	match sys.argv[1]:
		case '--stochastic':
			batch_size = 1
		case '--minibatch':
			batch_size = 10

houses = [
	'Gryffindor',
	'Slytherin',
	'Ravenclaw',
	'Hufflepuff'
]

file.write("House")
for i in range (0, train_grades[0].size + 1):
	file.write(',theta' + str(i))
file.write('\n')


for house in houses:

	houses_onevall = np.where(train_houses == house, 1, 0)
	thetas = np.zeros(train_grades[0].shape)
	thetas = np.insert(thetas, 0, 0)

	for i in range (0, epochs):
		n = random.sample(range(0, train_houses.size), batch_size)
		# print(n)
		batch_grade = train_grades[n]
		# print(batch_grade)
		batch_grade = np.insert(batch_grade, 0, 1, 1)
		# print(batch_grade)
		batch_house = houses_onevall[n]
		data_theta = np.dot(batch_grade, thetas)
		thetas -= learning_rate / data_theta.size * np.dot(data_theta - batch_house, batch_grade)
	
	file.write(house)
	for theta in thetas:
		file.write(',' + str(theta))
	file.write('\n')



