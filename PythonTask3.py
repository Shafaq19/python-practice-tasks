def GetPowerDictionary(n):
    dict={}
    for num in range(1,n+1):
        dict[num]=num**2
    return dict
print(GetPowerDictionary(8))