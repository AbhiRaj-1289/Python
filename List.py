'''list1 = ['java','python',1997,2001]
print(list1[1:3])'''
'''list1 = ['java','python',1997,2001]
print(list1)
for i in list1:
	print(i)
length = len(list1)
print(length)
count = 0
while(count < length):
	print(list1[count])
	count += 1
list1[2] = 2022
print(list1)
list1.remove('python')
print(list1)
fruits = ['Orange','Banana','Apple']
yellow_fruits = ['Mango','Papaya']
print(fruits)
fruits.extend(yellow_fruits)
print(fruits + yellow_fruits)
newlist = fruits + yellow_fruits
print(newlist)
fruits = fruits + yellow_fruits
print(newlist)
fruits.insert(1,'Cherry')
print(fruits)
import itertools
list1 = ['a','b','c','d']
count = 0
for i in itertools.permutations(list1):
	print(i)
	count += 1
print("Total Combinations = ",count)
list1 = [1,2,1,2,12,1,2,1,2,2,2,4,3,2]
print(list1.count(2))
a = ['a','b','c']
n =[1,2,3]
x = [a,n]
print(x[1][1])
list1 = [[1,2],[],[3,4]]
for i in list1:
	if i == []:
		print(i, "Is Empty!")
	else:	
		print(i, "Has Data")
a = 45
print(f"value of a is {a}")'''
listA = [1,2,3,4]
#listA = listB ---> Shallow Copy
listB = list(listA) #----> Deep Copy
listA[2] = 100
print(f"listA - > {listA} at {id(listA)}")
print(f"listB - > {listB} at {id(listB)}")