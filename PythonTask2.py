def PrintNumbers(upper_limit, lower_limit):
    """
     prints all such numbers which are divisible by 7 but are not a multiple of 5, between lower limit and upper limit (both included).
    :param upper_limit:
    :param lower_limit:
    :return:
    """
    lis = ""
    for num in range(lower_limit, upper_limit + 1):
        if (num % 7 == 0 and num % 5 != 0):
            lis += str(num) + ","
    print(
        "All numbers which are divisible by 7 but are not a multiple of 5, between 1000 and 2000 (both included) are : %s" % lis[
                                                                                                                             :-1])


if __name__ == '__main__':
    PrintNumbers(2000, 1000)
