firstNum = int (input ("please choose the first number"))
seconedNum = int (input ("please choose the seconed number"))
def a (firstNum , seconedNum):
    if firstNum and seconedNum < 0 :
      if  firstNum < seconedNum :
        for i in range (firstNum , seconedNum):
           print (i)
      else :
        print ("The first number should be smaller than seconed number ")
           
    else :
        print ("The Numbers should be negative")


a (firstNum , seconedNum)

    