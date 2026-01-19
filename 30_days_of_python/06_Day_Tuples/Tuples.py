#CREATING EMPTY TUPLES

# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

#Tuples with initial values
# syntax
tp1 = ('item1','item2','item3')
fruits = ('banana','orange', 'mango', 'lemon')

#TUPLES LENGTH
#we use len() method to get the length of a tuple

tp1 = ('item1','item2','item3')
len(tp1)


#ACESSING TUPLE INTEMS

#Syntax
tp1 = ('item1','item2','item3')
first_item = tp1[0] # accessing first item
second_item = tp1[1] # accessing second item

fruits = ('banana','orange', 'mango', 'lemon')
first_fruit = fruits[0] # accessing first fruit
second_fruit = fruits{1}
last_index = len(fruits) - 1
last_fruit = fruits[last_index] # accessing last fruit

#negative indexing
tp1 = ('item1','item2','item3','item4')
first_item = tp1[-4] # accessing first item
second_item = tp1[-3] # accessing second item
last_item = tp1[-1] # accessing last item

#SLICING TUPLES

#syntax
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:] # from index 1 to the end

#Range of negative index
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:] # from index -3 to the end

#CHANGING TUPLES TO LISTS AND VICE VERSA
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)  # converting tuple to list

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')

#CHECKING ITEM EXISTENCE IN TUPLE

# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment

#JOINING TUPLES

# Syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables

#DELETING A TUPLE
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits

