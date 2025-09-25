pi = 3.14

def area(radius):
    return pi*r*r
   

def circumference(radius):
    return 2*pi*r



r = float(input("enter your radius:"))
result = area(r)
res = circumference(r)
print("area is", result)
print("circumference is ", res)
    

