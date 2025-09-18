# Introduction to Numerical Python

# Package(numpy) is a combination of modules that are not necessarily included in the python distribution

# numpy is an abreviation for "Numerical Python"

# Importing the numpy package
import numpy as np

# Creating a numpy array
# array is a generic term for a multidimensional set of items of the same type
# we use the np.array() function to create an One-dimensional-array(vector)
x = np.array([12,14,16,18,20])
print(x)

y = np.array([2,4,6,8,10])
print(y)

print(x + y)

# In numpy matrices are typically represented as two-dimensional arrays
M = np.array([[2,4,6],[8,10,12]])       #Matrix
print(M)

# To access an attribute of an array, we use the array.attribute syntax
print(M.ndim)      # number of dimensions

print(M.shape)     # shape of the array (rows, columns)

print(M.dtype)     # data type of the array elements

print(M.size)      # total number of elements in the array (rows * columns)

# We can also create arrays using built-in functions
X = np.zeros((3,4))    # Create an array of zeros with 3 rows and 4 columns
print(X)

Y = np.matrix(np.ones((3,4)))    # Create a matrix of ones with 3 rows and 4 columns
print(Y)

Z = np.eye(4)    # Create a 4x4 identity matrix
print(Z)

# WE can reshape an array using the reshape() function
A = np.arange(10)    # Create an array with values from 0 to 9
print(A)
A_reshape = A.reshape(2,5)   # Reshape the array to 2 rows and 5 columns
print(A_reshape)

# Accessing elements in an array
print(A_reshape[0,0])   # Access the element in the first row and first column

print(A_reshape[1,2])     # Access the element in the second row and third column

# Modifying elements in an array
A_reshape[0,0] = 99    # Change the element in the first row and first column to 99
print(A_reshape)       # array after modification
print(A)               # array after modification

# Transposing an array

print(A_reshape)       # original array

A_transpose = A_reshape.T   # Transpose the array
print(A_transpose)          # transposed array

# Basic operations on arrays
B = np.array([[20,22,24,26,28],[12,14,16,18,20]])  # Create a 2x5 array
print(B)    # original array

print(A_reshape + B)    # Element-wise addition
print(A_reshape * B)    # Element-wise multiplication
print(A_reshape - B)    # Element-wise subtraction
print(A_reshape / B)    # Element-wise division
print(A_reshape ** 2)   # Element-wise exponentiation
print(A_reshape ** 0.5)  # Element-wise square root
print(A_reshape % B)   # Element-wise modulus

print(np.add(A_reshape,B))         # Element-wise addition using function
print(np.multiply(A_reshape,B))    # Element-wise multiplication using function        
print(np.subtract(A_reshape,B))    # Element-wise subtraction using function
print(np.divide(A_reshape,B))      # Element-wise division using function
print(np.power(A_reshape,2))                 # Element-wise exponentiation using function
print(np.sqrt(A_reshape))                   # Element-wise square root using function    
print(np.mod(A_reshape,B))         # Element-wise modulus using function