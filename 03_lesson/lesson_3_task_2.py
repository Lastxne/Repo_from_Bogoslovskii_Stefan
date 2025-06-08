from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14", "+79999999999"),
    Smartphone("Samsung", "Galaxy S23", "+79988888888"),
    Smartphone("Google", "Pixel 7", "+79977777777"),
    Smartphone("OnePlus", "OnePlus 11", "+79966666666")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
