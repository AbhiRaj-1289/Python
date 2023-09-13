# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

total = 0
for i in student_heights:
    total = total + i
number = 0
for j in student_heights:
   number += 1
average = round(total/number)
print("Average height = ",average)