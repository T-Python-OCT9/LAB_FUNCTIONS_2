def fun2(x : int,y : int):
    if x < 0 and y < 0:
        print("no problem")
    else:
        print("The numbers should be negative") 


    if x >  y:
        print("x shoud be smaller than y") 


    for i in range(x,y,1):
      print(i)


x=int(input("Enter the first number"))
y=int(input("Enter the secand number"))
fun2(x,y)