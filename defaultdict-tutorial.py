# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = map(int, input().split())
groupA = defaultdict(list)
for i in range(n):
    # take characters from user input and store them in s variable
    s=input().rstrip()
    # for each characters key, append the values as their position 
    groupA[s].append(i+1)
    
# print(groupA)
# print(groupA['a'])
for j in range(m):
    t=input().rstrip()
    # now check if the t is in the dictionary
    if t in groupA:
        # groupA[t] print the list values of that key 
        print(' '.join(map(str, groupA[t])))
    else:
        print('-1')
