import csv
from math import fsum
from statistics import median

file_name = "Final Data.csv"
with open(file_name, 'r') as f:
	reader = csv.reader(f)
	file = (list(reader))

columns = file[0]
data = file[1:]

# creates list of data that should be analyzed
to_analyze = []
for row in data:
	if row[2] == '1':
		to_analyze.append(row)

def data_median(column, to_analyze, median_dict):
	median_list = []
	for row in to_analyze:
		if row[columns.index(column)] != 'Not Available':
			median_list.append(float(row[columns.index(column)]))
	median_dict[column + ' median'] = median(median_list)
	return median_dict

def data_sum(column, to_analyze, sum_dict):
	sum_list = []
	for row in to_analyze:
		if row[columns.index(column)] != 'Not Available':
			sum_list.append(float(row[columns.index(column)]))
	sum_dict[column + ' total'] = fsum(sum_list)
	return sum_dict