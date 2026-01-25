#IF CONDITION 
#syntax 
if condition: 
    this part of code run for truthy conditions 

#Example 1
a = 3
if a > 0:
    print("a is a positive number")
# A is a positive number


#IF ELSE
#syntax 
if condition:
    this part of code run for truthy conditions
else:
    this part of code run for falsy conditions
#Example 
A = 3
if a< 0:
    print("a is a negative number")
else:
    print("a is a positive number")


#IF ELIF ELSE
#syntax
if condition1:
    code
elif condition:
    code
else:
    code

#Example
a = 0
if a > 0:
    print("a is a positive number")
elif a < 0:
    print("a is a negative number")
else:
    print("a is zero")


#SHORT HAND
#syntax
code if condtion else code

#Example
a = 3
print("a is a positive number") if a > 0 else print("a is a negative number")

#NESTED CONDDITONS 
#syntax
if condition:
    code
    if condition:
        code
    else:
        code

#Example
a = 3
if a >= 0:
    if a == 0:
        print("a is zero")
    else:
        print("a is a positive number")
elif: a == 0:
    print('a is zero')
else:
    print("a is a negative number") 

#IF CONFITION AND LOGICAL OPERATORS
#syntax
if condition and condition:
    Code 

#Example
a = 0
if a > 0 and a % 2 == 0:
    print('a is an even and positive integer')
elif a > 0 and a % 2 != 0:
    print('a is a positive integer')
elif a == 0:
    print('a is zero')
else:
    print('a is a negative')

#IF AND OR LOGICAL OPERATORS
#syntax
if condition or condition:
    Code 

#Example
user = 'James'
access_level = 3
if user == 'admit' or access_level >= 4:
    print('Access granted')
else:
    print('Access denied !')

