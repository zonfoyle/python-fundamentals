
#Numpy
#Importing NumPy

#How to import numpy
import numpy as np 

#How to check the version of the numpy package 
print('numpy:', np.__version__)

#Checking the available methods 
print(dir(np))


#----------------------------------------------------------------

#Creating numpy array using 
#Cretaing int numpy arrays 

# Creating python List
python_list = [1,2,3,4,5]

# Checking data types
print('Type:', type (python_list)) # <class 'list'>
#
print(python_list) # [1, 2, 3, 4, 5]

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]

print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# Creating Numpy(Numerical Python) array from python list

numpy_array_from_list = np.array(python_list)
print(type (numpy_array_from_list))   # <class 'numpy.ndarray'>
print(numpy_array_from_list) # array([1, 2, 3, 4, 5])

two_dimensional_list = [[0, 1, 2], [3, 4, 5] []]



#Creating float numpy arrays 
# Python list
python_list = [1,2,3,4,5]

numy_array_from_list2 = np.array(python_list, dtype=float)
print(numy_array_from_list2) # array([1., 2., 3., 4., 5.])


#Creating boolean numpy arrays 
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array) # array([False,  True,  True, False, False])


#Creating multidimensional array using numpy
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type (numpy_two_dimensional_list))
print(numpy_two_dimensional_list)

<class 'numpy.ndarray'>
[[0 1 2]
[3 4 5]
[6 7 8]]


#Converting numpy array to list
# We can always convert an array back to a python list using tolist().
np_to_list = numpy_array_from_list.tolist()
print(type (np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())

<class 'list'>
one dimensional array: [1, 2, 3, 4, 5]
two dimensional array:  [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


#Creating numpy array from tuple 
# Numpy array from tuple
# Creating tuple in Python
python_tuple = (1,2,3,4,5)
print(type (python_tuple)) # <class 'tuple'>
print('python_tuple: ', python_tuple) # python_tuple:  (1, 2, 3, 4, 5)

numpy_array_from_tuple = np.array(python_tuple)
print(type (numpy_array_from_tuple)) # <class 'numpy.ndarray'>
print('numpy_array_from_tuple: ', numpy_array_from_tuple) # numpy_array_from_tuple:  [1 2 3 4 5]



#Shape of numpy array

#The shape method provide the shape of the array as a tuple. The first is the row and the second is the column. If the array is just one dimensional it returns the size of the array.

nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('shape of nums: ', nums.shape)
numpy_two_dimensional_list = np.array([[0,1,2],[3,4,5],[6,7,8]])
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3],
    [4,5,6,7],
    [8,9,10,11]]
print(three_by_four_array)
print('shape of three_by_four_array: ', three_by_four_array.shape)
    [1 2 3 4 5]
    shape of nums:  (5,)
    [[0 1 2]
     [3 4 5]
     [6 7 8]]
shape of numpy_two_dimensional_list:  (3, 3)
(3, 4)
Data type of numpy array

#Type of data types: str, int, float, complex, bool, list, None

int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)
    [-3 -2 -1  0  1  2  3]
    int64
    [-3. -2. -1.  0.  1.  2.  3.]
    float64
#Size of a numpy array

#In numpy to know the number of items in a numpy array list we use size

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                              [3, 4, 5],
                              [6, 7, 8]])

print('The size:', numpy_array_from_list.size) # 5
print('The size:', two_dimensional_list.size)  # 3
    The size: 5
    The size: 9
#Mathematical Operation using numpy

#3NumPy array is not like exactly like python list. To do mathematical operation in Python list we have to loop through the items but numpy can allow to do any mathematical operation without looping. Mathematical Operation:

Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
Modules (%)
Floor Division(//)
Exponential(**)
Addition

# Mathematical Operation
# Addition
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list  + 10
print(ten_plus_original)
    original array:  [1 2 3 4 5]
    [11 12 13 14 15]
Subtraction

# Subtraction
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_minus_original = numpy_array_from_list  - 10
print(ten_minus_original)
    original array:  [1 2 3 4 5]
    [-9 -8 -7 -6 -5]
Multiplication

# Multiplication
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list * 10
print(ten_times_original)
    original array:  [1 2 3 4 5]
    [10 20 30 40 50]
Division

# Division
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list / 10
print(ten_times_original)
    original array:  [1 2 3 4 5]
    [0.1 0.2 0.3 0.4 0.5]
Modulus

# Modulus; Finding the remainder
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list % 3
print(ten_times_original)
    original array:  [1 2 3 4 5]
    [1 2 0 1 2]
Floor Division

# Floor division: the division result without the remainder
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list // 10
print(ten_times_original)
Exponential

# Exponential is finding some number the power of another:
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list  ** 2
print(ten_times_original)
    original array:  [1 2 3 4 5]
    [ 1  4  9 16 25]
Checking data types

#Int,  Float numbers
numpy_int_arr = np.array([1,2,3,4])
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)
    int64
    float64
    bool
##Converting types

#We can convert the data types of numpy array

Int to Float
numpy_int_arr = np.array([1,2,3,4], dtype = 'float')
numpy_int_arr
array([1., 2., 3., 4.])
Float to Int
numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
numpy_int_arr
    array([1, 2, 3, 4])
Int ot boolean
np.array([-3, -2, 0, 1,2,3], dtype='bool')
    array([ True,  True, False,  True,  True,  True])
Int to str
numpy_float_list.astype('int').astype('str')
    array(['1', '2', '3'], dtype='<U21')
Multi-dimensional Arrays

# 2 Dimension Array
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type (two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)
    <class 'numpy.ndarray'>
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    Shape:  (3, 3)
    Size: 9
    Data type: int64
#Getting items from a numpy array

# 2 Dimension Array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)
    First row: [1 2 3]
    Second row: [4 5 6]
    Third row:  [7 8 9]
first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)
    First column: [1 4 7]
    Second column: [2 5 8]
    Third column:  [3 6 9]
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
#Slicing Numpy array

#Slicing in numpy is similar to slicing in python list

two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)
    [[1 2]
     [4 5]]
#How to reverse the rows and the whole array?

two_dimension_array[::]
    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])
#Reverse the row and column positions

    two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
    two_dimension_array[::-1,::-1]
    array([[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]])
#How to represent missing values ?

    print(two_dimension_array)
    two_dimension_array[1,1] = 55
    two_dimension_array[1,2] =44
    print(two_dimension_array)
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    [[ 1  2  3]
     [ 4 55 44]
     [ 7  8  9]]
    # Numpy Zeroes
    # numpy.zeros(shape, dtype=float, order='C')
    numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
    numpy_zeroes
    array([[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]])
# Numpy Zeroes
numpy_ones = np.ones((3,3),dtype=int,order='C')
print(numpy_ones)
    [[1 1 1]
     [1 1 1]
     [1 1 1]]
twoes = numpy_ones * 2
# Reshape
# numpy.reshape(), numpy.flatten()
first_shape  = np.array([(1,2,3), (4,5,6)])
print(first_shape)
reshaped = first_shape.reshape(3,2)
print(reshaped)
    [[1 2 3]
     [4 5 6]]
    [[1 2]
     [3 4]
     [5 6]]
flattened = reshaped.flatten()
flattened
    array([1, 2, 3, 4, 5, 6])
    ## Horitzontal Stack
    np_list_one = np.array([1,2,3])
    np_list_two = np.array([4,5,6])

    print(np_list_one + np_list_two)

    print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))
    [5 7 9]
    Horizontal Append: [1 2 3 4 5 6]
    ## Vertical Stack
    print('Vertical Append:', np.vstack((np_list_one, np_list_two)))
    Vertical Append: [[1 2 3]
     [4 5 6]]
#Generating Random Numbers

    # Generate a random float  number
    random_float = np.random.random()
    random_float
    0.018929887384753874
    # Generate a random float  number
    random_floats = np.random.random(5)
    random_floats
    array([0.26392192, 0.35842215, 0.87908478, 0.41902195, 0.78926418])
    # Generating a random integers between 0 and 10

    random_int = np.random.randint(0, 11)
    random_int
    4
    # Generating a random integers between 2 and 11, and creating a one row array
    random_int = np.random.randint(2,10, size=4)
    random_int
    array([8, 8, 8, 2])
    # Generating a random integers between 0 and 10
    random_int = np.random.randint(2,10, size=(3,3))
    random_int
    array([[3, 5, 3],
           [7, 3, 6],
           [2, 3, 3]])
#Generationg random numbers

    # np.random.normal(mu, sigma, size)
    normal_array = np.random.normal(79, 15, 80)
    normal_array





import math 
import statistics 

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 1000]

print(sum(numbers) / len(numbers))
print(statistics. mean(numbers))

print(statistics.median(numbers))
if len(numbers) % 2 == 0:
    print(numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1] / 2)
else:
    print(numbers[len(numbers) // 2 ])

print(statistics.mode(numbers))
print(max(set(numbers), key=numbers.count))