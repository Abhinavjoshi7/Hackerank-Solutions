arry_len, set_len = input().split()
my_arr = input().split()
set_a = set(input().split())
set_b = set(input().split())

happiness = 0

for i in my_arr:
    if i in set_a:
        happiness += 1
    if i in set_b:
        happiness -= 1

print(happiness)
