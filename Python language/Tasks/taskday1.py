#task 1
print('portugal')
#task 2
fav_country='portugal'
print(fav_country)
#task 3
num_1=int(input('Enter Your First Number: '))
num_2=int(input('Enter Your Second Number: '))
print('The sum of',num_1,'and',num_2,'is',num_1+num_2)
print('The difference of',num_1,'and',num_2,'is',num_1-num_2)
print('The product of',num_1,'and',num_2,'is',num_1*num_2)
print('The division of',num_1,'and',num_2,'is',num_1/num_2)
print('The power of',num_1,'and',num_2,'is',num_1**num_2)
print('The modulus of',num_1,'and',num_2,'is',num_1//num_2)
#task 4
num_1=int(input('Enter Your First Number: '))
num_2=int(input('Enter Your Second Number: '))
operator=input('Enter which aritmetic operation to perform + for addition, - for substraction, * for multiplication, / for division, ** for power, // for floor or % for modulus:')
if operator == '+':
    result=num_1+num_2
elif operator=='-':
    result=num_1-num_2
elif operator=='*':
    result= num_1*num_2
elif operator=='/':
    result=num_1/num_2
elif operator=="**":
    result=num_1**num_2
elif operator=="//":
    result=num_1//num_2
else:
    print('Enter correct operator')
print(result)
