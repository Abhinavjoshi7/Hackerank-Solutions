if __name__ == '__main__':
    N = int(input())
    data = []
    input_list = []
    for x in range(N):
        input_list = input().split() #add the items to the list example ['insert', '0', '5']
        if input_list[0].lower() == 'insert':
            #insert returns 'None', it does not return a new list;
            data.insert(int(input_list[1]), int(input_list[2]))
        if  input_list[0].lower() == 'remove':
            data.remove(int(input_list[1]))
        if  input_list[0].lower() == 'append':
            data.append(int(input_list[1]))
        if  input_list[0].lower() == 'sort':
            data.sort()    
        if  input_list[0].lower() == 'pop':
            data.pop()
        if  input_list[0].lower() == 'reverse':
            data.reverse()
        if input_list[0].lower() == 'print':
            print(data)
            
            
