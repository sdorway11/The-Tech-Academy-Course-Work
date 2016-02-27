name = "Guido"

print name.upper()

print name.lower()

print name.capitalize()

date = "11/12/2013"

#Go though string and split
#Where there is a '/'
date_manip = date.split('/')

#Show the outcome
print date_manip

print 'Month: ' + date_manip[0]
print 'Day: ' + date_manip[1]
print 'Year: ' + date_manip[2]

print ('Month: ' + date_manip[0] +
     '. Day: ' + date_manip[1] +
     '. Year: ' + date_manip[2])

print name.title()

print name.swapcase()

phrase = "Spencer's Address:        1625 killarney dr."
print phrase.strip()
