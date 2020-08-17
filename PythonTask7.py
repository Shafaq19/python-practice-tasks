
def sort_comma_seperatedstring(sorted):
    def split(comma_seperated_string):
        list_of_words= list(comma_seperated_string.split(","))
        return ",".join(sorted(list_of_words))
    return split

sortedwithstr=sort_comma_seperatedstring(sorted)
print(sortedwithstr("without,hello,bag,world"))