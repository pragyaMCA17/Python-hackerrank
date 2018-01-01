import math
def percentage():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sumation=student_marks[query_name]
    percentage=(sum(sumation)/len(sumation))
    ans=(round(percentage,2))
    frac, whole = math.modf(ans)
    for i in range(10):
        if frac ==i*.1 :
            print(ans,"0",sep="")
            break
        elif frac <0.1 :
            print(ans,"0",sep="")
            break
    else:
        print(ans)
    
