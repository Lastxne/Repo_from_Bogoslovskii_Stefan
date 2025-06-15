from address import Address
from mailing import Mailing

from_address = Address('123456', 'Moscow', 'Tverskaya', '1', '10')
to_address = Address('654321', 'Saint Petersburg', 'Nevsky', '2', '20')

mail = Mailing(to_address, from_address, 100, 'TRACK1234567890')

print(
    f"Отправление {mail.track} из {mail.from_address.index}, "
    f"{mail.from_address.city}, {mail.from_address.street}, "
    f"{mail.from_address.building} - {mail.from_address.flat} "
    f"в {mail.to_address.index}, {mail.to_address.city}, "
    f"{mail.to_address.street}, {mail.to_address.building} - "
    f"{mail.to_address.flat}. Стоимость {mail.cost} рублей.")
