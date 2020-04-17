#! python3
# randomChore.py

import random, smtplib

# User information
my_email = 'email@gmail.com'
my_pw = 'passowrd'

# List of recipient email addresses
emails = ['recipient1@gmail.com',
          'recipient2@gmail.com']

def assignment():
    """"Function to assign chores and email them to email addresses in the list"""

    chores = ['Wash the dishes',
              'Walk the dog',
              'Mop the floor',
              'Feed the cat',
              'Clean the toilet',
              'Mow the lawn',
              'Clean the kitchen']
    for email in emails:
        random_chore = random.choice(chores)
        email_dict[email] = random_chore
        chores.remove(random_chore)
    for email in email_dict:
        message = str('Subject: Your random chore is... \n{}'.format(email_dict[email]))
        print(email.ljust(27) + ' is assigned: ' + email_dict[email].rjust(23))
        smtpObj.sendmail(from_addr=my_email, to_addrs=email, msg=message)

# Empty dictionary to collect emails with chores
email_dict = {}

# Logging into the SMTP Server
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(my_email, my_pw)

# Calling the function to send the email every week
assignment()

# Logging out of SMTP server
smtpObj.quit()



