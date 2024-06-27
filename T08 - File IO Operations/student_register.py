# ======== Task 8 - student_register.py =====================
# Program asks user to input the number of students they would like to register
# and creates a simple attendance register

try:
    # prompt user for the amount of students registering
    num = int(input("How many students would you like to register?:"))
    with open('reg_form.txt', 'w') as f:      # opens file named 'reg-form.txt' in the local directory
        for i in range(0,num):                # loops over the amount of students registering
            student_ID_number=input("Please enter student ID number:")
            f.write(student_ID_number+" ..........................\n\n")    # writes student ID number to file
except ValueError:
    print("Please enter an integer value e.g. (24)")      # gracefully returns error if num is not an integer


