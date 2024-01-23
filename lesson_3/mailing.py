from address import Address

class Mailing(Address):
    
    def __init__(self, index, city, street, build, flat,):
        super().__init__(index, city, street, build, flat)
        cost = 300
        track = 123456789
        self.index=index
        self.city=city
        self.street=street
        self.build=build
        self.flat=flat
        self.cost=cost
        self.track=track
    def to_address(self):
        print("Otpravlenie v: ",self.city,"Pochtovyi index: ",self.index,"ulitsa: ",self.street, "dom:", self.build, "kvartira: ", self.flat, "track nomer: ", self.track,"Stoimost' otpravleniya: ", self.cost )
    def from_address(self):
        print("Otpravlenie iz: ", self.city, "Pochtovyi index: ",self.index,"ulitsa: ",self.street, "dom:", self.build, "kvartira: ", self.flat,"track nomer: ", self.track,"Stoimost' otpravleniya: ", self.cost )