# ========= Task 3 - numbers.py =========
# Request user to enter three different integers
# Print out the calculations as instructed in the task description

num1 = int(input("Please enter your first integer: "))
num2 = int(input("Please enter your second integer: "))
num3 = int(input("Please enter your third integer: "))

# The sum of all the numbers
print(num1+num2+num3)

# The first number minus the second number
print(num1-num2)

# The third number multiplied by the first number
print(num3*num1)

# The sum of all three numbers divided by the third number
print((num1+num2+num3)/num3)