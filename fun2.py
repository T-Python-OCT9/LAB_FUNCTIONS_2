def function(num : int , num2 : int):
    if (num and num2)<0:
        print("The numbers negative")
        if num < num2:
            print("first parameter is smaller than the second parameter")
            for i in range(num,num2+1,1):
                print(i , end=".")
                print()
        else:
            print("first parameter is not smaller")

    else:
        print("The numbers should be negative")


number = int (input("Enter the first number: "))
number2 = int (input("Enter the second number: "))
function(number,number2)

