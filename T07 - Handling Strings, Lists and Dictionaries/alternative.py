# ========= Task 7 - alternative.py =========
# Program to display a user-defined string with
# (1) Alternate characters in upper/lower case
# (2) Alternate words in lower/upper case

# get string from the user
user_string = input("Please enter a sentence:")

# --- Part 1 - Alternate characters in upper/lower case ------
# initialise a char_list to loop through
char_list=list(range(0,len(user_string)))

# loop through the list and make every alternate character either uppercase or lowercase
for i in char_list:
    if i % 2 == 0:
        char_list[i] = user_string[i].upper()
    else:
        char_list[i] =user_string[i].lower()

# convert the list into a string and print the result
alternate_char_str="".join(char_list)
print(alternate_char_str)


# --- Part 2 - Alternate words in lower/upper case -----------
# split the user defined string into separate words
word_list=user_string.split()

# loop through this list and make every alternate word either lowercase or uppercase 
for i in list(range(0,len(word_list))):
    if i % 2 == 0:
        word_list[i]=str(word_list[i]).lower()
    else:
        word_list[i]=str(word_list[i]).upper()


# convert the list into a string and print the result
alternate_word_str=" ".join(word_list)
print(alternate_word_str)