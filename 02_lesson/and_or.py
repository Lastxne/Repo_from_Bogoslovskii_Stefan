# user_login = "abvgd"
# user_pass = "pass"

# login = input("Login:")
# password = input("Password:")

# if login == user_login and password == user_pass:
#     print("Secret is open")
# else:
#     print("Locked")

crit = "red"
crit2 = "lock"

color = input("Color: ")
feature = input("Feature: ")

if color == crit or feature == crit2:
    print("Buy it!")
else:
    print("Don't buy it!")