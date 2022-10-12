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