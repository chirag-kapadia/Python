class Student:

    def __init__(self, name, age, pno):
        self.name = name
        self.age = age
        self.pno = pno
        self.Subject= self.Subject()

    def show(self):
        print("Your name is : ", self.name)
        print("Your age is : ", self.age)
        print("Your phone no is : ", self.pno)
        self.Subject.show()

    # inner class
    class Subject:
        def __init__(self):
            self.m1 = 23
            self.m2 = 45
            self.m3 = 50

        def show(self):
            print("Mark1 is : ",self.m1)
            print("Mark2 is : ",self.m2)
            print("Mark3 is : ",self.m3)


s1 = Student('Chirag', 22, 9898989898)
s1.show()

