# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
print(is_even(num))

# Print out "Even!" if the number is even. Otherwise print "Odd"

if is_even(num) == True:
    print('Even!')
else:
    print('Odd')

# Write a function that doubles the value of an integer

#YOUR CODE HERE
def double(n):
    return n*2

my_int = 10
double(my_int)

print(my_int)

# find resource on passing by reference vs passing by value

# prints 10 --> we did not change the original value
# passed by VALUE, not by reference
# with integers, python passes by value

# this passes list by value, by creating a list comprehension:
# def double_list(l):
#     return [i * 2 for i in l]

# modify original list directly with a for loop
def double_list(l):
    for i in range(len(l)-1):
        l[i] *= 2
    return l

my_list = [2, 7, 23, 11, 4]
double_list(my_list)

# how do we NOT modify?? use a slice!
# double_list(my_list[:])

print(my_list)

def capitalize_name(name): # first last
    full_name = name.split(" ")
    name = full_name[0][0:1].upper() + full_name[0][1:] + " " + full_name[1][0:1].upper() + full_name[1][1:]
    print(name)
    # name = name[0:1].upper() + ??? + name[].upper() + name[?:]

my_name = "bruce cabanayan"
capitalize_name(my_name)
print(my_name)
