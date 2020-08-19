from Pythontasks.PythonTask1 import Summ
from time import time_ns
from Pythontasks.PythonTask12 import remove_url

def time_the_function(function):
    def timer(*args, **kwargs):
        start = time_ns()
        function(*args, **kwargs)
        print("%s took %f nanoseconds" % (function.__name__, time_ns() - start))

    return timer

if __name__ == '__main__':
    #test functions to time
    Summ = time_the_function(Summ)
    remove_url = time_the_function( remove_url)
    sorted = time_the_function(sorted)

    sorted([6, 4, 2, 9, 8])
    remove_url("My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of http://www.geeksforgeeks.org")
    Summ(1, 2)
