def month_to_season(number):
    if number in [12, 1, 2]:
        print("Зима")
    elif number in [3, 4, 5]:
        print("Весна")
    elif number in [6, 7, 8]:
        print("Лето")
    elif number in [9, 10, 11]:
        print("Осень")
    else:
        print("Некорректный номер месяца")
    
month_to_season (5)