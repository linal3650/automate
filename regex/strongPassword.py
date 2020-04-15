#! python3
# strongPassword.py

import re

# TODO: 8 characters long, contains both uppercase and lowercase characters, has at least one digit
passwordRegex = re.compile('''(
    ^(?=.*[A-Z].*[A-Z])         # at least two capital letters
    (?=.*[!@#$&*])               # at least one of these special characters
    (?=.*[0-9].*[0-9])          # at least two numeric digits
    (?=.*[a-z].*[a-z].*[a-z])   # at least three lower case letters
    .{8,}                      # at least 8 total digits
    $
    )''', re.VERBOSE)

def userInputPasswordCheck():
    ppass = input("Enter a potential password: ")
    mo = passwordRegex.search(ppass)
    if not(mo):
        print("Not a strong password, please try again")
        return False
    else:
        print("Strong Password")
        return True

userInputPasswordCheck()



