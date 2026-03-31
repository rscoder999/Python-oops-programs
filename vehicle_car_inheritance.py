

class Vehicle:

    def start(self):
        print("Vehicle started")

class Car(Vehicle):

    def drive(self):
        print("Car is driving")


c1=Car()
c1.start()
c1.drive()
