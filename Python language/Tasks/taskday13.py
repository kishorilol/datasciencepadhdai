#task
# reverse a list using loop and slicing
#using loop
list1=[1,2,3,4,5,"kishor","ilol"]
print(list1)
temp=[]
for i in range(len(list1)-1,-1,-1):
    temp.append(list1[i])
print('after applying loop for reverse')
print(temp)
#using slicing
print('using slicing')
a=len(list1)
print(list1[::-1])
# frequency of characters in a string
string1="mathematics"
store={}
for i in string1:
    if i in store:
        store[i]+=1
    else:
        store[i]=1
print(f'frequency of each letter in string {string1}: ')
print(store)