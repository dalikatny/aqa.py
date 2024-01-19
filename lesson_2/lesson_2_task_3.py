def square():
    import math
    side=float(input("Введите сторону : "))
    if type(side) is float:
        side=math.ceil(side)
        print(side**2)
    else:
        print(side**2)

square()