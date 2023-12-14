if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    
    query_name = input()
    average_marks = 0
    total_marks = 0
    # #acess the dictionary 
    # print(student_marks["Krishna"])
    # print(student_marks.keys())
    # for i in student_marks:
    #     print (i, student_marks[i])
    for i in student_marks:
        if query_name == i:
            marks_list_lenght = len(student_marks[i])
            total_marks = sum(student_marks[i])

    average_marks = total_marks / marks_list_lenght
    print(format(average_marks, ".2f"))
            
