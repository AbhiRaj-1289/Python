#Python code to check if a number is palindrome or not

num = int(input("Enter a number : "))
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
  print(str(num)+" is a palindrome")
else:
  print(str(num)+" is not a palindrome")