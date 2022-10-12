
'''
# LAB_FUNCTIONS_2


## Create a function that takes two parameters of type int . The function should do the following:
- Check if all the variables are negative . Else print "The numbers should be negative"
- Check that the first parameter is smaller than the second parameter .
- Using a loop Print all the numbers bettween the smaller int up to the bigger int . 

Note : Ask the user for the 2 numbers . (use input)

#### Example : when we call the function with parameter1 =  -15 , and parameter2 = -4 ,
#  the printed output should look like this:
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




def checkVal(num1 : int , num2:int) -> str:
    if not num1 < 0 and not num2 < 0:
        return "The numbers must be negative"
    
    if not num1 < num2:
        return "The first number must smaller than the second number"
    

    result : str = ""
    for n in range(num1, num2+1):
        result = result + str(n) + ". \n"
    

    return result
        
    


num1 = int(input("please entre first  number: "))
num2 = int(input("please entre second  number: "))

result = checkVal(num1,num2)
print(result)