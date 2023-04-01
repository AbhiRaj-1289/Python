#dict{key : values}
'''Car = {"Brand" : "Ford","Model" : "Mustang",
"Year" : 1964, "Brand" : "Honda"}
print(len(Car[""]))
Marks = {"Bill" : 90,"James" : 55, "Andrew" : 77}
name = input("Enter Name :")
for students in Marks:
	if(students == name):
		print(Marks[students])
dict1 = {"a" : 10, 'b':20,'c':30}
dict2 = {'d':40,'e':50}
dict3 = dict1 | dict2
print(dict3)
keys = ["Ten","Twenty","Thirty","Forty"]
values = [10,20,30,40]
res_dict = dict(zip(keys,values))
print(res_dict)'''
student = {1:{"Name":"Abhinav","Age":20},
			2:{"Name":"Nikhil","Age":18}}
student[3] = {"Name":"Ritesh","Age":22}
print(student)