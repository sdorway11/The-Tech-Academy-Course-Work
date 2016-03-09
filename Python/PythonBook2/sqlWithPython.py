import sqlite3

# connect to database
conn = sqlite3.connect('simpsons.db')

# Drop the table if it exists
conn.execute("DROP TABLE IF EXISTS SIMPSON_INFO;")

# Create Simpsons info table
conn.execute("CREATE TABLE SIMPSON_INFO ( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    NAME TEXT, \
    GENDER TEXT, \
    AGE INT, \
    OCCUPATION TEXT \
    );")

# Add Bart to the table
conn.execute("INSERT INTO SIMPSON_INFO \
    (NAME, GENDER, AGE, OCCUPATION) VALUES \
    ('Bart Simpson', 'Male', 10, 'Student')");

# Add Homer to the table
conn.execute("INSERT INTO SIMPSON_INFO \
    (NAME, GENDER, AGE, OCCUPATION) VALUES \
    ('Homer Simpson', 'Male', 40, 'Nuclear Plant')");

# Add another Homer to the table to practice deleting
conn.execute("INSERT INTO SIMPSON_INFO \
    (NAME, GENDER, AGE, OCCUPATION) VALUES \
    ('Homer Simpson', 'Male', 40, 'Nuclear Plant')");

# Add Lisa to the table
conn.execute("INSERT INTO SIMPSON_INFO \
    (NAME, GENDER, AGE, OCCUPATION) VALUES \
    ('Lisa Simpson', 'Female', 8, 'Student')");

# Deleting from the table
conn.execute("DELETE from SIMPSON_INFO where ID=2;")

# Save Changes
conn.commit()

#Get Info from database
cursor = conn.execute("SELECT * from SIMPSON_INFO")
#print cursor

#Get Data from cursor
rows = cursor.fetchall()
print rows

#Selecting specific info
homer = conn.execute("SELECT * from SIMPSON_INFO where NAME = 'Homer Simpson';")

female = conn.execute("SELECT * from SIMPSON_INFO where GENDER = 'Female';")

student = conn.execute("SELECT * from SIMPSON_INFO where \
    OCCUPATION = 'Student';")

#Print the results
hom = homer.fetchall()
print "Search Results: ",hom

fem = female.fetchall()
print "Search Results: ",fem

stu = student.fetchall()
print "Search Results: ",stu

# Print the number of changes to Database
changes = conn.total_changes
print "Number of changes: ", changes

#Updating information
conn.execute("UPDATE SIMPSON_INFO set AGE=41 where NAME='Homer Simpson';")

# Save Changes
conn.commit()

#Selecting specific info
homer = conn.execute("SELECT * from SIMPSON_INFO where NAME = 'Homer Simpson';")

#Print the results
hom = homer.fetchall()
print "Search Results: ",hom
