import sys
import csv
import numpy as np

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

def open_file(file):
	file_str = []
	try:
		with open(file, 'r') as f:
			reader = csv.reader(f)
			for row in reader:
				file_str.append(row)
	except (FileNotFoundError, PermissionError) as ve:
		print("File not found or invalid permissions")
		sys.exit(1)
	data_str = np.transpose(np.array(file_str))
	data_str[data_str == ''] = '0'
	data_float = np.array(data_str[6:, 1:], float)
	houses = data_str[1, 1:]
	return data_float, houses

def	normalize(train, predict):
	for i in range (0, train.T[0].size):
		max_train = abs(max(train[i], key=abs))
		max_predict = abs(max(predict[i], key=abs))
		max_abs = max(max_train, max_predict)
		train[i] /= max_abs
		predict[i] /= max_abs
	

def preproc():
	data_train, houses = open_file('dataset_train.csv')
	data_predict, empty = open_file('dataset_test.csv')
	normalize(data_train, data_predict)
	return np.transpose(data_train), houses, np.transpose(data_predict)
