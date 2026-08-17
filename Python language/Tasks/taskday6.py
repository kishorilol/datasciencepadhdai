#task: redo all the tasks using function

# 1. make a caculator program using function
# def calculator(a,b,operation):
#     match operation:
#         case '+':
#             return a+b
#         case '-':
#             return a-b
#         case '*':
#             return a*b
#         case '/':
#             return a/b
#         case _:
#             return 'Invalid operation'
# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
# operation = input('Enter operation (+,-,*,/): ')
# result = calculator(num1,num2,operation)
# print(f'Result: {result}')

#2. make a login register program using function
# users = {}
# def register(username,password):
#     if username in users:
#         return 'Username already exists'
#     users[username] = password
#     return 'User registered successfully'
# def login(username,password):
#     if username in users and users[username] == password:
#         return 'Login successful'
#     return 'Invalid username or password'   
# while True:
#     choice = input('Do you want to register or login? (r/l): ')
#     if choice == 'r':
#         username = input('Enter username: ')
#         password = input('Enter password: ')
#         print(register(username,password))
#     elif choice == 'l':
#         username = input('Enter username: ')
#         password = input('Enter password: ')
#         print(login(username,password))
#     else:
#         print('Invalid choice')
#     cont = input('Do you want to continue? (y/n): ')
#     if cont == 'n':
#         break
    
#3. make a atm using function

atm_data=[{'username':'admin','password':'admin@123'}]
def register(username,password):
    for user in atm_data:
        if user['username']==username:
            print('Username already exists')
            break
        elif len(password)<8:
            print('Password must be 8 characters or long')
            break
        elif '!' not in password and '@' not in password and '#' not in password and '$' not in password and '%' not in password and '&' not in password and '^' not in password and '*' not in password:
            print('password must contain a symbol')
            break
    else:
        atm_data.append({
            'username':username,
            'password':password,
            'balance':0
        })
        print('Register success')
def login(username,password):
    for user in atm_data:
        if user['username']==username and user['password']==password:
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
def deposit(username,damount):
    for user in atm_data:
        if user['username']==username:
            user['balance']+=damount
            print('deposit successful')
def withdrawl(username,wamount):
    for user in atm_data:
        if user['username']==username:
            user['balance']-=wamount
            print('withdraw successful')
def checkBalance(username):
    for user in atm_data:
        if user['username']==username:
            return user['balance']
while True:
    choice = input('Do you want to register or login? (r/l): ')
    if choice == 'r':
        username = input('Enter username: ')
        password = input('Enter password: ')
        register(username,password)
    elif choice == 'l':
        username = input('Enter username: ')
        password = input('Enter password: ')
        login(username,password)
    else:
        print('Invalid choice')
    cont = input('Do you want to continue? (y/n): ')
    if cont == 'n':
        print('Exiting the system')
        break