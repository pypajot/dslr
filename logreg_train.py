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

def	normalize_data(data):
	for row in data:
		# print(abs(max(row, key=abs)))
		row /= abs(max(row, key=abs))

try:
	data_str = open_file(sys.argv[1])
except IndexError:
	print("Usage: describe.py filename")
	sys.exit(1)

data_str[data_str == ''] = '0'

data_float = np.array(data_str[6:, 1:], float)

# data_float[data_float == 0] = None

data_students = np.transpose(data_float)
normalize_data(data_float)
data_houses = data_str[1, 1:]

# print(data_students[0])
# print(data_houses)

# print(data_float)


learning_rate = 0.001
epochs = 100000

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

houses_onevall = np.where(data_houses == 'Hufflepuff', 1, 0)
print(sum(houses_onevall))
thetas = np.zeros(data_students[0].shape)
# print(thetas)
for i in range (0, epochs):
	data_theta = data_students.dot(thetas)
	# print(data_theta)
	# print(data_houses)
	# print(houses_onevall)
	thetas -= learning_rate / data_students[0].size * np.dot(data_theta - houses_onevall, data_students)

# print(thetas)
score = 0
result = sigmoid(np.dot(data_students, thetas))
for i in result:
	if i > 0.60:
		score += 1


print(score)