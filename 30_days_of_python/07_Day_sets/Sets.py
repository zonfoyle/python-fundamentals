#CREATING A SET

#syntax 
st = set()

#syntax 
st = {'item1', 'item2', 'item3','item4'}

#Example 
fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits) #4

#ACCESS ITEMS IN A SET

#syntax (Checking if an item exists in a set)
st = {'item1', 'item2', 'item3','item4'}
print("Does set st contain item3? ", 'item3' in st) #True

#Example 
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) #True

#ADDING ITEMS TO A SET
#syntax (Adding one item using odd)
st = {'item1', 'item2', 'item3','item4'}
st.update(['item5', 'item6','item7']) #Adding multiple items using update()

#Example 
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)


#REMOVING ITEMS FROM A SET
#syntax (Removing an item using remove())
st = {'item1', 'item2', 'item3','item4'}
st.remove('item2') #removes item2 from the set

#Example
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop() #removes a random item from the set
#If we are interested in the removed item.
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()

#CLEARNING ITEMS IN A SET
#syntax (Clearing all items in a set)
st = {'item1', 'item2', 'item3','item4'}
st.clear() #removes all items from the set

#Example
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear() #removes all items from the set
print(fruits) #set()

#DELETING A SET
#syntax (Deleting the set completely)
st = {'item1', 'item2', 'item3','item4'}
del st #deletes the set completely
#Example
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits #deletes the set completely

#CONVERTING LIST TO SET
#syntax
lst = ['item1', 'item2', 'item3','item4']
st = set(lst) # {'item1', 'item2', 'item3','item4'} - the order is random, because sets are unordered
#Example
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana', 'orange']
fruits_set = set(fruits) # {'banana', 'orange', 'mango', 'lemon'} - duplicates are removed

#JOINING SETS
#syntax (Using union())
st1 = {'item1', 'item2', 'item3','item4'}
st2 = {'item5', 'item6', 'item7','item8'}
st3 = st1.union(st2) # st3 = st1 | st2

#Example
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'banana', 'orange', 'mango', 'lemon', 'tomato', 'potato', 'cabbage', 'onion', 'carrot'}

#syntax (Using update())
st1 = {'item1', 'item2', 'item3','item4'}
st2 = {'item5', 'item6', 'item7','item8'}
st1.update(st2) #st1 now contains items from both sets

#Example
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'banana', 'orange', 'mango', 'lemon', 'tomato', 'potato', 'cabbage', 'onion', 'carrot'}

#FINDING INTERSECTION ITEMS 
#syntax (Using intersection())
st1 = {'item1', 'item2', 'item3','item4'}
st2 = {'item3', 'item2',}
st1.intersection(st2) # {'item2', 'item3'}

#Example 
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
# python & dragon

#CHECKING SUBSET AND SUPERSET
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True

#Example 
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False

#CHECKING THE DIFFERENCE BETWEEN TWO SETS

#syntax (Using difference())
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set() : st2 - st1
st1.difference(st2) # {'item1', 'item4'} => st1\st2  : st2 - st1

#Example 
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
# python - dragon
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
# dragon - python

#FINDING SYMMETRIC DIFFERENCE BETWEEN TWO SETS
#syntax (Using symmetric_difference())
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'} : st2 ^ st1

#Example
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
# python ^ dragon

#JOINING SETS 
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False

#Example 
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}