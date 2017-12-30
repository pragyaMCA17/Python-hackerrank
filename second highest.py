def second_highest():
    n = int(input())      #no of inputs
    arr = list(map(int, input().split())) #input list
    arr.sort(reverse=True)
    element=arr[0]
    for i in range(len(arr)):
        if element!=arr[i]:
            print(arr[i])
            break
