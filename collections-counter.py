# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
shoes = int(input())
shoes_list = Counter(list(map(int, input().split())))
# print(shoes_list)
# print(shoes_list[5]) access the value with key = 5, it is not an index
cust = int(input())

sum = 0
for i in range(cust):
    size, price = input().split()
    size = int(size)
    price = int(price)
    if shoes_list[size] > 0:
        sum = sum + price
        shoes_list[size] -=1
print(sum)
