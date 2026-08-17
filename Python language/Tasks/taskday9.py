#task: implement all tasks using exception handling
 #calculator using exception handling
# while True:
#     try:
#         num1=int(input('enter number a: '))
#         num2=int(input('enter number b: '))
#         print('1.addition\n2.subtraction\n3.multiplication\n4.division')
#         choice=int(input('enter your choice: '))
#         if choice==1:
#             print(num1+num2)
#         elif choice==2:
#             print(num1-num2)
#         elif choice==3:
#             print(num1*num2)
#         elif choice==4:
#             print(num1/num2)
#         else:
#             print('invalid choice')
#     except ValueError:
#         print('invalid input')
#     except ZeroDivisionError:
#         print('division by zero is not allowed')
#     except Exception as e:
#         print('error:',e)
#     choice=input('do you want to continue? y/n: ')
#     if choice.lower()=='n':
#         break
# atm implementation using exception handling
import json

def getData():
    username=input('Enter username: ')
    password=input('Enter password: ')
    return username,password

def getFileData():
    try:
        file=open('userdata.txt','r')
        content=file.read()
        file.close()
        data=content.split('*')
        return data
    except Exception as e:
        print('error occured',e)

def register():
    username,password=getData()
    try:
        veri = getFileData()
    except Exception as e:
        print("Error reading file:", e)
        return
    for user in veri:
        if user!="":
            dict_cred=json.loads(user)
            if dict_cred["username"]==username:
                print('username already used')
                break
    else:
        data={'username':username,'password':password,'balance':0}
        try:
            file = open('userdata.txt', 'a')
            file.write(json.dumps(data) + '*')
            file.close()
            print("Registration successful")
        except Exception as e:
            print("Could not save user:", e)

def update(update_data):
    try:
        file = open('userdata.txt', 'w')
        file.write(update_data)
        file.close()
    except Exception as e:
        print("Error updating file:", e)

def deposit(username,damount):
    try:
        data = getFileData()
    except Exception as e:
        print("Error reading file:", e)
        return
    updated_data=""
    for user in data:
        if user!="":
            try:
                dict_cred = json.loads(user)
            except json.JSONDecodeError:
                print("Corrupted user data.")
                continue
            if dict_cred["username"]==username:
                dict_cred["balance"]+=damount
            updated_data+=json.dumps(dict_cred)+'*'
    try:
        update(updated_data)
    except Exception as e:
        print("Unable to update balance:", e)
    print('Deposit success')

def withdrawl(username,wamount):
    try:
        data = getFileData()
    except Exception as e:
        print("Error reading file:", e)
        return
    updated_data=""
    for user in data:
        if user!="":
            try:
                dict_cred = json.loads(user)
            except json.JSONDecodeError:
                print("Corrupted user data.")
                continue
            if dict_cred["username"]==username:
                if dict_cred["balance"] <= wamount:
                    print('insufficient balance')
                    return
                dict_cred["balance"]-=wamount
            updated_data+=json.dumps(dict_cred)+'*'
    try:
        update(updated_data)
    except Exception as e:
        print("Unable to update balance:", e)
    print('Withdrawl success')

def checkBalance(username):
    try:
        data = getFileData()
    except Exception as e:
        print("Error reading file:", e)
        return
    for user in data:
        if user!="":
            try:
                dict_cred = json.loads(user)
            except json.JSONDecodeError:
                print("Corrupted user data.")
                continue
            if dict_cred["username"]==username:
                return dict_cred["balance"]

def login():
    username,password=getData()
    try:
        data = getFileData()
    except Exception as e:
        print("Error reading file:", e)
        return
    for user in data:
        if user != "":
            try:
                dict_cred = json.loads(user)
            except json.JSONDecodeError:
                print("Corrupted user data.")
                continue
            if dict_cred['username']==username and dict_cred['password']==password:
                print('login success')
                while True:
                    act=input('Enter d for deposit, w for withdrawl, b for check balance or e for exit: ')
                    match act:
                        case 'd':
                            try:
                                deposit_amount=int(input('Enter the amount you want to deposit: '))
                            except ValueError:
                                print('please enter a valid number.')
                                continue
                            if deposit_amount<=0:
                                print('Amount must be greater than 0.')
                                continue
                            deposit(username,deposit_amount)
                        case 'w':
                            try:
                                withdrawl_amount=int(input('Enter the amount you want to withdraw: '))
                            except ValueError:
                                print('please enter a valid number.')
                                continue
                            withdrawl(username,withdrawl_amount)
                        case 'b':
                            print(f'Your current balance is {checkBalance(username)}')
                        case 'e':
                            print('Exiting your account')
                            break
                        case _:
                            print('invalid entry')
                break
    else:
        print('login failed')

while True:
    choice=input('Enter 1. for register 2. for login or 3. to exit: ')
    match choice:
        case '1':
            register()
        case '2':
            login()
        case '3':
            print('exiting the system')
            break
        case _:
            print('Invalid input')