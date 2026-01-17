# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ") # This is a string

if len(username) > 12:                     # This is an integer, and we are saying not more than 12 characters
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:         # This is checking for spaces in the string, no space is required
    print("Your username can't contain spaces")
elif not username.isalpha():                # This is checking for digits in the string, no digits are required
    print("Your username can't contain numbers ")
else: 
    print(f"Welcome, {username}")           #This is saying if all conditions are met, welcome the user