# generating random data

#importing numpy
import numpy as np

# generatimg random data in a vector form
x = np.random.normal(loc = 0, scale = 1, size = 10)      #loc is mean(0), scale is standard deviation(1) and size of data is 10
print("x: ",x)

# for each time we run the code, we will get different random numbers

x = np.random.normal(loc = 0, scale = 1, size = 10)
print("x: ",x)

# to get the same random numbers each time we run the code, we can set the seed
rng = np.random.default_rng(13033)  # setting the seed
# 1303 acts a key to generate the same random numbers each time we run the code
x1 = rng.normal(size = 10)
print(' x1: ',x1)
rng2 = np.random.default_rng(13033)  # setting the seed
x2 = rng2.normal(size = 10)
print(' x2: ',x2)   # generating random numbers using the seed

# we can create an array by adding an independent N(50,1) random variable to each element of a vector
# of integers from 1 to 10

y = np.random.normal(loc = 50, scale = 1, size = 10) + x
print("y: ",y)

# we can also use the seed to generate the same random numbers each time we run the code
rng = np.random.default_rng(13033)
y1 = rng.normal(loc=50, scale=1, size=10) + x1
print("y1:", y1)

rng2 = np.random.default_rng(13033)  # reset again
y2 = rng2.normal(loc=50, scale=1, size=10) + x2
print("y2:", y2)

#finding the mean, variance and standard deviation of the generated data
rng = np.random.default_rng(42)
z = rng.standard_normal(10) # fixed mean 0 and standard deviation 1 not dynamic for mean and std
print("z: ",z)

#Mean represents the central value of the data
#Variance measures the spread of the data around the mean
#Standard Deviation is the square root of the variance and represents the average distance of each data point from the mean

print("Mean of z: ", np.mean(z))   # mean of z mean = 1/n * sum(zi)
print("Population Variance of z: ", np.var(z))  # population variance of z var = 1/n * sum((zi - mean)^2)
print("Sample Variance of z: ", np.var(z, ddof = 1))  # sample variance of z var = 1/(n-1) * sum((zi - mean)^2)
print("Standard Deviation of z: ", np.std(z))  # standard deviation of z std = sqrt(var)
print("Sample Standard Deviation of z: ", np.std(z, ddof = 1))  # sample standard deviation of z std = sqrt(var)

# finding the correlation coefficient between x and y
# Correlation coefficient measures the strength and direction of the linear relationship between two variables
# it ranges from -1 to 1
# 1 indicates a perfect positive linear relationship x increases, y increases
# -1 indicates a perfect negative linear relationship x increases, y decreases
# 0 indicates no linear relationship x and y are independent
print("Correlation Coefficient between x and y: ", np.corrcoef(x, y))  # correlation coefficient between x and y

# matix data

M = rng.standard_normal((10,3))  # generating a 10x3 matrix of random numbers
print("M: ",M)
print("Mean of M: ", np.mean(M, axis = 0))  # mean of each column
print("Mean of M: ", np.mean(M, axis = 1))  # mean of each row
print("Variance of M: ", np.var(M, axis = 0))  # variance   of each column
print("Variance of M: ", np.var(M, axis = 1))  # variance of each row
print("Standard Deviation of M: ", np.std(M, axis = 0)) # standard deviation of each column
print("Standard Deviation of M: ", np.std(M, axis = 1)) # standard deviation of each row