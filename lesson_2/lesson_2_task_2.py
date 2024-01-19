def is_year_leap():
    year=input('Введите год:' )
    if (int(year) % 4 == 0):
        print(True)  
    else :
        print(False)  


is_year_leap() 