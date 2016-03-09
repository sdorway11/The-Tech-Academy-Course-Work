import urllib2, progressbar, csv, os
from bs4 import BeautifulSoup

# Open Webpage
webpage = urllib2.urlopen("http://www.inadaybooks.com/justiceleague")

def extractMData(webpage):
    soup = BeautifulSoup(webpage, "html.parser")
    #print soup
    #print soup.title.get_text()
    #Find all the divs with the class block
    divBlock = soup.findAll("div", {"class": "block"})
    #print divBlock[3]
    info = divBlock[3]

    #Extract into_left and into_right divs
    getLeft = info.findAll("div",{"class":"info_left"})
    getRight = info.findAll("div", {"class":"info_right"})
    #print getLeft
    #print getRight

    # Create arrays for exporting data to csv file
    getLeftArr = []
    getRightArr = []
    
    for i in range(0,len(getLeft)):
        textLeft = getLeft[i].get_text()
        textRight = getRight[i].get_text()
        getLeftArr.append(textLeft)
        getRightArr.append(textRight)
        #print textLeft + ": " + textRight
    #print ""

    #return the arrays so they can be exported to the csv file
    return [getLeftArr, getRightArr]

#print BeautifulSoup(webpage)

# Convert to BeautifulSoup
soup = BeautifulSoup(webpage, "html.parser")
#print soup.title
#print soup.body

# get contents of website
divContainer = soup.find("div",{"id": "container"})
#print divContainer

# get the div class block
divBlock = divContainer.findAll("div", {"class": "block"})
#print divBlock[3]

# get all with div class separator
divSep = divBlock[3].findAll("div", {"class": "separator"})
#print divSep[3]

# get the members
members = divSep[3].findAll("a")

#Creating the progress bar
nMembers = len(members)
#print nMembers
bar = progressbar.ProgressBar(nMembers).start()

    
count = 0

# The path to the script
currentPath = os.path.dirname(os.path.abspath("__file__"))

# Make the Spreadsheet path
outputCsv = currentPath + "\members.csv"

#Open the file
csvFile = open(outputCsv, "wb")

# Create writer object
writer = csv.writer(csvFile, delimiter= ",")

    # Loop through members
for member in members:
    # strip <a> tags
    #print member.get_text()
    #print member.get("title")
    href = member.get("href")
    
    # create URL to open
    url = "http://inadaybooks.com/justiceleague/" + href
    
    # Open url
    mPage = urllib2.urlopen(url)
    #print extractMData(mPage)

    #Write data to csv file
    data = extractMData(mPage)

    if count == 0:
        # Write heading to csv file
        writer.writerow(data[0])
        #print data[0]

    writer.writerow(data[1])
    #print data[0]
    #print data[1]
    
    # Increment count
    count+=1

    # Update progress bar
    bar.update(count)
