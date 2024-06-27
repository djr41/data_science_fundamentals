# ========= Task 3 - manipulation.py =========
# Request user to enter a sentence/string
# Manipulate this string as intructed in the task description

str_manip = input("Please enter a sentence: ")

# Calculate and display the length of str_manip.
print(len(str_manip))

# Find the last letter in str_manip and replace every occurrence with '@'
print(str_manip.replace(str_manip[-1], '@'))

# Print the last three characters in str_manip backwards
print(str_manip[-1:-4:-1])

# Print the the first three characters and the last two characters in str_manip
print(str_manip[0:3]+str_manip[-2:])