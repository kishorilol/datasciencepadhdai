#multilevel inheritence
#child inherit from parent and parent from grandparent

class Grandparent:
    name='child'
    def display2(self):
        print('displaying form Granparent')
class Parent(Grandparent):
    name='child'
    def display1(self):
        print('displaying form parent2')
class Child(Parent):
    name='child'
    def display(self):
        print('displaying form child') 
c1=Child()
c1.display2()

#super() => is used to access the properties of parent class from inside the child class
#in python super() follows mro chain
class A:
    def show(self):
        print('A')
class B(A):
    def show(self):
        super().show()
        print("B")
class C(A):
    def show(self):
        super().show()
        print("C")
class D(B,C):
    def show(self):
        super().show()
        print("D")
print(D.mro())
d1=D()
d1.show()

#del => Deletes the attributes, method or an object
class student:
    name='kishor'
    age=21
    sem=6
    def show (self):
        print(self.age)
s1=student()
print(s1.name)
s1.show()
try:
    del s1.name
    del s1.show
except:
    pass
print()

#polymorphism => same property different behaviour
#polymorphism follows the concept of property overriding
print(5+10)
print('5'+'10')

class Man:
    def eat(self):
        print('eats pizza')
class Cat:
    def eat(self):
        print('eats milk')
class Dog:
    def eat(self):
        print('eats bone')
m1=Man()
c1=Cat()
d1=Dog()
m1.eat()
c1.eat()
d1.eat()