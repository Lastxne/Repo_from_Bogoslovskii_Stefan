rate_is_str = input("Оцените нашу работу от 1 до 5:")
rate = int(rate_is_str)

if (rate < 1):
    rate = 1

if (rate > 5):
    rate = 5

feedback = ''

if rate == 1:
    feedback = input("Расскажите ппочему 1:")
elif rate == 2:
    feedback = input("расскажите почему 2:")
elif rate == 3:
    feedback = input("расскажите почему 3:")
elif rate == 4:
    feedback = input("расскажите почему 4:")
else:
    feedback = print(" thanks for 5")
