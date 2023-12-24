# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
set_a = set(map(int, input().split()))
m = int(input())
set_b = set(map(int, input().split()))

set_c = set()
# print(*set_a)
# print(*set_b)
# print(type(set_a))
# print(set_a.union(set_b))
for i in sorted(set_a.difference(set_b)):
    set_c.add(str(i))
       
for i in sorted(set_b.difference(set_a)):
    set_c.add(str(i))
    
for i in sorted(set_c, key=int):
    print(i)
