def get_power_dictionary(n):
    dict = {}
    for num in range(1, n + 1):
        dict[num] = num ** 2
    return dict

if __name__ == '__main__':
    print(get_power_dictionary(8))
