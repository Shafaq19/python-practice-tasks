from collections import Counter

if __name__ == '__main__':
    with open("name") as f:
        #get names and counts
        names = Counter(f.readlines())

        #print
        print("Name\tCount")
        for name in names:
            print("%s \t %d" % (name.replace("\n", ""), names[name]))
