'''num = [10,20,40,30,60,50]
num.sort()#----> Ascending Order
num.sort(reverse=True)#---> Descending Order
print(num)
str1 = ['Fish','Banana','Cat','Apple','Dog']
str1.sort()
print(str1)
list1 = ['hello','python']
tuple1 = tuple(list1)
print(tuple1)
tuple1 = tuple('Python')
print(tuple1)
tuple1 = (1,2,3)
tuple2 = ('Python','Django')
tuple3 = (tuple1,tuple2)
print(tuple3[1][1])
tuple1 = ('Python','for','freshers')
a,b,c = tuple1
print(a)
print(b)
print(c)'''
name = ["Manish","Naveen","Shefali","Amrita"]
roll_no = [24,17,35,21]
course = ["B.Com","M.Sc.","B.Tech.","M.Tech."]
zip_obj = zip(name,roll_no,course)
print(list(zip_obj))