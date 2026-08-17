#exception handling
#handling the error
#try=> we write block of code that may contain error
#if error occurs then exception block is executed
#else try block will be executed
list1=[1,2,3,3,4,5,6,7]
# general error handling
try:
    print(list1[14])
except:
    print('list index out of range')
#specific error handling
try:
    print(list1[15])
    num1=int(input('enter number a: '))
    num2=int(input('enter number b: '))
    print(num1/num2)
except IndexError:
    print('list index out of range')
except ValueError:
    print('invalid input')
except ZeroDivisionError:
    print('division by zero is not allowed')
#recommended approach
try:
    print(list1[15])
    num1=int(input('enter number a: '))
    num2=int(input('enter number b: '))
    print(num1/num2)
except Exception as e:
    print('error:',e)
    