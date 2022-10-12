def check_negative(x: int, y: int):
    if x >= 0 and y >= 0 or x > y:
        print("The numbers should be negative")
    else:
        for i in range(x, y):
            if i > 0:
                print(i)


x = int(input("please inter the num 1 ="))
y = int(input("please inter the num 2 ="))
check_negative(x, y)
