def is_year_leap():
    year=input('Введите год:' )
    if (int(year) % 4 == 0):
        print(True)  
    else :
        print(False)  


is_year_leap() 

def is_year_leap1(year1):
    if (int(year1) % 4 == 0):
        print("год",+year1,":",True)
    else :
        print("год",+year1,":",False)
     

is_year_leap1(2023)