'''
function that print weird if no is odd or in range of 6 to 20 
else print Not Weird
'''
def function():
    number = int(input())
    if (number % 2 != 0 ):
        print("Weird")
    elif (number >=6 and number <= 20):
        print("Weird")
    else:
        print("Not Weird")

    
