#operator continued
# identity operator => is is not
#checks actual location instead of value
a=[10]
b=[10]
c=a
print(a==b)
print(a is b)
print(a is c)
print(a is not b)
# logical operator => and or not
list1=[True,True,False,False]
list2=[True,False,True,False]
for i in range (len(list1)):
    print("and",list1[i] and list2[i])
    print("or",list1[i] or list2[i])
    print('not',not list1[i])
# data types
# 1.mutable datatype => values can be changed and updated after creation
# example: list, dictionary, set
# 2.immutable datatype => values cannot be changed and updated '', to change new object is created
#example: string, tuples
#type() => finds the datatype of a indentifier
a=10
print(type(a))
#group datatype => that contains multiple elements
#example: string, list, tuple, set, dictionary, JSON
#list => inside[] contains multiple elements, an ordered and mutable datatype
a=[10,"hello",True,[1,2,3,4]]
print(a)
#tuples => inside () ordered but immutable
tup=(10,"kxa",True,a)
print(tup)
#set => inside {} contains only int, float and string, is unordered and mutable, cannot contain dublicate
set1={1,2,3,"haha",1.2}
print(set1)
#dictionary => elements comes in pair of key:value, inside{}, ordered and mutable
dicti={
    "name":"kishor",
    "age":21,
    "address":"manamaiju",
    "subject":['maths','cs']
}
print(dicti)
#task:try all the method of different datatypes
#create a list of username, ask username as input and check if it is in list or not
#create a dictionary of username and passwords, extract all the username from the dictionary and input username from the user ans check if it is there or not
