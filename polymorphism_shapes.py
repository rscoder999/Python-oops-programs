

class Circle:
    def area(self):
        return 3.14 * 5 * 5

class Square:
    def area(self):
        return 4 * 4

for shape in [Circle(), Square()]:
    print(shape.area())
