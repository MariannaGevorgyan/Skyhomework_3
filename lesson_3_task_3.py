from address import Address
from mailing import Mailing
from_address = Address("171407", "Moscow", "Tverskaya", "17","7")
to_address = Address("171409", "Saint-Petersburg", "Kazanskaya", "17", "7")
mailing= Mailing(to_address, from_address, "20000", "Skoda745KK46")
print(mailing)

