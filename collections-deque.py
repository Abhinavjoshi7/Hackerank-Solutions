# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(input())
data = deque()
# print(data)
# print(n)
for i in range(n):
    commands = input().split()
    if commands[0] in ("clear", "pop", "popleft", "reverse"):
        x = str(commands[0])
        getattr(data, x)()
    else:
        x = str(commands[0])
        y = int(commands[1])
        getattr(data, x)(y)
        # getattr(data.commands[0](commands[1]))
print(" ".join(map(str, data)))
