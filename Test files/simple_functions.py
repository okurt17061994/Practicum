def hello (name="World"):
	print("Hi", name)

hello ("Jone")
hello()

print("_________________________")

def max2(x,y):
    if x > y:
		return x
	else:
		return y

print(max2(35,100))

print("_________________________")

def max3(x,y,z):
	return max2(x,max2(y,z))

print(max3(4.3,2.2,1.5))

print("_________________________")

def hello_separated (name="World", separator="-"):
	print("Hello,", name, sep=separator)

	hello_separated(separator="***", name="John")