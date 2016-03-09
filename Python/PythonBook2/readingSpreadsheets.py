import os, csv

# The path to the script

currentPath = os.path.dirname(os.path.abspath("__file__"))


#Make the Spreadsheet Path

inputCsv = currentPath + '\spreadsheet.csv'

# Open File in read mode
csvFile = open(inputCsv, "rb")

# Create Reader Object
reader = csv.reader(csvFile, delimiter = ",")

# Add data to an array
readerData = []

# Print the data out in file
for row in reader:
    print row
    readerData.append(row)
    
print readerData
