class Car:
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_dist = 0

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if 0 <= new_speed <= self.max_speed:
            self.current_speed += new_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = self.max_speed
        return

car = Car("ABC-123", 142)

# for k,v in car.__dict__.items():
#     print(f"{k}: {v}")

print(f"Current speed is: {car.current_speed}")
car.accelerate(30)
print(f"Current speed is: {car.current_speed}")
car.accelerate(50)
print(f"Current speed is: {car.current_speed}")
car.accelerate(70)
print(f"Current speed is: {car.current_speed}")
car.accelerate(-200)
print(f"Current speed is: {car.current_speed}")