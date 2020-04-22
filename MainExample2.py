def GetData():
    Name = input("Enter Your Name : ")
    Email = input("Enter Your Email : ")
    Phone = int(input("Enter Your Phone Number : "))
    Display(Name, Email, Phone)


def Display(x, y, z):
    print("Name : ", x)
    print("Email : ", y)
    print("Phone : ", z)
    login()


def login():
    UName = input("Enter Your Username : ")
    Pass = input("Enter Your Password : ")

    if UName == 'Chirag' and Pass == 'Admin':
        print("Successful Login")
        forgetPassword()
    else:
        print("Invalid Username and Password!")
        login()


def forgetPassword():
    UName = input("Enter Username to Change Password : ")
    Pass = input("Enter Password to Change Password : ")
    if UName == 'Chirag' and Pass == 'Admin':
        NewPassword = input("Enter New Password : ")
        Pass = NewPassword
        print("Your Password Change Successfully And Your Password is : ", Pass)
        forgetPassword()
    else:
        print("Please Check Your Username and Password")
        forgetPassword()


def main():
    GetData()
    login()
    forgetPassword()


if __name__ == "__main__":
    main()
