# LAB_FUNCTIONS_2
x= int(input("lease enter first number"))
y= int(input("please enter second number"))
def num (x:int , y:int):
    if x <0 and y <0:
        if x<y:
            for i in range (x,y +1):
                print(i,".")
    else:
        print("the number should be negative")


num(x,y)