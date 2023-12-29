# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
items = OrderedDict()
for i in range(n):
    st = input().split()
    item_name = ' '.join(st[:-1])
    item_price = int(st[-1])
    # print(item_name, item_price)
    if item_name in items:
        item_price += items[item_name]
    items[item_name] = item_price

for key, value in items.items():
    print(key, value)
        
