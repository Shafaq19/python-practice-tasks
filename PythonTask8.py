"""
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Task 8
"""
input=[1,2,3,4,5,6,7,8,9]
newlst= [str(i) for i in input if i%2!=0]
print(",".join(newlst))