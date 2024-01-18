def bank():
    x = int(input("Введите размер вклада (руб.): " ))
    y = int(input("Срок вклада (в годах) : " ))
    z = 10
    sum=(x*1*((z/100)))
    if y==1:
     print(sum)
    else:
     sum_if_more_1_year=sum+(sum*y*((z/100)))
     print(sum_if_more_1_year)     
bank()