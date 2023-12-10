if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    dict_arr = dict.fromkeys(arr) #convert to dict as dict has no duplicates
    list_arr = list(dict_arr) #convert back to list
    list_arr.sort() # sort
    max_item = (max(list_arr)) #get the max
    list_arr.remove(max_item) #remove the max item  
    max_item = (max(list_arr)) #get the max item again
    print(max_item)
    
    
            
