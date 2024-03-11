#!/usr/bin/env python3

import argparse
import numpy as np
import random
import sys
from utils import preproc


parser = argparse.ArgumentParser(description = 'train a logistic model on data')
parser.add_argument('-e', '--epochs', type = int, default = 3000)
parser.add_argument('-l', '--learning-rate', type = float, default = 0.01)
opti = parser.add_mutually_exclusive_group()
opti.add_argument('-s', '--stochastic', action = 'store_true')
opti.add_argument('-mb', '--mini-batch', type = int, default = 10)
opti.add_argument('-b', '--batch', action = 'store_true', default = True)

args = parser.parse_args()

try:
	file = open("thetas.csv", 'w')
except PermissionError as ve:
	print("Theta file not writable")
	exit(1)

train_grades, train_houses, predict = preproc()

epochs = args.epochs
learning_rate = args.learning_rate
if args.batch:
	batch_size = train_houses.size
elif args.stochastic:
	batch_size = 1
else:
	batch_size = args.mini_batch

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
		batch_grade = train_grades[n]
		batch_grade = np.insert(batch_grade, 0, 1, 1)
		batch_house = houses_onevall[n]
		data_theta = np.dot(batch_grade, thetas)
		thetas -= learning_rate / data_theta.size * np.dot(data_theta - batch_house, batch_grade)
	
	file.write(house)
	for theta in thetas:
		file.write(',' + str(theta))
	file.write('\n')



