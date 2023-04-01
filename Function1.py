'''def main():
	print("Hello World!")
if __name__ == '__main__':
	main()'''
#anonymous function
#lambda arguments: expression
'''multi = lambda x,y: x*y
print(multi(4,9))
result = lambda x: print(x,"is even") if x % 2 == 0 else print(x, "is odd")
result(4)'''
fun = lambda a,b,c,d,e : ((a+b)/(c+d))*e
print(fun(1,2,4,5,3))