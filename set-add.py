# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
cities = set()
for i in range(n):
    city = input()
    cities.add(city)
    
print(len(cities))
