# Task
# You are given an integer, , on a single line. The next line contains  space-separated integers. Create a tuple, , of those  integers, then compute and print the result of hash().

# Note: hash() is one of the functions in the __builtins__ module.

# Input Format

# The first line contains an integer,  (the number of elements in the tuple).
# The second line contains  space-separated integers describing .

# If the inputs are given on one line separated by a space character, use split() to get the separate values in the form of a list:

# >> a = raw_input()
# 5 4 3 2
# >> lis = a.split()
# >> print (lis)
# ['5', '4', '3', '2']
# If the list values are all integer types, use the map() method to convert all the strings to integers.

# >> newlis = list(map(int, lis))
# >> print (newlis)
# [5, 4, 3, 2]



# map function here converts string y into number of integers
x = raw_input()
y = raw_input()
print hash(tuple(map(int, y.strip().split(" "))))
