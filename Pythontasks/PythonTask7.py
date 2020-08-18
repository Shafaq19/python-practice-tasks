def comma_string_to_list(function):
    def split(comma_seperated_string):
        list_of_words = list(comma_seperated_string.split(","))
        return ",".join(function(list_of_words))

    return split


if __name__ == '__main__':
    sorted = comma_string_to_list(sorted)
    print(sorted("without,hello,bag,world"))
