def bank1():
  x=int(input("Введите сумму депозита: "))
  y=int(input("Введите срок депозита: "))
  z=0.3444
  for i in range(y):
    x+=x*z
  sum=round(x,4)
  print(sum)

bank1()