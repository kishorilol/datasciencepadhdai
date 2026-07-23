#indexing => accessing element from list 
list1=["kishor","rojanc","rojans","mission","resh","nioz","nishant","kapil"]
#index always starts from 0
print(list1[0]) #kishor
print(list1[-1]) #kapil

#slicing => accessing multiple elements from list [start_index:end_index:step], end index is not included
print(list1[2:5:1]) #rojans, mission, resh
print(list1[2:5:2]) #rojans, resh
print(list1[6:1:-1]) #nishant, nioz, resh, mission
print(list1[6:1:-2]) #nishant, resh
print(list1[-1:-5:-1]) #kapil, nishant, nioz, resh
print(list1[:5]) #kishor, rojanc, rojans, mission, resh
print(list1[5:]) #nioz, nishant, kapil
print(list1[:]) #kishor, rojanc, rojans, mission, resh, nioz, nishant, kapil

#conditonal statements
#codes are executed based on the condition
# if else =>if else, if elif else
# match case => like switch case in other programming languages
# looping statements => for loop, while loop
# we use for loop => when we know the number of iterations
# we use while loop => when we don't know the number of iterations

#if else
#simple if else => only if no else
# if condition:
    #code to be executed if condition is true
if(10>5):
    print("condition is true")
age=int(input("Enter your age: "))
if(age>=18):
    print("You are eligible to vote")
#if else 
if(age>=18):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
# if elif else
percentage=int(input("Enter your percentage: "))
if(percentage>=90):
    print("You got A+ grade")
elif(percentage>=80):
    print("You got A grade")
elif(percentage>=70):
    print("You got B+ grade")
else:
    print("You got C grade")

#nested if else
#program to find greatest number of three numbers
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if(num1>num2):
    if(num1>num3):
        print(f"{num1} is greatest")
    else:
        print(f"{num3} is greatest")
else:
    if(num2>num3):
        print(f"{num2} is greatest")
    else:
        print(f"{num3} is greatest")
#f-string => formatted string

# task1: make a calculator using if elif else
# task2: userlogin system using dictionary and if else