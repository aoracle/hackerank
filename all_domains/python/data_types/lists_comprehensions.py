# Enter your code here. Read input from STDIN. Print output to STDOUT
# CRUDE way of solving problem
# x = input()
# y = input()
# z = input()
# n = input()

# a = []

# x_values = [x for x in range(x+1)]
# y_values = [y for y in range(y+1)]
# z_values = [z for z in range(z+1)]
# #print x_values

# for i in x_values:
#     for j in y_values:
#         for k in z_values:
#             if i+j+k == n:
#                 pass
#             else:
#                 a.append((i,j,k))
# print a

#range (x,y) -- This produces values between x and y

x, y, z, n = int(input()), int(input()), int(input()), int(input())
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])
