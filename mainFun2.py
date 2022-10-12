#the sconed func lab

def Negative_nums(user_input1:int,user_input2:int)-> str:
    '''this Function take two prameters and check if it negative and print it ascending
    '''
    #to check the conditions 
    if  not user_input1 < 0 and not user_input2 < 0:
        return "The numbers should be negative"
        if user_input1 < user_input2:
            return "The 1st number should be smaller than the2nd number"
    result : str = ""
    for n in range(user_input1, user_input2, +1):
        result = result + str(n) + ". \n"
    return result
user_input1 = int(input("Enter the 1st negative number : "))
user_input2 = int(input("Enter the 2nd negative number : "))
#to print the result of the user input...

result= Negative_nums(user_input1, user_input2)
print(result)



      
   