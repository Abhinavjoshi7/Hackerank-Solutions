# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
string, n = input().split()
n = int(n)
string = list(sorted(string))
# print(type(string))
# # print(list(combinations(string, n)))

# print(*combinations(string, 1))
for i in range(1, n+1):
    itr = list(combinations(string, i))
    for x in sorted(itr):
        print(*x, sep='')
