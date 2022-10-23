
N = int(input("please entre first  number: "))
O = int(input("please entre second  number: "))

def checkVal(N : int , O:int) -> str:
    if not N < 0 and not O < 0:
        return "The numbers must be negative"
    if not N < O:
        return "The first number must smaller than the second number"
    result : str = ""
    for n in range(N, O+1):
        result = result + str(n) + ". \n"
    return result

result = checkVal(N,O)
print(result)
