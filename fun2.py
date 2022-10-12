## Using a loop Print all the numbers bettween the smaller int up to the bigger int . 
from ast import Break


x= int(input("type the first number, should be negative number"))
y= int(input("type the seconf, should be negative number"))

def fun (x:int , y:int)->int:
    if (x < 0 and y < 0):
        if (x < y):
            for i in range (x,y+1):
              print(i,".")
        else:
              print("the number is smaller than the second num")  
    else:
          print("The numbers should be negative")
        
fun(x,y)