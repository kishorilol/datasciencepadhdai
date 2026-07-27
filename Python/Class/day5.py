#while loop => we dont know the number of iterations
#syntax:
#while condition:
    #code block
    #increment/decrement
#we can make infinite loop using while loop if we dont use increment/decrement
a=5
while a>0:
    print(a)
    a-=1
data=[]
while True:
    choice=input("Enter 1 for sign up, 2 for sign in, 3 for exit: ")
    match choice:
        case "1":
            username=input("Enter your username: ")
            password=input("Enter your password: ")
            data.append({username:password})
            print(f"Sign up successful for {username}")
        case "2":
            username=input("Enter your username: ")
            password=input("Enter your password: ")
            for user_record in data:
                if username in user_record:
                    if password == user_record[username]:
                        print("Login Successfull")
                    else:
                        print("Password Incorrect")
                else:
                    print("Username not found")
                    break
        case "3":
            print("Exiting the program")
            break
        case _:
            print("Invalid choice")
#for else => for else is used to execute a block of code when the loop is not terminated by a break statement
for i in range(5):
    print(i)
else:
    print("Loop completed without break")
#pass => ignores empty block
#task: make a userlogin and password verification
#task: make a atm
