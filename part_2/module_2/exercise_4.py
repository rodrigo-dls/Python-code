# This exercise continues the previous car race exercise from the last exercise set. Write a Race class that has the following properties: name, distance in kilometers and a list of cars participating in the race. The class has an initializer that receives the name, kilometers, and car list as parameters and sets their values to the corresponding properties in the class. The class has the following methods:
#
#     hour_passes, which performs the operations done once per hour in the original exercise: generates a random change of speed for each car and calls their drive method.
#     print_status, which prints out the current information of each car as a clear, formatted table.
#     race_finished, which returns True if any of the cars has reached the finish line, meaning that they have driven the entire distance of the race.
#
# Write a main program that creates an 8000-kilometer race called Grand Demolition Derby. The new race is given a list of ten cars similarly to the earlier exercise. The main program simulates the progressing of the race by calling the hour_passes in a loop, after which it uses the race_finished method to check if the race has finished. The current status is printed out using the print_status method every ten hours and then once more at the end of the race.

import random

class Car:
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_dist = 0

    def __str__(self):
        return f"|{self.reg_num: ^20}|{self.max_speed: ^20}|{self.current_speed: ^20}|{self.travelled_dist: ^20}|"

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        self.current_speed = min(self.max_speed, max(0, new_speed))
        return

    def drive(self, hours):
        self.travelled_dist += self.current_speed * hours
        return

class Race:
    def __init__(self, name, distance, cars_list):
        self.name = name
        self.distance = distance
        self.cars_list = cars_list

    def hour_passes(self):
        for car in self.cars_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
        return

    def print_status(self):
        # Head of the Table
        row_head = f"|"
        for col in self.cars_list[0].__dict__.keys():
            row_head += f"{str(col).replace('_', ' ').capitalize():^20}|"
        horizontal_line = '-' * len(row_head)
        print(horizontal_line)
        print(row_head)
        print(horizontal_line)

        # Body of the Table
        for car in self.cars_list:
            print(car)
        print(horizontal_line)
        return

    def race_finished(self):
        for car in self.cars_list:
            if car.travelled_dist >= self.distance:
                 return True
        return False

# Build cars
cars = []
for i in range(10):
    car = Car(f"ABC-{i+1}", random.randint(100,200))
    cars.append(car)

race = Race('Grand Demolition', 8000, cars)

print(f"{'='*10} {race.name} race starts now! {'='*10}")
hours = 0
while True:
    race.hour_passes()
    hours += 1
    if hours % 10 == 0:
        print(f"Hours of race: {hours}")
        race.print_status()
    if race.race_finished():
        print(f"Hours of race: {hours}")
        race.print_status()
        break