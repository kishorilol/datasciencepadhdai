#function => block of code which is used to perform a specific task
#types of function => built-in function, user-defined function
#built-in function => functions which are already defined in python and can be used directly
#example of built-in function => print(), input(), len(), type(), int(), str(), float(), list(), tuple(), set(), dict()
#user-defined function => functions which are defined by the user to perform a specific task
#to define a funtion we use def keyword
#syntax:
# def function_name(parameter):
#     code to be executed
#function_name(arguments) function call need to be done to access the function
#arguments => the value that we pass into a function
#parameter => the values that the function recieves
def sum(a,b):
    print(a+b)
sum(1,2) 
#type of arguments 
#position arguments => the parameter that recieves the arguments according to the position
#keyword arguments => the parameter are sent in key value pair, the order of the arguments does not matter
def sum1(a,b):
    print(a+b)
sum1(b=2,a=1)
def learning(*args,**kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
learning(1,2,3,'lol','kxa',a=10,b='haina')
#global variable => a variable which is defined outside the function and can be accessed inside the function
#lifetime is throuhghout the program
#local variable => a variable which is defined inside the function and can only be accessed inside the function
#lifetime is only inside the function
b=10
def sum2(a):
    print(a) #a is local variable
    print(b) #b is global variable
sum2(5)
print(b) #b is global variable
#print(a) #a is local variable, will give error
#returnable function => a function which returns a value to the caller
def sum3(a,b):
    return a+b
result = sum3(5,10)
print(result) 

#task: update calculator program, login register and atm program 
