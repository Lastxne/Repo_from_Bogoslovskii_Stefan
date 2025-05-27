# employee_list = ["Jonh Snow", "Piter Pen", "Drakula", "IvanIV", "Moana", "Juilet"]

# print(employee_list[1] + ", " + employee_list[-2])

# def dev_by_three(number):
#     return "Yes" if number % 3 == 0 else "No"

# num = int(input("Введите число: "))
# result = dev_by_three(num)
# print(f"Число {num} делится на 3? - {result}")

# import math

# def min_boxes(count):
#     return math.ceil(count / 5)

# counts = int(input("Введите количество товаров: "))
# print(f"Минимальное количество коробок: {min_boxes(counts)}")


# n = int(input("Введите число:"))


# def check_divisibility(n):
#     for i in range(1, n + 1):
#         if i % 4 == 0:
#             print(f"{i} - Делится и на 2, и на 4")
#         elif i % 2 == 0:
#             print(f"{i} - Делится на 2, но не на 4")
#         else:
#             print(i)


# check_divisibility(n)

# def quarter_of_year(month):
#     if 1 <= month <= 3:
#         return "I квартал"
#     elif 4 <= month <= 6:
#         return "II квартал"
#     elif 7 <= month <= 9:
#         return "III квартал"
#     elif 10 <= month <= 12:
#         return "IV квартал"
#     else:
#         return "Неверный номер месяца"

# try:
#     month = int(input("Введите номер месяца (1-12): "))
#     print(quarter_of_year(month)) 
# except ValueError:
#     print("Пожалуйста, введите целое число от 1 до 12.")