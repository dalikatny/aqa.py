from address import Address
from mailing import Mailing
mailing_to = Mailing('12345','Moscow','Lenina','1','1')
mailing_from=Mailing('54321','Saint Petersburg','Pushkin','2','2')
mailing_to.to_address()
mailing_from.from_address()
