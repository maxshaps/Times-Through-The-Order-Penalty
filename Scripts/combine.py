from sys import argv
from os.path import exists


"""
Combines a bunch of CSV files into one big one
Ignores any line breaks at the beginning of the files
Input: firstFileName: Name of the first file in the list of files to combine.
					  Must be of the format <blah>_<number>
       outputFileName: Name of the output file that will be saved.
       numberScripts: Number of CSV files to be concatenated.
"""


script, firstFileName, outputFileName, numberScripts = argv

baseFileName = firstFileName.partition('_')[0] + '_'
firstFileNumber = int(firstFileName.partition('_')[2].partition('.')[0])
numberScripts = int(numberScripts)


with open(outputFileName, 'w') as out_file:

    for line in open(firstFileName): #includes file header of first file
		if line != '\n':
			out_file.write(line)

    for index in range(firstFileNumber+1,firstFileNumber+numberScripts):
        currentFileName = baseFileName + str(index) + '.csv'
        with open(currentFileName) as current_file:
			out_file.write('\n')			#start writing on new line
			for line in current_file:
				if line == '\n':
					current_file.next()
				elif line[0:3] == 'Yr#':	#skips file headers of appended files
					current_file.next()
				else:
					out_file.write(line)
