import math

def square(side):
    return math.ceil(side * side)

square2 = int(input("Введите длину стороны: "))
print(f"Площадь ровна: {square(square2)}")