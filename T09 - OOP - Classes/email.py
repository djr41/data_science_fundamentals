### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

class Email():
    # Constructor method
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
    # Declare the has_been_read class variable, with default value False for emails. 
        self.has_been_read = False

    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True

# --- Functions --- #
# Here are the required functions for this email simulator.

def populate_inbox():
    email_1  = Email("support@hyperiondev.com", "Your submission has been reviewed!", "Your submission for the following task was reviewed successfully")
    email_2  = Email("noreply@cogrammar.com", "Discover exclusive career opportunities", "We hope this email finds you well and thriving in your coding journey.")
    email_3  = Email("no-reply@livestorm-events.com", "Here's your access link", "You've registered for 'Skills Bootcamp Cohort 7 - Academic Sessions - Python'")
    inbox = [email_1, email_2, email_3]
    return inbox

def list_emails():
    
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    email_list = list(enumerate(inbox))
    for i in range (0,len(email_list)):
        print(email_list[i][0],email_list[i][1].subject_line)

def read_email(index):
#     # Create a function which displays a selected email. 
    print(f"\nThe following email has now been 'Marked as Read'\n \
          \nFrom: {inbox[index].email_address} \
          \nSubject: {inbox[index].subject_line} \
          \nContents: {inbox[index].email_content}")

#     # Once displayed, call the class method to set its 'has_been_read' variable to True.
    inbox[index].mark_as_read()

# # --- Email Program --- #

# # Call the function to populate the Inbox.
inbox = populate_inbox()

# # Menu operations with the required logic.
menu = True

while menu == True:
     user_choice = int(input('''\nWould you like to:
     1. Read an email
     2. View unread emails
     3. Quit application

     Enter selection: '''))
       
     if user_choice == 1:
         list_emails()
         index = int(input("\nPlease enter the index of the email that you would like to read: "))
         read_email(index)
        
     elif user_choice == 2:
         print("\nHere are a list of your unread emails: ")
         unread_email_count=0
         for i in range (0,len(inbox)):
                # check for unread emails and print the subject line
                if inbox[i].has_been_read == False:
                  print(inbox[i].subject_line)
                  unread_email_count=unread_email_count+1
         if unread_email_count == 0:  
             #if there are no unread emails the following is printed 
             print("You have read all your emails!")
            
     elif user_choice == 3:
         menu = False
         print("\nYou are now exiting the email program\n")

     else:
         print("Oops - incorrect input.")

