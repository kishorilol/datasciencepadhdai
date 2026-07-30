#file handling in python
#file handling flow
#open, perform operation, close
# modes: r=>read, w=>write, a=>append
#syntax: open('file_name','mode')
#oeprations: read(),write()
#close: close()
#readmode

# file=open('abc.txt','r')
# content=file.read()
# file.close()

#in read mode if there is no file then it gives an error
#writemode

# file=open('abc.txt','w')
# content=file.write('kishor maharjan')#we can only write string and JSON
# file.close()

#in write mode if the file doesnt exist new file is created
#if we open a file in write mode it ereases the previous content and writes new
#in append mode adds into the existing file without removing removing previous data at last 
#it creates file if not made

# file=open('abc.txt','a')
# content=file.write(' im a student')#we can only write string and JSON
# file.close()

#JSON: JavaScript Object Notation
#always wrapped inside {"key":"value"}
#we need to import JSON
#dumps()=>converts dict to json
#loads()=>converts json to dict
import json
def register(username, password):
    dict_creds = {username:password}
    file = open('credentials.txt','a')
    file.write(json.dumps(dict_creds)+"*")
    file.close()
    
    
def login(username, password):
    file = open('credentials.txt','r')
    content = file.read()
    file.close()
    
    list_creds = content.split("*")
    for cred in list_creds:
        if cred != "":
            dict_cred = json.loads(cred)
            if username in dict_cred and dict_cred[username] == password:
                print("Login Successful")
                break
    else:
        print("Login Failed: Invalid Credentials")
        

def operation(method):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if method == 'register':
        register(username, password)
    else:
        login(username, password)

while True:
    choice = input("Enter 1 for register, 2 for login, 3 for exit:  ")
    match choice:
        case '1':
            operation('register')
        case '2':
            operation('login')
        case '3':
            print("Thank you")
            break
        case _:
            print("Invalid Input")