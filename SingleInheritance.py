class Teams:
    def Developer(self):
        print("Chirag")
        print("Balvant")


class Teams2(Teams): # Look Here for concept
    def Designer(self):
        print("Apurva")


T1 = Teams2()
T1.Designer()
T1.Developer()
