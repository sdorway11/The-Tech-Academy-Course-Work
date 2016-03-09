import sqlite3

# connect to database
conn = sqlite3.connect('simpsons.db')

# Create Simpsons info table function
def createTable():
    conn.execute("CREATE TABLE if not exists SIMPSON_INFO ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        NAME TEXT, \
        GENDER TEXT, \
        AGE INT, \
        OCCUPATION TEXT \
        );")

createTable()

# Printing Clean Data Function
def printData(data):
    for row in data:
        print "ID: ", row[0]
        print "Name: ", row[1]
        print "Gender: ", row[2]
        print "Age: ", row[3]
        print "Occupation: ", row[4], "\n"
        

# Create user input function to enter into the table
def newCharacter():
    print '\nAdding a new Character...'

    # Take Inputs
    name = raw_input('Name: ')
    gender = raw_input('Gender: ')
    age = raw_input('Age: ')
    occupation = raw_input('Occupation: ')

    # Create values part of sql command
    val_str = "'{}','{}','{}','{}'".format( \
        name, gender, age, occupation)
    #print val_str

    # Add val_str to the rest of the sql
    sql_str = "INSERT INTO SIMPSON_INFO \
        (NAME, GENDER, AGE, OCCUPATION) \
        VALUES ({});".format(val_str)
    #print sql_str

    # Executing the sql code
    conn.execute(sql_str)
    conn.commit()
    print "Number of changes: ", conn.total_changes

# Create function to view the table
def viewAll():
    # Create sql string
    sql_str = "SELECT * from SIMPSON_INFO"
    cursor = conn.execute(sql_str)

    # Get data from cursor
    rows = cursor.fetchall()
    print rows


def viewDetails():
    print "\nViewing character details"

    # Take name input
    name = raw_input("Enter the character's name: ")
    #print name

    # sql query for info
    sql_str = "SELECT * from SIMPSON_INFO where \
        NAME = '{}'".format(name)
    #print sql_str

    # Execute sql string
    cursor = conn.execute(sql_str)

    # Get data from array
    rows = cursor.fetchall()
    if len(rows) == 0:
        # There is no data in the array
        print "There are no records found"
    else:
        # Print the data
        printData(rows)

def deleteCharacter():
    print"\nDeleting a Character"

    # Take name input
    name = raw_input("Enter the character's name: ")
    sql_str = "SELECT * from SIMPSON_INFO where \
        NAME = '{}'".format(name)
    cursor = conn.execute(sql_str)
    rows = cursor.fetchall()

    change_id = 0
    
    if len(rows) == 0:
        # There is no data in the array
        print "There are no records found"

        # End the function
        return
    
    elif len(rows) == 1:
        print "One record found"
        #Select row
        row = rows[0]
        #Select ID
        change_id = row[0]
        printData(rows)
        
    else:
        print "More than one record found..."
        printData(rows)
        change_id = raw_input("Type the ID of the character to date: ")
        print "Change ID: ", change_id

    # Confim the delete
    delete = raw_input("Confim character delete (y/n): ")
    if delete == 'y':
        sql_str = "DELETE from SIMPSON_INFO where \
            ID = '{}'".format(change_id)
        conn.execute(sql_str)
        conn.commit()
        print "Number of changes: ", conn.total_changes

    else:
        print "No action performed"
        return

def updateCharacter():
    print"\nUpdating a Character"

    # Take name input
    name = raw_input("Enter the character's name: ")
    sql_str = "SELECT * from SIMPSON_INFO where \
        NAME = '{}'".format(name)
    cursor = conn.execute(sql_str)
    rows = cursor.fetchall()

    change_id = 0
    
    if len(rows) == 0:
        # There is no data in the array
        print "There are no records found"

        # End the function
        return
    
    elif len(rows) == 1:
        print "One record found"
        #Select row
        row = rows[0]
        #Select ID
        change_id = row[0]
        printData(rows)
        
    else:
        print "More than one record found..."
        printData(rows)
        change_id = raw_input("Type the ID of the character to date: ")
        print "Change ID: ", change_id

    print "Insert the updated info:"

    # Get change data
    name = raw_input("Name: ")
    gender = raw_input("Gender: ")
    age = raw_input("Age: ")
    occupation = raw_input("Occupation: ")
    if not name == '':
        sql_str = "UPDATE SIMPSON_INFO \
            set NAME='{}' where ID={}" \
            .format(name, change_id)
        conn.execute(sql_str)
        
    if not gender == '':
        sql_str = "UPDATE SIMPSON_INFO \
            set GENDER='{}' where ID={}" \
            .format(gender, change_id)
        conn.execute(sql_str)
        
    if not age == '':
        sql_str = "UPDATE SIMPSON_INFO \
            set AGE={} where ID={}" \
            .format(age, change_id)
        conn.execute(sql_str)
        
    if not occupation == '':
        sql_str = "UPDATE SIMPSON_INFO \
            set OCCUPATION='{}' where ID={}" \
            .format(occupation, change_id)
        conn.execute(sql_str)

    conn.commit
    print "Number of changes: ", conn.total_changes
    sql_str = "SELECT * from SIMPSON_INFO where ID={}".format(change_id)
    cursor = conn.execute(sql_str)
    rows = cursor.fetchall()
    printData(rows)
    

def options():
    # Print out the options
    print "\nWhat would you like to do?"

    print "1. Add new character"
    print "2. View all characters"
    print "3. Search for a character"
    print "4. Delete a character"
    print "5. Update a character"
    print "6. Exit"

    # Ask user what they want to do
    response = raw_input("Enter number: " )

    if response == "1":
        newCharacter()
    elif response == "2":
        viewAll()
    elif response == "3":
        viewDetails()
    elif response == "4":
        deleteCharacter()
    elif response == "5":
        updateCharacter()
    else:
        print "Exiting the program"
        return 
       

def mainLoop():
    in_loop = True
    while in_loop == True:
        
        # Run options function
        options()

        # Ask user if they want to continue
        again = raw_input("Would you like to do something else? (y/n): ")

        # If answer does not equal y exit loop
        if again != "y":
            in_loop = False


#newCharacter()
#viewAll()
#viewDetails()
mainLoop()
