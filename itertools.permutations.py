# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
str, n = input().split()
n = int(n)
per = list(permutations(sorted(str), n))

for i in per:
    print(''.join(i))
