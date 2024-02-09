class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.gas = 50

    def car_details(self):
        print(f'{self.year} {self.make} {self.model}')

    def add_gas(self, g):
        if g > 0:
            self.gas += g
        if self.gas >= 100:
            print('This gas tank is full!')
        if self.gas + g > 100:
            max_allowed = 100 - self.gas
            print(f'Gas level is {self.gas}. You can only add {max_allowed} more gallons')
        
    def check_gas(self):
        print(f'The gas level is at {self.gas}')

first_car = Car('Honda', 'Accord', '1999')
first_car.car_details()
first_car.check_gas()


# COMPOSITION
# you may find that you’re adding more and more detail to a class. 
# You’ll find that you have a growing list of attributes and methods and 
# that your files are becoming lengthy. In these situations, you might recognize 
# that part of one class can be written as a separate class. You can break your 
# large class into smaller classes that work together; this approach is called composition.

# Composition example with Battery
class Battery:
    def __init__(self, battery=60):
        self.battery = battery

    def check_battery(self):
        print(f'Battery is at {self.battery}%')
        
    def charge(self, battery):
        if battery > 0:
            self.battery += battery
            # self.check_gas()
        if self.battery >= 100:
            print('This battery fully charged!')
        if self.battery + battery > 100:
            max_allowed = 100 - self.battery
            print(f'battery level is {self.battery}%. You can only charge {max_allowed} more')


# SUBCLASS EXAMPLE
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def add_gas(self, g):
        raise AttributeError("Electric cars don't use gas!")
    
    


first_electric_car = ElectricCar('Nissan', 'Leaf', 2024)

first_electric_car.car_details()
first_electric_car.battery.charge(20)
