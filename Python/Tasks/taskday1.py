#task 1
print('portugal')
#task 2
fav_country='portugal'
print(fav_country)
#task 3
num_1=int(input('Enter Your First Number: '))
num_2=int(input('Enter Your Second Number: '))
operator=input('Enter which aritmetic operation to perform + for addition, - for substraction, * for multiplication, / for division, ** for power or // for modulus:')
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