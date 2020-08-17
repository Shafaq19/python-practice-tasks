import re

def remove_url(strr):
    regular_exp_for_urls = r"https?://[^\s]+"
    return re.findall(regular_exp_for_urls, strr)
print(remove_url("My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of http://www.geeksforgeeks.org"))