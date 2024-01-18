def month_to_season():
    month=int(input("Введите номер месяца от 1 до 12: "))
    if int(month) == 1 or int(month) == 2 or int(month) == 12:
      print("Зима")
    else:
     if int(month) == 3 or int(month) == 4 or int(month) == 5:
      print("Весна")
     else:
      if int(month) == 6 or int(month) == 7 or int(month) == 8:
       print("Лето")
      else:
       if int(month) == 9 or int(month) == 10 or int(month) == 11:
        print("Осень")
       else:
        print("Нужно ввести номер месяца от 1 до 12")

month_to_season()