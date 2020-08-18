class StringClass:
    def __init__(self):
        self.var_string = ""

    def get_string(self):
        self.var_string = input("enter string \n")

    def print_string(self):
        print(self.var_string.upper())

if __name__ == '__main__':

    mystr = StringClass()
    mystr.get_string()
    mystr.print_string()
