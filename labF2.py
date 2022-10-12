

def checkNum(Num1 : int , Num2:int) -> str:
    if not Num1 < 0 and not Num2 < 0:
        return "The numbers must be negative"
    
    if not Num1 < Num2:
        return "The first number must smaller than the second number"
    

    result : str = ""
    for n in range(Num1, Num2+1):
        result = result + str(n) + "\n"
    

    return result
    
Num1 = int(input("please entre first  number: "))
Num2 = int(input("please entre second  number: "))

result = checkNum(Num1,Num2)
print(result)
