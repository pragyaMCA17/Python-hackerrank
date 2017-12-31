def second_lowest():
    x=[]
    students=[]
    for _ in range(int(input())):     #number of students
        name = input()                #name of student
        score = float(input())        #number of that student
        x.append(score)
        students.append([name,score])
    x.sort()
    students.sort()
    element=x[0]
    for i in range(len(students)):
        if element!=x[i]:
            element=x[i]
            break
    for i in range(len(students)):
        if element==students[i][1]:
            print(students[i][0])
