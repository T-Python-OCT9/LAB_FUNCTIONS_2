

def my_fun(x:int,y:int):
    for n in range(x,y,+1):
        print(n)

while True:
    x = int(input("Enter the first num: "))
    y = int(input("Enter the 2nd num: "))
    if x <0 and y <0 and x<y:
        my_fun(x,y)
        break
    else:
        print("Please Try Again")
        continue
