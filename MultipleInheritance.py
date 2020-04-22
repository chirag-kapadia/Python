class Teams:
    def Developer(self):
        print("Chirag")
        print("Balvant")


class Teams2():
    def Designer(self):
        print("Apurva")


class Teams3(Teams2,Teams): # Look Here for concept
    def Security(self):
        print("Yash")
        print("Tanmay")


T1 = Teams3()
T1.Developer()
T1.Designer()
T1.Security()
