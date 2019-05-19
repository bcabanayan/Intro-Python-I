"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = []

# for loop

# for x in range(1,6,1):
#     y.append(x)

y = [y + 1 for y in range(5)]

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = []

# for loop

# for x in range (10):
#     y.append(x**3)

y = [y ** 3 for y in range(9)]

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [a[i].upper() for i in range(len(a))]

# for loop

# for i in range(len(a)):
#     y.append(a[i].upper())

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = []

# for loop

# for i in range(len(x)):
#     if int(x[i]) % 2 == 0:
#         y.append(int(x[i]))

y = [int(x[i]) for i in range(len(x)) if int(x[i]) % 2 == 0]

print(y)

# all cubes of 0 - 20 that are also divisible by 3

y = [i ** 3 for i in range(21) if i ** 3 % 3 == 0]
print(y)

# don't forget square brackets
# any list comprehension can be written as a for loop