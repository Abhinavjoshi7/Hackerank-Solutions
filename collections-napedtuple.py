# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
total_marks = 0
students = namedtuple('student', input().split())
for i in range(n):
    ID, MARKS, NAME, CLASS = input().split()
    student = students(ID, MARKS, NAME, CLASS)
    # print(*student.MARKS)
    total_marks += int(student.MARKS)
print('{:.2f}'.format(total_marks / n))
