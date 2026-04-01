# Now we will program a car race. The travelled distance of a new car is initialized as zero.
# At the beginning of the main program, create a list that consists of 10 car objects created using a loop.
# The maximum speed of each new car is a random value between 100 km/h and 200 km/h. The registration numbers are created as follows: “ABC-1”, “ABC-2” and so on. Now the race begins. One per every hour of the race, the following operations are performed:

#         The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. This is done using the accerelate method.
#         Each car is made to drive for one hour. This is done with the drive method.
#
# The race continues until one of the cars has advanced at least 10,000 kilometers. Finally, the properties of each car are printed out formatted into a clear table.
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
        # self.current_speed = max(0, new_speed)
        self.current_speed = min(self.max_speed, max(0, new_speed))
        # if 0 <= new_speed <= self.max_speed:
        #     self.current_speed = new_speed
        # elif new_speed < 0:
        #     self.current_speed = 0
        # else:
        #     self.current_speed = self.max_speed
        return

    def drive(self, hours):
        self.travelled_dist += self.current_speed * hours
        return

# Build cars
cars = []
for i in range(10):
    car = Car(f"ABC-{i+1}", random.randint(100,200))
    cars.append(car)

# The race
race_is_over = False
while not race_is_over:
    for car in cars:
        car.accelerate(random.randint(-10,15))
        car.drive(1)
        if car.travelled_dist >= 10000 :
            race_is_over = True

# REPORT TABLE
# Head of the Table
row_head = f"|"
for col in cars[0].__dict__.keys():
    row_head += f"{str(col).replace('_', ' ').capitalize():^20}|"
horizontal_line = '-'*len(row_head)
print(horizontal_line)
print(row_head)
print(horizontal_line)

# Body of the Table
for car in cars:
    print(car)
print(horizontal_line)
