#task1: caculator with loop
loop_count=int(input("Enter the number of calculations you want to perform: "))
for i in range(loop_count):
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    choice=input("enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: ")
    match choice:
        case "1":
            print(f"{num1} + {num2} = {num1 + num2}")
        case "2":
            print(f"{num1} - {num2} = {num1 - num2}")
        case "3":
            print(f"{num1} * {num2} = {num1 * num2}")
        case "4":
            print(f"{num1} / {num2} = {num1 / num2}")
        case _:
            print("Invalid choice")