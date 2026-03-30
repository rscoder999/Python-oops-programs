class Student:
  def __init__(self,name,rollno):
    self.name=name
    self.rollno=rollno

#defining a method
  def display(self):
      print(f"Name: {self.name}")
      print(f"Rollno: {self.rollno}")


#creating an object
student1=Student("Ram",1)
student1.display()
