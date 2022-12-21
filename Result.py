a = int(input("Enter Marks in Physics : "))
b = int(input("Enter Marks in Chemistry : "))
c = int(input("Enter Marks in Biology : "))
d = int(input("Enter Marks in Mathematics : "))
e = int(input("Enter Marks in English : "))
sum = int(a+b+c+d+e)
print("Total Marks =",sum)
percentage = (sum/500)*100
if percentage >= 80:
    print("1st Division")
elif percentage < 80 and percentage > 60:
    print("2nd Division")
elif percentage < 60 and percentage > 30:
    print("3rd Division")
else:
    print("Fail")
if a > 80:
    print("Distinction In Physics")
if b > 80:
    print("Distinction In Chemistry")
if c > 80:
    print("Distinction In Biology")
if d > 80:
    print("Distinction In Mathematics")
if e > 80:
    print("Distinction In English")
