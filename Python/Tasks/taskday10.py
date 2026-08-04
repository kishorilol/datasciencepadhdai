#task: implement class and objects for car
class Car:
    def __init__(self,brand,model,year,registration):
        self.brand=brand
        self.model=model
        self.year=year
        self.registration=registration
    def Display(self):
        print(f'Brand Name: {self.brand}')
        print(f'Model Name: {self.model}')
        print(f'Year: {self.year}')
        print(f'Registration Number: {self.registration}')
car1=Car('Toyota','Supra','2020','02tk123')
car1.Display()
print()
car2=Car('Hyundai','Creta','2024','90fhe213')
car2.Display()
