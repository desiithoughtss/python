#1
class Car:
    
    total_car = 0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model 
        Car.total_car +=1
        
    def get_brand(self):
        return self.__brand + "!"
        
    def full_name(self):
        return f"{self.__brand} and {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel" 
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric charge" 

class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCar2(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCar2("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())

my_tesla = ElectricCar("tesla", "Model S", "85Kwh")
my_car = Car("abc1", "anymodel1")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# my_car.model = "ASDFGHJK"
# print(my_car.model)

# my_car.model = "ASDFGHJK"
# print(my_car.model)

# print(Car.general_description())
# print(my_car.general_description())

# print(Car.total_car)

# print(my_tesla.fuel_type())
# print(my_car.fuel_type())

# print(my_tesla.get_brand()) #inheritance
# print(my_tesla.full_name())
# print(my_tesla.brand)
# print(my_tesla.model)
# print(my_tesla.battery_size)

# my_car = Car("abc1", "anymodel1")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# another_car = Car("abc1", "anymodel2")
# print(another_car.brand)
# print(another_car.model)