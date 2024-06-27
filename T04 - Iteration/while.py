# ========= Task 4 - while.py =========
# Request user enters numbers while they don't enter -1
# Calculate average of the numbers (excluding -1) that were entered

num = 0         # variable for numbers that user inputs
count = 0       # number count
total = 0       # running total of user inputted numbers

while num != -1:
    num = float(input("Please enter a number: "))
    if num == -1:         # break condition
        break
    total = total + num   
    count += 1            
    
average = total/(count)
print(f"The average of the numbers (excluding -1) that you entered is: {average}")