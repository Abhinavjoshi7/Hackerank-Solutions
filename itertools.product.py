# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))
print(*list(product(list_A, list_B)))
