def bank1():
  x=int(input("Введите сумму депозита: "))
  y=int(input("Введите срок депозита: "))
  z=0.1
  for i in range(y):
    x+=x*z
  print(x)

bank1()