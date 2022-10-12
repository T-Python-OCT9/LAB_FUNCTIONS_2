def NumberPrint (number1 : int, number2 : int)->int:
    if number1<0 and number2<0:
        if number1<number2:
            for n in range(number1,number2+1):
                print(n)
        else:
            print("shoud number one be smaller than the second")
    
    else:
        print("The numbers should be negative")


numberOne=int(input("inter first number"))
numberTwo=int(input("inter first number"))

NumberPrint(numberOne,numberTwo)