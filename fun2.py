## Using a loop Print all the numbers bettween the smaller int up to the bigger int . 
from ast import Break


x= int(input("type the first number, should be negative number"))
y= int(input("type the seconf, should be negative number"))

def fun (x:int , y:int)->int:
    
    if x < 0 and y < 0:
        if (x < y):
            print(x,y)
        elif (x>y):
           Break
    else:
        print("The numbers should be negative")
        


print(fun(x,y))