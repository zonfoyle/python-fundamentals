#Example of a Python Error

age = int("hello")

#Output

ValueError: invalid Literal for int()   #Why?, Because this si trying to turn text ("hello") inot a number.



# "TypeError" (Happens when you use the wrong data type)
print("5" + 3)

#Output X Error
TypeError: can only concatenate str (not "int")

#Correct way
print(int("5") + 3)



# "ValueError" (Happens when the value is wrong)
 int ("abc")

#Output X Error
ValueError: invalid literal for int()



# "NameError"   (Happens when a variable is not defined)
printage(age)

#Output X Error
NameError: name 'age' is not defined



# "IndexError"   (Happens when accessing an index that doesn't exist)
numbers = [1,2,3]
print(numbers[5])


#Output X Error
IndexError: list index out of range


# "KeyError"  (Happens when a key does not exist in a dictionary)
person = {"name": "Zonique"}
print(person["age"])

#Output X Error
KeyError: 'age'



# "ZeroDivisionError" (Happens when dividing by zero)
print(10/0)

#Output X Error
ZeroDivisionError: division by zero