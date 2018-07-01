from sys import argv
from os.path import exists
import os
import string


"""
Renames a bunch of CSV files into a "<year> <blah>_<number> format.
Input: firstFileName: Name of the first file in the list of files to rename.
					  Must be of the format <blah>_table_<year>_<number>.
       outputFileName: Name of the <blah> in the output that will be saved.
"""


script, firstFileName, outputFileName = argv

fileYear = firstFileName.partition('table_')[2].partition('_')[0]
baseFileName = fileYear + ' ' + outputFileName + '_'

fileDirectory = sorted(os.listdir(os.path.dirname(firstFileName)), key=lambda x: int(x.partition(fileYear + '_')[2].partition('.')[0]))
baseName = os.path.dirname(firstFileName)

for index,filename in enumerate(fileDirectory):
    if os.path.basename(filename).split(".")[-1] == 'csv':
    	os.rename(baseName + '\\' + filename, baseName + '\\' + baseFileName + str(index+1) + '.csv')
