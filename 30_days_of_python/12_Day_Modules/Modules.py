#Creating a Module
# mymodule.py file
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname

#Importing a Module
# main.py file
import mymodule
print(mymodule.generate_full_name('Zonique', 'Foyle')) # Zonique Foyle

#Import Functions from a Module
# main.py file
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Zonique','Foyle'))    # Zonique Foyle
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'])

#import Functions from a Module and Rename It
# main.py file
# main.py file
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Zonique','Foyle'))
print(total(1, 9))
mass = 100 
weight = mass * g
print(weight)
print(p)
print(p['firstname'])

#Import Bulit-in Modules
# OS Module
# import the module
import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()

#Sys Module
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))


#Statistics Module
from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

#Math Modules 
import math 
math.sqrt(16) #Find the square root of 16 # Returns 4.0 

math.pow(2, 3) #Find 2 to the power of 3 # Returns 8.0

dir (math) #This lists all the attributes and methods of the math module

math.pi #Returns the value of pi

math.log10(100) #Returns the base-10 logarithm of 100 # Returns 2.0

math.log10(1000) #Returns the base-10 logarithm of 1000 # Returns 3.0

math.floor(2.3) #Rounds down to the nearest integer # Returns 2

math.ceil(2.3) #Rounds up to the nearest integer # Returns 3

#String Module
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

#random Module
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive



#Calendar Module

import calendar
cal = calendar.month(2016, 1) #Returns the calendar of January 2016
print (cal)

calendar.isleap(2016) #Returns True if the year is a leap year, else False # Returns True

calendar.isleap(2015) #Returns True if the year is a leap year, else False # Returns False

dir (calendar) #This lists all the attributes and methods of the calendar module









