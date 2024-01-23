class User:
    age = 23;
    country = "russia";
    city = "Chita";

    def __init__(self, name):
        print(name, ":  ya sozdalsa") 
        self.username=name        

    def SayName(self):
        print("Menya zovut", self.username)

    def SayHowOldAreYou(self):
        print("I'm is", self.age, "years old")

    def SayWhereAreYouFrom(self):
        print("I'm from", self.country, self.city)

    def setAge(self, newAge):
        self.age=newAge

    def addCard(self, card):
        self.card = card

    def getCard(self):
        return self.card