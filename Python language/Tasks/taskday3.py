#Task1
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Invalid operator")

#Task2
user_record={
    "kishor":"kishor123",
    "ram":"123kishor",
    "hari":"hari213",
    "huh":"huh123321",
    "lol":"lolol",
    "thikxa":"qwerty123",
    "hora":"hoinahola"
}
username = input("Enter your username: ")
password = input("Enter your password: ")
if username in user_record.keys():
    if password==user_record[username]:
        print("Login Successfull")
    else:
        print("Password Incorrect")
else:
    print("Username not found")