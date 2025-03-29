from smartphone import Smartphone

cataloge = [
    Smartphone("Apple", "iPhone 15 Pro", "+79680035581"),
    Smartphone("Samsung", "Galaxy A", "+9660035581"),
    Smartphone("Motorola", "Edge 20", "+79030035581"),
    Smartphone("Huawei", "Mate XT", "+79990035581"),
    Smartphone("Nokia", "6300 Silver", "+79060035581")
]

for smartphone in cataloge:
    print(f"{smartphone.phonemark} - {smartphone.phonemodel} - {smartphone.number}")