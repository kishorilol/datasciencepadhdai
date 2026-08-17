#decorator=> function that receives a function as an attributes
#decorators help in modifying the function but without changing its actual code
#it receives a function, it has a nested function
#the nested function modifies the function
#the decorator returns nested function
#to use a decorator we need to use @ as prefix and should be just above the function
def myDecorator(func):
    def wrapper():
        for i in range(5):
            func()
    return wrapper
@myDecorator
def display():
    print('kxa')
    print(12)
    print('thik xa')
display()
# @abstractmethod
# @staticmethod
class Students:
    college='ascol'
    @staticmethod #no need to use self for function that doesnt need self 
    def display():
        print('displaying')
s1=Students
s1.display()

#4 pillers of oop
#inheritence
#encapsulation
#polymorphism
#abstraction
print()
print()
# Inheritance => child class has the properties of the parent
#types:
#single=> one child inherit from one parent
#multiple=> one child inherit form multiple parent
#multilevel=> child inherit fomr parent, parent inherit form grandparent so child inherits grandparents

#single inheritence:
class Parent:
    name='child'
    def display1(self):
        print('displaying form parent')
class Child(Parent):
    name='child'
    def display(self):
        print('displaying form child')
c1=Child()
print(c1.name)
c1.display()
c1.display1()

#multiple inheritence
#python uses MRO, chain of parent class
#decides from which class the properties are accepted
#MRO chain is always of class not object
#class_name.mro
class Parent1:
    name='child'
    def display1(self):
        print('displaying form parent1')
class Parent2:
    name='child'
    def display1(self):
        print('displaying form parent2')
class Child(Parent1,Parent2):
    name='child'
    def display(self):
        print('displaying form child')
c1=Child()
print(c1.name)
c1.display()
print(Child.mro())
c1.display1()