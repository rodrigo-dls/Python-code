# Extend the previous program by creating a Building class. The initializer parameters for the class are the numbers of the bottom and top floors and the number of elevators in the building. When a building is created, the building creates the required number of elevators. The list of elevators is stored as a property of the building. Write a method called run_elevator that accepts the number of the elevator and the destination floor as its parameters. In the main program, write the statements for creating a new building and running the elevators of the building.

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
            print(f"{self.current_floor * '-' + '>'} Floor: {self.current_floor}")
            if floor == self.current_floor: break
        else:
            if floor == self.current_floor:
                print("The elevator is already on that floor.")
            else:
                print("The desired floor does not exist in this building.")
        return

class Building:
    def __init__(self, bottom, top, n_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = self.create_elevators(n_elevators)  # [ Elevator(self.bottom, self.top) for _ in range(n_elevators) ] would let me dispose from create_elevators()

    def create_elevators(self, n_elevators):
        elevators = []
        for _ in range(n_elevators):
            elevators.append( Elevator(self.bottom, self.top) )
        return elevators

    def run_elevator(self, id_elevator, dest_floor):
        print(f"{'='*10} Elevator {id_elevator} {'='*10}")
        self.elevators[id_elevator-1].go_to_floor(dest_floor)
        return

b = Building(0, 10, 5)

b.run_elevator(3, 7)
b.run_elevator(2, -2)
b.run_elevator(5, 11) # Tries to go to a floor higher than the building's top floor
b.run_elevator(1, 5)
b.run_elevator(4, 8)
print()
# Display properties of building's elevator
for key, value in b.__dict__.items():
    if key == 'elevators':
        for id_elevator, elevator in enumerate(value, 1):
            print(f"Elevator {id_elevator} is in floor {elevator.__dict__.get('current_floor')}")

