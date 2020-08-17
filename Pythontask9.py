from PythonTask7 import comma_string_to_list
import re


def check_password(password):
    if (len(password) > 6 and len(password) < 12):
        expression = r"(?=.*[a-z]+)(?=.*[A-Z]+)(?=.*[$#@]+)(?=.*[0-9]+)"
        if (re.match(expression, password) != None):
            return True
    return False


@comma_string_to_list
def check_passwords(comma_seperated_passwords):
    return [password for password in comma_seperated_passwords if check_password(password) == True]


print(check_passwords("ABd1234@1,a F1#,2w3E*,2We3345"))
