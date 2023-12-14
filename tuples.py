if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split())) 
# Enter your code here. Read input from STDIN. Print output to STDOUT
    print(hash(integer_list))
