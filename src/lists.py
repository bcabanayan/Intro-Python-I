# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# concatenate arrays, rather than add entire array into last position of list
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# value to remove!
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# index first, then value
x.insert(5, 99)
print(x)

# Print the length of list x
print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
# javascript: for (i = 0; i < arr.length; i++ ) { etc }
# python:
# don't forget the colon!
for i in range(0 , len(x)):
    print(x[i]*1000)
# more like a python for each
for number in x:
    print(number*1000)

