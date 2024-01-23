class Card:
    number = '0000 0000 0000 0000'
    validDate = '01/99'
    holder = 'Unknown'
    bank = 'Sber'

    def __init__(self,number, validDate, holder,bank):
        self.holder=holder
        self.number=number
        self.validDate=validDate
        self.bank=bank


    def pay(self,amount):
        print("from card", self.number, "bylo spisano", amount)