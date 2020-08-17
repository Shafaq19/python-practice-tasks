class Person:
    def __init__(self, fname):
        self.name = fname

    def print(self):
        print("Name: %s\nGender: %s" % (self.name, self.getGender()))

    def getGender(self):
        pass


class Male(Person):
    def getGender(self):
        return "Male"


class Female(Person):
    def getGender(self):
        return "Female"


male = Male("ALI")
female = Female("kiran")
female.print()
male.print()
