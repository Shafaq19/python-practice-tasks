import re


def remove_url(strr):
    #starts with http://, has form letters/digits.letters upto a space is found
    regular_exp_for_urls = r"https?://[a-zA-Z0-9]+\.[a-z]+[^\s]+"
    return re.findall(regular_exp_for_urls, strr)


if __name__ == '__main__':
    print(remove_url(
        "My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of http://www.geeksforgeeks.org"))
