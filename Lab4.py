


def Functions_2(x: int , y :int) :
    x= int(input("Please give a nagative number:"))  
    y= int(input("Please give the second nagative number:"))
    
    for i in range (x,y):
        if x  < 0 and y < 0  and x < y :
            print (i)
        else:
            print ("enter a nagtive number")
        
print(Functions_2(1,1))