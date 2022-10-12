# this is lab4 - 12 oct- functions 2 - ghadah alahrbi 

def Lab4 (x : int , y: int ):

    if x >=0 and y >=0 or x>y : 
        print("The numbers should be negative or the first number is grater than second one , try again later!")
          
    return x,y
        
    


x , y= Lab4(int(input("enter the first integer ")),int(input("enter the second integer ")))

for n in range(x,y+1):
             print(n ,".")
