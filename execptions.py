# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for i in range(t):
    x, y = input().split()
    try:
        a = int(x)
        b = int(y)
        sum = (a/b)
        print(int(sum))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except Exception as e:
        print("Error Code:", e)
