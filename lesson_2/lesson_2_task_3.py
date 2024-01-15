def square(side):
     if type(side) is float:
         side = round(side) 
         print(side ** 2)
     else:
         print(side**2)

square(5) 
        
def square():
     side=input("Введите сторону: ")
     side = round(float(side))
     print(int(side) **2)

square()

def square():
    side=float(input("Введите сторону : "))
    if type(side) is float:
        side=round(side)
        print(side**2)
    else:
        print(side**2)

square()