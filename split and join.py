def split_and_join(line):
    line=line.split(" ")
    line=  "-".join(line)
    return line

if__name__=="__main__" :
   # line ="This is an example of split and join"
    line= input("Enter the line : ")
    print("Line , before function call: ",line)
    print("Line , after function call :",split_and_join(line))
    
