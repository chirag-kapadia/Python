

class Student:
    Demo = 30

    def __init__(self, name, pno, rollno):
        self.name = x
        self.pno = y
        self.roll = rollno

    def Display(self):
        print("Your Name is : ", self.name)
        print("Your Phone No is : ", self.pno)


x = input("Enter Your Name : ")
y = int(input("Enter your Phone No : "))
z = int(input("Enter your age : "))
s1 = Student(x, y, z)
s1.Display()
