# Extend the previosly written Car class by adding two subclasses: ElectricCar and GasolineCar. Electric cars have the capacity of the battery in kilowatt-hours as their property. Gasoline cars have the volume of the tank in liters as their property. Write initializers for the subclasses. For example, the initializer of electric cars receives the registration number, maximum speed and battery capacity as its parameter. It calls the initializer of the base class to set the first two properties and then sets its capacity. Write a main program where you create one electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l). Select speeds for both cars, make them drive for three hours and print out the values of their kilometer counters.

class Car:
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_dist = 0

    def __str__(self):
        return f"|{self.reg_num: ^10}|{self.max_speed: ^10}|{self.current_speed: ^10}|{self.travelled_dist: ^10}|"

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        self.current_speed = min(self.max_speed, max(0, new_speed))
        return

    def drive(self, hours):
        self.travelled_dist += self.current_speed * hours
        return

class ElectricCar(Car):
    def __init__(self, reg_num, max_speed, battery_capacity):
        super().__init__(reg_num, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, reg_num, max_speed, tank_vol):
        super().__init__(reg_num, max_speed)
        self.tank_vol = tank_vol


electric_car = ElectricCar('ABC-15', 180, 52.5)
gas_car = GasolineCar('ACD-123', 165, 32.3)

electric_car.accelerate(100)
electric_car.drive(3)
print(f"Electric car kilometers counter: {electric_car.travelled_dist}")

gas_car.accelerate(80)
gas_car.drive(3)
print(f"Gasoline car kilometers counter: {gas_car.travelled_dist}")
