'''# LAB_FUNCTIONS_2


## Create a function that takes two parameters of type int . The function should do the following:
- Check if all the variables are negative . Else print "The numbers should be negative"
- Check that the first parameter is smaller than the second parameter .
- Using a loop Print all the numbers bettween the smaller int up to the bigger int . 

Note : Ask the user for the 2 numbers . (use input)

#### Example : when we call the function with parameter1 =  -15 , and parameter2 = -4 , the printed output should look like this:
-15.   
-14.  
-13.  
-12.  
-11.  
-10.  
-9.  
-8.  
-7.  
-6.  
-5.  
-4.  
'''
x  =int (input("please inter first number:"))
y  =int (input("please inter seconde number:"))

def coun(num1 :int  ,num2:int ):
    if num1 <0 and num2 <0 :
        while num1 <num2:
            for i in range (num1 ,num2+1):
                print()
        else:
            for i in range (num2 ,num1+1):
                print (i)
    else:
        print ("The numbers should be negative")
    

coun(x,y)
