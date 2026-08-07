#encapculation => the main idea is data hiding
#we use __ as prefix in attributes or method to make it hidden
#the hidden data can only be accessed inside the class from another not hidden data
class Stundent:
    __name='kishor'
    name=__name
s1=Stundent()
print(s1.name)
class Credentials:
    def __init__(self,username,password):
        self.__username=username #attributes hidimg
        self.__password=password # ''
    def __display(self): # method hiding
        return self.__username
    def changepass(self,oldpass,newpass):
        if self.__password==oldpass:
            self.__password=newpass
            print(f'{self.__display()} your password changed successful')
        else:
            print('old password doesnt match')
c1=Credentials('kishor','kishor123')
c1.changepass('kishor123','kishor345')

#abstraction => the main idea is showing what is needed only, hiding inplementation details
#import abstractmethod form abc method ABC = Abstract Base Class
#the parent class should inherit from ABC class
#the parent class should have atleast one abstractmethod
#the child class should inherit form parent class
#then ever class the inherits from parent class should have abstractmethod

from abc import ABC,abstractmethod
class Parent(ABC):
    name="parent"
    @abstractmethod
    def abc(self):
        print(self.name)
class Child(Parent):
    name="child"
    def abc(self):
        print(self.name)
c1=Child()
c1.abc()
print()
class Student(ABC):
    def __init__(self,name,gender,marks):
        self.name=name
        self.gender=gender
        self.marks=marks
    @abstractmethod
    def displayMarks(self):
        print(self.marks)
class Mindrisers(Student):
    def __init__(self, name, gender, marks):
        std=Stundent(name,gender,marks)
    def displayMarks(self):
        print(self.std.marks)
m1=Mindrisers('kishor','male','70')
m1.displayMarks()

#task: reverse a list using loop and slicing
# frequency of characters in a sting