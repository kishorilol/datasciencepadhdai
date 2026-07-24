#match case => we match the value of a variable with different cases and execute the corresponding block of code based on the match.
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
#looping statements => for loop, while loop. used to execute a block of code multiple times based on a condition.

#for loop => when we know the number of iterations
#syntax of for loop 
# for iterator in iterable:
    # code to be executed
#iterator => variable that takes the value of the item inside the iterable in each iteration
#iterable => a collection of items that can be iterated over like list, tuple, string, dictionary, set
#iteration => complete execution of a loop
num=[1,2,3,4,5,'kishor',6,7,8,9,10]
for i in num:
    print(i)
#range() => generates a sequence of numbers, used to iterate over with for loop 
#syntax of range() => range(start, stop, step), must be integers, start is inclusive, stop is exclusive, step is optional and default is 1
#if only one argument is passed, it is considered as stop and start is 0 and step is 1
for i in range(5):
    print(i)
#if two arguments are passed, they are considered as start and stop and step is 1
for i in range(1,5):
    print(i)

#break => used to exit the loop when a condition is met
for i in range(1,11):
    if i==5:
        break
    print(i)
#continue => used to skip the current iteration and move to the next iteration when a condition is met
for i in range(1,11):
    if i==5:
        continue
    print(i)
#nested for loop => a for loop inside another for loop
for i in range(1,4):
    for j in range(1,4):
        if i==j:
            continue
        print(f"i={i}, j={j}")
#while loop => when we don't know the number of iterations

# task : execute the calculator program using loops