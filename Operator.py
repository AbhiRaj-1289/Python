'''x = 24
y = 'ing'
mylist = [10,20,30,40]
mystring = 'Coding'
if(x is not  mylist):
	print("x is not present inn mylist")
else:
	print("x is present inn mylist")
if(y in mystring):
	print("y is present in mystring")
else:
	print("y is not present in mystring")
nice_weather = False
print("Go out for a walk" if nice_weather else "Watch a movie at home")
a = 10
b = 20
a=a*b
b=a//b
a=a//b
print(a,b)'''
"""a,b = 10,20
a,b = b,a
print(a,b)"""
'''a,b = (input("Enter Two Numbers :")).split(",")
c = int(a) + int(b)
print("Sum = ",c)'''
#Docstring
def myfun():
	"""
	working of myfun()is:
	usages: myfun(int(x),float(y))
	"""
	print("Hello")
#print(myfun.__doc__)
help(myfun)