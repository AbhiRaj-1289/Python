elements = 0 
sum = 0 
number_list = []
n = int(input("Enter No. Of Elements : "))
for i in range(n):
    elements  = int(input())
    number_list.append(elements)
length = len(number_list)
for values in number_list:
    sum =  sum + values
print(f"Average = {sum/length}")    