#here salary attribute is a private member which can be accessed only within the class
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

emp = Employee(50000)
print(emp.get_salary())
