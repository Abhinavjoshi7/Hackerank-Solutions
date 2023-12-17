def print_rangoli(size):
    # your code goes here
    str_len = (size - 1) * 4 + 1
    #gives us all the alphabets, 
    alphabets = list(map(chr, range(97, 123)))
    #create a full list upto n 
    # alphabets[size-1::-1] gives us alphabets starting at last alphabet and giving us upto the the first aplphabet, ::-1 gives us from the reverse order 
    # alphabets[1:size] gives us the rest of the elements execpt the first letter upto the end of list
    full_list = '-'.join(alphabets[size-1::-1] +alphabets[1:size]).center(str_len, '-')
    # print(full_list)
    for i in range(1, size):
        upper_list = '-'.join(alphabets[size-1: size-i:-1] + alphabets[size-i:size]).center(str_len, '-')
        print(upper_list)
    print(full_list)
    for i in reversed(range(1, size)):
        lower_list = '-'.join(alphabets[size-1: size-i:-1] + alphabets[size-i:size]).center(str_len, '-')
        print(lower_list)
       
    
