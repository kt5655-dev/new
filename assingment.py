def main ():
 n = float(input("enter your current balance ammount:"))
 m = float(input("enter your transaction s.no - 1.WITHDRAWAL, enter negative value or""\n 2.DEPOSIT, add positive value:"))
 z = float(input("enter your ammount: "))
 x = n + z
 def transaction_validator(cab, tr):
    if m == 1:
       print (x)
    if m == 2:
       print (x)
    if z == 0:
        print("it is invalid")
    elif x < 0:
        print ("it is invalid")
 
 transaction_validator(n,z)

 def account_category_checker():
    if x >= 100000:
       print("Category: Premium ")
    elif 99999>x>50000:
       print("Category: Gold")
    elif 49999>x>10000:
       print ("Category: Standard")
    elif 10000>x:
       print ("Category: Basic")

 account_category_checker()
    
   

main()