def fizz_buzz():
    n=int(input("Введите число: "))
    for x in range (0,n+1):
        if (x % 3 == 0) and (x % 5 == 0):
                 print("FizzBuzz")
        else:
            if(x % 5 == 0):
                print("buzz")
            else:
                if (x % 3 == 0):
                 print("Fizz")
                else:
                    print(x)


fizz_buzz()
