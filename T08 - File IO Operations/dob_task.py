# ======== Task 8 - dob_task.py =====================
# Make sure the file 'DOB.txt' is local to where you are running this script
# This program prints out the names in this file and then the birthdates

# for formatting titles in bold
startb = '\033[1m'
endb = '\033[0m'

# store the file data as a list of strings in the variable lines
with open('DOB.txt', 'r+') as file:
    lines = file.readlines()

# for each line print out the names
print(startb+'\nName'+endb)
for line in lines:
    line=line.split()
    print(str(line[0])+" "+str(line[1]))

# for each line print out the birthdates
print(startb+'\nBirthdate'+endb)
for line in lines:
    line=line.split()
    print(str(line[2])+" "+str(line[3])+" "+str(line[4]))
print("\n")