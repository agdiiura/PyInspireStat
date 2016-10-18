#!/usr/bin/env python
'''
pyinspirestat - Get time series from INSPIRE HEP database, the code is largely based on pyinspire.py , originally written by Ian Huston
Author: Andrea Di Iura
'''
import os
import re
import numpy as np

start_year, stop_year = 1930, 2015
years = map(str, range(start_year, stop_year + 1))
query = 'date '
output = []
j = 0
for year in years: 
	#print(year)
	j = j + 1
	print("\nYear = ", year, ". Completed @ {0:.1f}".format(j*100./(stop_year - start_year + 1)), "%")

	command = 'python pyinspire.py -s "find ' + query + year +'"'
	#print(command)
	return_value = os.popen(command).read().rstrip()
	return_value = re.sub('((?<=,)|^)(?=,|$)', '0', return_value)

	print("Number of papers: ", return_value)
	output.append([int(year), int(return_value)])

npoutput = np.array(output)
print("\n")
print(npoutput)


### export data
file_name = query.replace (" ", "_") + 'years.dat'
header_str = query + str(start_year) + ' ---> ' + str(stop_year)
#print(file_name)
np.savetxt(file_name, npoutput, fmt = '%.f', delimiter = '\t', header = header_str)
