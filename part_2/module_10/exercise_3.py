# Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all elevators to the bottom floor. Continue the main program by causing a fire alarm in your building.

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
        while floor != self.current_floor and (
                self.bottom <= floor <= self.top):
            if floor < self.current_floor:
                self.floor_down()
            elif floor > self.current_floor:
                self.floor_up()
            print(
                f"{self.current_floor * '-' + '>'} Floor: {self.current_floor}")
            if floor == self.current_floor: break
        else:
            if floor == self.current_floor:
                print(
                    "The elevator is already on that floor.")
            else:
                print(
                    "The desired floor does not exist in this building.")
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

    def fire_alarm(self):
        print(f"{'-'*40}")
        print(f"| {'FIRE ALARM HAS BEEN ACTIVATED!':^{40 - 4}} |")
        print(f"{'-'*40}")

        for id_elevator, elevator in enumerate(self.elevators, 1):
            print(f"{'=' * 10} Elevator {id_elevator} {'=' * 10}")
            elevator.go_to_floor(self.bottom)
        return

b = Building(0, 10, 5)

b.run_elevator(1, 5 )
b.run_elevator(2, -1 ) # Tries to go to a floor lower than the building's bottom floor
b.run_elevator(3, 0 )
b.run_elevator(4, 8 )
b.run_elevator(5, 11) # Tries to go to a floor higher than the building's top floor

print()

# Display position of building's elevators
for key, value in b.__dict__.items():
    if key == 'elevators':
        for i, elevator in enumerate(value, 1):
            print(f"Elevator {i} is in floor {elevator.__dict__.get('current_floor')}")

print()
b.fire_alarm()
print()

# Display position of building's elevators
for key, value in b.__dict__.items():
    if key == 'elevators':
        for i, elevator in enumerate(value, 1):
            print(f"Elevator {i} is in floor {elevator.__dict__.get('current_floor')}")

