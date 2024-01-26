from mailing import Mailing
from address import Address

mail=Mailing(Address(1234567,'Chita','bogomyaghkova',12,12),
             Address(756656,'Moscow','Lesnaya',12,122),
             122,
             12345678)

print(
'Отправление',mail.track , 'из', mail.to_address.index, mail.to_address.city,mail.to_address.street,mail.to_address.build,mail.to_address.flat,  'в', mail.from_address.index, mail.from_address.city, mail.from_address.street, mail.from_address.build ,mail.from_address.flat,'.' 'Стоимость', mail.cost, 'рублей..'
)

