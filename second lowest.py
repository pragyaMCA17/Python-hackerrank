def second_lowest():
    x=[]
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
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
