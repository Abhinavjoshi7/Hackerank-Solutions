if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    data = []
    data = list(arr)
    data.sort()
    data_unique = set(data)
    data_unique_list = list(data_unique)
    max_item = max(data_unique_list)
    data_unique_list.remove(max_item)
    print(max(data_unique_list))
    
