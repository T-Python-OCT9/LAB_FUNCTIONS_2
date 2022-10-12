''' Create a function that takes two parameters of type int . The function should do the following:
- Check if all the variables are negative . Else print "The numbers should be negative"
- Check that the first parameter is smaller than the second parameter .
- Using a loop Print all the numbers bettween the smaller int up to the bigger int . 

Note : Ask the user for the 2 numbers . (use input)

# Example : when we call the function with parameter1 =  -15 , and parameter2 = -4 ,
#  the printed output should look like this:'''

def  Two_para_func(first : int, second : int) -> int:
    if first and second < 0 :
        if first < second :
            for x in range(first, second+1, +1):
                print(x) 
        else:
            print("Second parameter is smaller than first parameter")   
    else:
        print("The number should be negative")
        
         

print("please enter 2 int numbers")

first_input: int = int(input())
second_input: int = int(input())

Two_para_func(first=first_input, second=second_input)           
