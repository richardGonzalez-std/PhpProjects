class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def addPassenger(self,name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Draco", "Ron", "Hermione"]

for person in people:
    success = flight.addPassenger(person)
    if success:
        print(f"Added {person} to flight successfully!, available {flight.open_seats()} seats")
        
    else:
        print(f"Failed to add {person} to flight successfully")