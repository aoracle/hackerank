# Task
# Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

# Input Format

# The first line of input contains an integer, .
# The second line contains  space-separated integers.
# The third line contains an integer, .
# The fourth line contains  space-separated integers.



input()
a = set(map(int,raw_input().split()))
input()
b = set(map(int,raw_input().split()))
c = a.symmetric_difference(b)
for n in sorted(list(c)):
	print n
