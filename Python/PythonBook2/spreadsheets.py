import os, csv

# The path to the script

currentPath = os.path.dirname(os.path.abspath("__file__"))
print currentPath

#Make the Spreadsheet Path

outputCsv = currentPath + '\spreadsheet.csv'
print outputCsv

# Open the file
csvFile = open(outputCsv, "wb")

# Writing to the File(one way)
# csvFile.write("Testing")

# Writing to the file (Better way)
writer = csv.writer(csvFile, delimiter = ",")

# Data to go in csv file
row_1 = [1, "Row 1", 123]
row_2 = [2, "Row 2", 456]
row_3 = [3, "Row 3", 789]

# write the data to the file (slow way)
#writer.writerow(row_1)
#writer.writerow(row_2)
#writer.writerow(row_3)

# all rows
rows = [row_1, row_2, row_3]

# Loop rows and write eache
for row in rows:
    writer.writerow(row)

csvFile.close()
