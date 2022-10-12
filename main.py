num1= int(input("please enter first number"))
num2= int (input("please enter first number"))


def check(num1 :int ,num2:int )->int:
    if num1<0 and num2<0 :
       if num1<num2:
        for i in range(num1,num2 +1):
            print(i ,".")



    else:
        print("The numbers should be negative")


check(num1,num2)
