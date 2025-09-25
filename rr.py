def divis(number):
    if number % 2 == 0:
        print ("the number is divisible by 2")
        
    elif number % 3 == 0:
        print ("the number is divisible ny 3")
        
    else:
        print ("the number is neither divisible by 2 or 3")
        
num = int(input("enter your number:"))        

divis(num)