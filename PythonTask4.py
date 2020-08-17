class string:
    def __init__(self):
        self.var_string=""
    def getString(self):
        self.var_string = input("enter string \n")
    def printString(self):
        print(self.var_string.upper())
mystr = string()
mystr.getString()
mystr.printString()