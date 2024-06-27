# ========= Task 3 - award.py =========
# Read in times for all three events
# Calculate and display the total time
# Determine and display the award that the participant will receive

# I choose to cast these variables as floats as the problem still makes sense for event times with non-integer values
# the next stage would be to ask for the user to input the event times in a particular format e.g. h:mm:ss:00
swim_time=float(input("Please enter the time in minutes for the swim: "))
cycling_time=float(input("Please enter the time in minutes for the cycling: "))
running_time=float(input("Please enter the time taken in minutes for the running: "))

# ----------------------------------------------------------------
# Optional error checking
# if swim_time<=0:
#     print("Please enter a positive value for the swim time")
#     quit()
# elif cycling_time<=0:
#     print("Please enter a positive value for the cycling time")
#     quit()
# elif running_time<=0:
#     print("Please enter a positive value for the running time")
#     quit()
# ----------------------------------------------------------------

triathlon_time=swim_time+cycling_time+running_time

print(f"The total time taken for the triathlon is {triathlon_time} minutes")

if triathlon_time<=100:
    print("Congratulations you have been awarded: 'Provincial colours'")
elif triathlon_time<=105:
    print("Congratulations you have been awarded: 'Provincial half colours'")
elif triathlon_time<=110:
    print("Congratulations you have been awarded a: 'Provincial scroll'")
elif triathlon_time>110:
    print("You did not qualify for an award at this event - keep training and better luck next time!")