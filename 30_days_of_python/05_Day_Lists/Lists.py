#How to Create a List

# Using list built in function
#syntax
lst = list()
empty_list = list () # this is an empty list, no item in the list 

# Using square brackets, []
#syntax
lst = []
empty_list = [] # this is an empty list, no item in the list
print(len(empty_list)) # 0

#List with initials values. We use len() to find the lenght of a list. 

fruits = ['banana', 'orange', 'mango', 'lemon'] # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot'] # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yogurt'] # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Denmark', 'Sweden', 'Norway', 'Iceland'] # list of countries in the nordic region


#Printing lists and their lengths
print('Fruits', fruits)
print('Number of fruits:',len(fruits))
