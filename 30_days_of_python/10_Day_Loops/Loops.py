#If Condition

# syntax
import code


if condition:
   # this part of code runs for truthy conditions
#Example: 1

a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number

#If Else

#If condition is true the first block will be executed, if not the else condition will run.

# syntax
if condition:
    #this part of code runs for truthy conditions
else:
     #this part of code runs for false conditions
#Example:

a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
#The condition above proves false, therefore the else block was executed. How about if our condition is more than two? We could use elif.

#If Elif Else

#In our daily life, we make decisions on daily basis. We make decisions not by checking one or two conditions but multiple conditions. As similar to life, programming is also full of conditions. We use elif when we have multiple conditions.

# syntax
if condition:
    #code
elif condition:
    #code
else:
    #code
#Example:

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
#Short Hand

# syntax
#code if condition else code
#Example:

a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed
#Nested Conditions

#Conditions can be nested

# syntax
if condition:
    #code
    if condition:
        #code
#Example:

a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
#We can avoid writing nested condition by using logical operator and.

#If Condition and Logical Operators

# syntax
if condition and condition:
    #code
#Example:

a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
#If and Or Logical Operators

# syntax
if condition or condition:
    #code
#Example:

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')