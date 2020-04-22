def GetData():
    Name = input("Enter Your Name : ")
    Email = input("Enter Your Email : ")
    Phone = int(input("Enter Your Phone Number : "))
    Display(Name, Email, Phone)


def Display(x, y, z):
    print("Name : ", x)
    print("Email : ", y)
    print("Phone : ", z)


GetData()
