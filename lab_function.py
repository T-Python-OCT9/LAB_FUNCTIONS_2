def check_negative(x: int, y: int) -> int:
    if x < 0 and y < 0:
        if x < y:
            for i in range(x, y + 1):
                print(i, ".")
    else:
        print("The numbers should be negative")


x = int(input("please inter the num 1 ="))
y = int(input("please inter the num 2 ="))
check_negative(x, y)
