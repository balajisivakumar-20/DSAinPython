#unpack a collection - collection of variables

cars = ["BMW", "Audi", "Mercedes", "Jaguar"]
a, b, c, d = cars
print(a)
print(b)
print(c)
print(d)

print (a,b,c,d)

number = "m3"

print ( a, number)

def my_function():
	global x #always avoid using global variables
	x = "fantastic"
	print("python is "+x)
my_function()
print(x)

def my_func():
	print("python is really "+x)

my_func()




