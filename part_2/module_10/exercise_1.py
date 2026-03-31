# Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters. The elevator has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor. If you make elevator h for example the method call h.go_to_floor(5), the method calls either the floor_up or floor_down methods as many times as it needs to get to the fifth floor. The methods run the elevator one floor up or down and tell what floor the elevator is after each move. Test the class by creating an elevator in the main program, tell it to move to a floor of your choice and then back to the bottom floor.

class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_down(self):
        self.current_floor -= 1
        return

    def floor_up(self):
        self.current_floor += 1
        return

    def go_to_floor(self, floor):
        while floor != self.current_floor and (self.bottom <= floor <= self.top):
            if floor < self.current_floor:
                self.floor_down()
            elif floor > self.current_floor:
                self.floor_up()
            print(f"{self.current_floor*'-'+'>'} Floor: {self.current_floor}")
        return

h = Elevator(0, 10)

print(h.__dict__)

h.go_to_floor(5)

h.go_to_floor(2)

h.go_to_floor(7)

h.go_to_floor(-2)

h.go_to_floor(0)

