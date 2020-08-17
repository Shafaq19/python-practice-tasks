strr=input("eneter string")
digits = [1 if x.isdigit() else 0 for x in strr]
letters =  [1 if x.isalpha() else 0 for x in strr]
print("Letters: %d"%sum(letters))
print("Letters: %d"%sum(digits))
