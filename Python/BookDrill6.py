# Create the list of epic proggramers
epic_programmer_list = ["Tim Berners-Lee",
                        "Guido van Rossum",
                        "Linus Torvalds",
                        "Larry Page",
                        "Sergey Brin",]

# print to console
print "Epic programmers: " + epic_programmer_list[0]
print "Epic programmers: " + epic_programmer_list[1]
print "Epic programmers: " + epic_programmer_list[2]
print "Epic programmers: " + epic_programmer_list[3]
print "Epic programmers: " + epic_programmer_list[4]

#epic_programmer_list[4]="Me"
#print epic_programmer_list

# Add myself to the end of the list
epic_programmer_list.append("Me")
print "An epic programmer: " + epic_programmer_list[5]


# Looping through each item in
epic_programmer_list
for programmer in epic_programmer_list:
    # Print the programmers' name to console
    print "An epic programmer: " + programmer

# Create list of numbers
number_list = [1,2,3,4,5]
empty_number_list = []

# Loop each number in number_list
for x in number_list:
    # Append each number to the power of 2
    # to the empty_number_list
    empty_number_list.append(x**2)

print empty_number_list
