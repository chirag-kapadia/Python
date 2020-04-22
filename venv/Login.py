
def login():
    UName=input("Enter Your Username : ")
    Pass=input("Enter Your Password : ")

    if UName=='Chirag' and Pass=='Admin':
        print("Successful Login")
    else:
        print("Invalid Username and Password!")
        login()

def forgetPassword():
    UName=input("Enter Username to Change Password : ")
    Pass=input("Enter Password to Change Password : ")
    if UName=='Chirag' and Pass=='Admin':
        NewPassword=input("Enter New Password : ")
        Pass=NewPassword
        print("Your Password Change Successfully And Your Password is : ",Pass)
        forgetPassword()
    else:
        print("Please Check Your Username and Passowrd")
        forgetPassword()


# login()
forgetPassword()