'''class Dog:
	attr1 = "Mammel"
	attr2 = "Dog"
	def fun(self):
		print(f"I am a {self.attr1}")
		print(f"I am a {self.attr2}")
Rodger = Dog()
print(Rodger.attr1)
Rodger.fun()
print()'''
'''class Person:
	def __init__(self,name):
		self.name = name
	def say_hi(self):
		print("Hello, My name is ",self.name)
p = Person("Abhinav")
p.say_hi()'''
'''class Addition():
	first = 0
	second = 0 
	answer = 0
	def __init__(self,n1,n2):
		self.first = n1
		self.second = n2
	def calculate(self):
		self.answer = self.first + self.second
	def display(self):
		print("First Number = ",self.first)
		print("Second Number = ",self.second)
		print(f"Sum is {self.answer}")
num1 = int(input("Enter First Number: "))
num2 =  int(input("Enter Second Number: "))
add1 = Addition(num1,num2)
add1.calculate()
add1.display()'''
'''class Person(): #Parent Class
	def __init__(self,name,ecode):
		self.name = name
		self.ecode = ecode
	def display(self):
		print(f"Name {self.name} and ecode {self.ecode}")
emp = Person("Abhinav",101)
class Employee(Person):  #Child Class
	def __init__(self,name, ecode,salary,post):
		self.salary = salary
		self.post = post
		Person.__init__(self,name,ecode)
emp_details = Employee("Nikhil",102,2300,"Assistant")
emp_details.display()'''
'''class Parent1:
	def __init__(self):
		self.var1 = "Variable1"
		print("Parent1 Constructor")
class Parent2:
	def __init__(self):
		self.var2 = "Variable2"
		print("Parent2 Constructor")
class Derived(Parent1,Parent2):
	def __init__(self):
		Parent1.__init__(self)
		Parent2.__init__(self)
		print("Derived Class Constructor")
	def display(self):
		print(self.var1,self.var2)
obj = Derived()
obj.display()'''
class Superclass1:
	def info(self):
		print("Superclass1 method called!")
class Superclass2:
	def info(self):
		print("Superclass2 method called!")
class Derived(Superclass2, Superclass1):
	pass
d1 = Derived()
d1.info()