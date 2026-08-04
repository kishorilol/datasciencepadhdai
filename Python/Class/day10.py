#oop => object orented programming
#implemented using class and object
#class=> blueprint of objects
#object=> instance of a class
# class keyword is used to make a class
#syntax:
# class class_name:
#     attributes=>variable defined inside a class
#     methods=>functions defined inside a class
class Students:
    name='kishor'
    age=21
    def set_info(self): #the methods always contains self parameter
        pass
std1=Students()
print(std1)
print(std1.name)
print(std1.age)
#class attribute=>all objects has same data no change in data for different object
#object attribute=> all objects has there own attributes
#we always need method to create object attribute
# class Student:
#     college_name='mindrisers'
#     def set_info(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def display(self):
#         print(f'Name: {self.name}')
#         print(f'Age: {self.age}')
#         print(f'Gender: {self.gender}')
#         print(f'College: {self.college_name}')
# std=Student()
# print(std)
# std.set_info('kishor',21,'male')
# std.display()
# std2=Student()
# std2.set_info('rojan',21,'male')
# std.display()
#constructors => function that runs automatically when function is created
#used to create object attributes
#there is only one constructor __init__
class Studentss:
    college_name='ascol'
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')
        print(f'College: {self.college_name}')
std=Studentss('kishor',21,'male')
std.display()