#task: make a user login and signup
# user_data = []
# while True:
#     choice = input("Enter 1 for sign up, 2 for sign in, 3 for exit: ")
#     match choice:
#         case "1":
#             username = input("Enter your username: ")
#             password = input("Enter your password: ")
#             user_data.append({username: password})
#             print(f"Sign up successful for {username}")
#         case "2":
#             username = input("Enter your username: ")
#             password = input("Enter your password: ")
#             for user_record in user_data:
#                 if username in user_record:
#                     if password == user_record[username]:
#                         print("Login Successful")
#                     else:
#                         print("Password Incorrect")
#                 else:
#                     print("Username not found")
#                     break
#         case "3":
#             print("Exiting the program")
#             break
#         case _:
#             print("Invalid choice")
            
#task: make a atm
atm_data = []
while True:
    choice=input('Enter 1. for register 2. for login and 3. for exit')
    match choice:
        case '1':
            username=input('Enter your username: ')
            password=input('Enter your password: ')
            atm_data.append({
                'username': username,
                'password': password,
                'balance': 0
            })
            print('Account registered successful')
        case '2':
            username=input('Enter your username: ')
            password=input('Enter your password: ')
            for user in atm_data:
                if user['username']==username and user['password']==password:
                    print('login success')
                    while True:
                        act=input('Enter d for deposit, w for withdrawl, b for check balance or e for exit: ')
                        match act:
                            case 'd':
                                deposit_amount=int(input('Enter the amount you want to deposit: '))
                                user['balance']+=deposit_amount
                                print('deposit successful')
                            case 'w':
                                withdrawl_amount=int(input('Enter the amount you want to withdraw: '))
                                user['balance']-=withdrawl_amount
                                print('withdraw successful')
                            case 'b':
                                print(f'Your current balance is {user['balance']}')
                            case 'e':
                                print('exiting your account')
                                break
                            case _:
                                print('invalid entry')
                else:
                    print('login failed')
        case '3':
            print('Exiting the system')
            break
        case _:
            print('Please enter valid input')