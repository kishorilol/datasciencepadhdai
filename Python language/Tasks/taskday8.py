#task: make a atm machine with filehandling
import json

def getData():
    username=input('Enter username: ')
    password=input('Enter password: ')
    return username,password

def getFileData():
    file=open('userdata.txt','r')
    content=file.read()
    file.close()
    data=content.split('*')
    return data

def register():
    username,password=getData()
    veri=getFileData()
    for user in veri:
        if user!="":
            dict_cred=json.loads(user)
            if dict_cred["username"]==username:
                print('username already used')
                break
    else:
        data={'username':username,'password':password,'balance':0}
        file=open('userdata.txt','a')
        file.write(json.dumps(data)+'*')
        file.close()

def update(update_data):
    file=open('userdata.txt','w')
    file.write(update_data)
    file.close()

def deposit(username,damount):
    data=getFileData()
    updated_data=""
    for user in data:
        if user!="":
            dict_cred=json.loads(user)
            if dict_cred["username"]==username:
                dict_cred["balance"]+=damount
            updated_data+=json.dumps(dict_cred)+'*'
    update(updated_data)
    print('Deposit success')

def withdrawl(username,wamount):
    data=getFileData()
    updated_data=""
    for user in data:
        if user!="":
            dict_cred=json.loads(user)
            if dict_cred["username"]==username:
                dict_cred["balance"]-=wamount
            updated_data+=json.dumps(dict_cred)+'*'
    update(updated_data)
    print('Withdrawl success')

def checkBalance(username):
    data=getFileData()
    for user in data:
        if user!="":
            dict_cred=json.loads(user)
            if dict_cred["username"]==username:
                return dict_cred["balance"]

def login():
    username,password=getData()
    data=getFileData()
    for user in data:
        if user != "":
            dict_cred=json.loads(user)
            if dict_cred['username']==username and dict_cred['password']==password:
                print('login success')
                while True:
                    act=input('Enter d for deposit, w for withdrawl, b for check balance or e for exit: ')
                    match act:
                        case 'd':
                            deposit_amount=int(input('Enter the amount you want to deposit: '))
                            deposit(username,deposit_amount)
                        case 'w':
                            withdrawl_amount=int(input('Enter the amount you want to withdraw: '))
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
