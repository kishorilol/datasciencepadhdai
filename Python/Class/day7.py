#lambda function => function in one line
#lambda keyword is used to define lambda function
#lambda is also known as nameless function =>name is not needed to define a funcition
#Syntax: name = lambda parameter : operations
#call: name(arguments)
sum = lambda a,b: a/b if b!=0 else 'cannot be divide by 0' #if else in lambda
print(sum(1,0))
#map function => it applies the function to every element of group datatype
#syntax: map(function,group_data_type)
list1=[1,2,3,4,5]
result=map(lambda x:x**2,list1)
print(list(result))
#filter function => filters the elements of group datatype
#syntax: filter(function,group_data_type)
result1=filter(lambda x:x>3,list1)
print(list(result1))
#reduce function => reduce the group data type into a single value
from functools import reduce
#syntax: reduce(function,group_data_type)
result2=reduce(lambda x,y:x+y,list1)
print(result2)
#zip function=> combines multiple list into a tuple in an element wise order
#zip expects a homogeneous list
list2=['kxa','thikxa','hainahola','ho','lala']
list3=['a','b','c','d','e']
result3=zip(list1,list2,list3)
print(list(result3))
#list comprehension => using keywords inside a list
list4=[i for i in range(10) if i%2==0]
print(list4)
#dictionary comprehension
dict={key:value for key,value in zip(list1,list2)}
print(dict)