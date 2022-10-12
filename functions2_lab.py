'''
Create a function that takes two parameters of type int . The function should do the following:
- Check if all the variables are negative . Else print "The numbers should be negative"
- Check that the first parameter is smaller than the second parameter .
- Using a loop Print all the numbers bettween the smaller int up to the bigger int
'''

def looping(num1:int, num2:int)-> str:
    ''' this function print the numbers from num1 to num2'''

    fun_result : str = "" # create string to store the  final result
    for numbers in range(num1,num2+1):
        fun_result = fun_result + str(numbers) + ". \n" 
    return fun_result


while True:
   num1 = int(input("Enter the first number: ")) 
   num2 = int(input("Enter the second number: "))

   if num1 < 0 and num2 <0: # check if all the variables are negative 
        if num1 < num2:  # Check that the first parameter is smaller than the second parameter
            result = looping(num1,num2)  # call the function
            print(result)
            break
        else: 
            print("The first number should be grater then the second")
   else:
        print('The numbers should be negative')





