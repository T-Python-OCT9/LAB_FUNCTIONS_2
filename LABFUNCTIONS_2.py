'''
 - Check if all the variables are negative . Else print "The numbers should be negative"
- Check that the first parameter is smaller than the second parameter .
- Using a loop Print all the numbers bettween the smaller int up to the bigger int . 

Note : Ask the user for the 2 numbers . (use input) 

def tringal(number:int):

num_input=int(input("what is the paramet"))
tringal(num_input)
'''





#var1 = int(input("what is the variable input1"))
#var2= int(input("what is the variable input2"))
#variable_input1= var1
#variable_input2= var2

variable_input1=int(input("what is the variable input1"))
variable_input2=int(input("what is the variable input2"))

def variables (variable_input1:int , variable_input2:int ):
   if variable_input1 < 0 and variable_input2 < 0:
     if variable_input1 < variable_input2:
        for i in range(variable_input1,variable_input2):
            print(i)
   else :
    print ("The numbers should be negative")
     

#variables(-5,-5)
variables(variable_input1,variable_input2)        
