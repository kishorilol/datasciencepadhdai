#magic methods => special method that runs automatically under certain condition
#__init__ => automatically runs when an object is created
#__str__ => automatically runs when a object is printed
class Students:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
    def display(self):
        print(f'name: {self.name}')
        print(f'gender: {self.gender}')
    def __str__(self): #str always returns a value
        return f'{self.name} object is printed'
class Numbers:
    def __init__(self,a):
        self.num=a
    def __add__(self, other):
        return f'addition ={self.num+other.age}'
s1=Students('kishor','male',21)
s1.display()
print(s1)
n1=Numbers(5)
n2=Numbers(10)
print(n1+s1) # n1.__add__(n2)

#LMS
#Create, visit
#books: physical,digital(takes memory)
class Book:
    def __init__(self,name,author):
        pass
    def display(self):
        pass
class Ebook(Book):
    def __init__(self,name,author,size):
        super().__init__()
        
#make a fully functioning lms
#download git and github