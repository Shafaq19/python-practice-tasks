
def comma_string_to_list(function):
    def split(comma_seperated_string):
        list_of_words= list(comma_seperated_string.split(","))
        return ",".join(function(list_of_words))
    return split

sorted=comma_string_to_list(sorted)
if __name__ == '__main__':
    print(sorted("without,hello,bag,world"))