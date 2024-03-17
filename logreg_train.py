#!/usr/bin/env python3

import argparse
import numpy as np
from utils import preproc, sigmoid
import math
import matplotlib.pyplot as plt

def batch_init(size):
	set = list(range(size))
	np.random.shuffle(set)
	return set

def	get_batch(set, size):
	size = min(size, len(set))
	batch = set[:size]
	del set[:size]
	return batch


parser = argparse.ArgumentParser(description = 'train a logistic model on data')
parser.add_argument('-e', '--epochs', type = int, default = 50)
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

size = train_houses.size

train_size = math.floor(size * 0.9)
sample = list(range(size))
np.random.shuffle(sample)

sample_train = sample[:train_size]
sample_test = sample[train_size:]

data_train = train_grades[sample_train]
data_test = train_grades[sample_test]
house_train = train_houses[sample_train]
house_test = train_houses[sample_test]

test_acc = []

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

data_train = np.insert(data_train, 0, 1, 1)
data_test = np.insert(data_test, 0, 1, 1)

values = np.empty((house_test.size, epochs, 4))
h = 0
for house in houses:

	houses_onevall = np.where(house_train == house, 1, 0)
	thetas = np.zeros(data_train[0].shape)

	for i in range (0, epochs):
		batch_set = batch_init(house_train.size)
		while (batch_set):
			n = get_batch(batch_set, batch_size)
			batch_grade = data_train[n]
			batch_house = houses_onevall[n]
			data_theta = np.dot(batch_grade, thetas)
			thetas -= learning_rate / data_theta.size * np.dot(data_theta - batch_house, batch_grade)
		for j in range(house_test.size):
			values[j][i][h] = sigmoid(np.dot(data_test[j], thetas.T))

	file.write(house)
	for theta in thetas:
		file.write(',' + str(theta))
	file.write('\n')
	h += 1

acc = []
for i in range(epochs):
	acc_epochs = 0
	for j in range(house_test.size):
		acc_epochs += houses[np.argmax(values[j][i])] == house_test[j]
	acc.append(acc_epochs / house_test.size) 

print(acc[epochs - 1])
plt.plot(range(epochs), acc)
plt.show()
