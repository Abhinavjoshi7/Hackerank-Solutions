# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 
a = int(input())
b = int(input())

# since bm = mc, it is an isocelos triangle.Then Angle MBC = MCB
# Now tanO = Opp/Adjc 
# tanO = AB / BC 
# O = tan(invrs) BM/BC
theta = math.atan(a/b)
print(round(math.degrees(theta)), chr(176), sep='')
# print(new_dimension, b, c_half)
