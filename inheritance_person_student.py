
#here person is parent class and student is child class
class Person:
    def __init__(self,name):
        self.name=name


class Student(Person):

    def study(self):
        print(f"{self.name} is studying")


stu1=Student("Ram")
stu1.study()
