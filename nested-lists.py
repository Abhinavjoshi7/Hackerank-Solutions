if __name__ == '__main__':
    data = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name,score])
        score_list.append(score)
        
    grades_set = set(score_list)
    grades_set_sorted = sorted(grades_set)
    lowest_marks = grades_set_sorted[1]
    name_list = []
    for grades in data:
        if lowest_marks == grades[1]:
                name_list.append(grades[0])
    #to print the list    
    # for i in data:
    #     print(i[0], i[1])
    name_list =    sorted(name_list)
    for name in name_list:
        print(name)
