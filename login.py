#Variables
import time

#Global Variables
totalWrongAttempts = 0

#LOGIN USER/PASS
username = "test"
password = "test"

#Login
def login():
    ask = input("Welcome to Burn's Login System \nWhat would you like to do? \n 1. Login \n 2. Forgot login details? ")
    # Login to System
    if ask == "1":
        def Username():
            Username = input("Please enter your username. ")
            if Username == username:
                def Security():
                    Password = input("Please enter your password. ")
                    if Password == password:
                        print("Welcome,", username.upper())
                        #
                    if Password != password:
                        print("Wrong Password.")
                        global totalWrongAttempts
                        totalWrongAttempts = totalWrongAttempts
                        totalWrongAttempts + 1
                        if totalWrongAttempts == 5:
                            print("You've typed the wrong password 5 times you must now wait 15 seconds to continue")
                            time.sleep(15)
                        return Security()
                Security
                Security()
            else:
                print("Wrong username please try again")
                return Username()
        Username
        Username()
    # Retrieve Password
    if ask == "2":
        forgotPassword = input("What information would you like to retrieve? \n 1. Username \n 2. Password ")
        if forgotPassword == "1":
            securityQuestion = input("What is the first 3 digits of Pi? ")
            if securityQuestion == "3.14":
                print("Your Username is:", username)
                return login()

            else:
                print("Wrong Answer")
                return login()

        if forgotPassword == "2":
            securityQuestion2 = input("What is Vandal headshot damage? ")
            if securityQuestion2 == "160":
                print("Your Password is:", password)
                return login()
            
            else:
                print("Wrong Answer")
                return login()

    else:
        print("The number you've entered is invalid, please try again")
        return login()
login            
login()

"""
Might Add
- Timeout for password
- Safer security for login
- Forgot Account Details
- Create an account
- Change details without editing file
- Add things to list
"""
