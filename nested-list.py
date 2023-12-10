if __name__ == '__main__':
    data = []
    grade =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name,score])
        grade.append(score)
        
grade = set(grade) #remove null as a set cannot have nulls 
grade_sorted = sorted(grade)
second_grade = grade_sorted[1]
#print(second_grade)
name =[]
for i in data:
    if second_grade == i[1]: #i[1] is the scores of students, i[0] = name, i[1] = score
        name.append(i[0]) #append the name 
        
#now we have two names, we need to sort them alphabetically as per the question 
name = sorted(name)
for i in name:
    print(i)        
