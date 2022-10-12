


def func1(x : int, y: int ) -> str:
    if x<0 and y<0 :
        if x<y:
            for i in range(x,y +1):
                print(i,".")
    else:
        print("The numbers should be negative")
   
    
x = int(input(" enter number first "))
y = int(input(" enter number second "))
func1(x,y)