#Set --> It does not allow duplicate values.
#{}--> used for set definition
'''s1 = {5,7,8,9,4}
s2 = {1,2,3,4,5}
print(s1.union(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
s1.pop()
s1.add(10)
s1.remove(5)
print(s1)
print(s2)
set1 = {"Python","Django","Java","MySql"}
print(set1)'''
DaysA = {"Mon","Tues","Wed"}
DaysB = {"Wed","Thu","Fri","Sat","Sun"}
AllDays= DaysA | DaysB #---->Union
AllDays= DaysA & DaysB #----> Intersection
print(AllDays)
'''Months = {"Jan","Feb","Mar","Apr"}
Dates = {21,22,17}
Days.discard("Sun")
print(Days)
#for i in Days:
#	print(i)'''