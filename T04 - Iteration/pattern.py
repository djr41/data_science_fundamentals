# ========= Task 4 - pattern.py =========
# Create code to display stated pattern using an if-else statement in combination with a for loop

for i in range(1, 10):
    if i <=5:
        print('*'*i)
    else:
        print('*'*(10-i))

# Uncomment the following code snippet to also allow the user to define the number of lines for the pattern 
number_of_lines = int(input("Please enter the number of lines for your pattern: "))
for i in range(1, number_of_lines+1):
    if i <= number_of_lines/2:
        print('*'*i)
    else:
        print('*'*(number_of_lines+1-i))