class User:
    first_name = 'dalik'
    last_name = 'dalikatny'
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    def Name(self):
        print("Моё имя: ", self.first_name)
    def LastName(self):
        print("Моя фамилия: ", self.last_name)
    def fullName(self):
        print("Моё полное имя: ", self.first_name, self.last_name )    


# Slava=User("Slava","Dalikatny")
# Slava.Name()
# Slava.LastName()
# Slava.fullName()