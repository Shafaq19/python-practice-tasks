def Summ(num1,num2):
    """
    function which can compute the sum of two provided numbers.
    :param num1:
    :param num2:
    :return:
    """
    return num1+num2
if __name__ == '__main__':
    a,b=10,20
    print("sum of %d and %d is %d"%(a,b,Summ(a,b)))