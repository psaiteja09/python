#creating a function with no parameters

def func1():
	print("hi")
	print("hello")
func1()



#function with a parameter
def func2(a):#a=1
	print("hi\t",a)

func2("abs")


#with 2/3 parameters
def func3(a,b,c):#a=2,b=5,c=6
	d=a+b+c
	print(a,b,c,d)
func3(2,5,6)

#with default parameter
def func4(university="IITB"):
	print("I am in"+"\t"+university)
func4("IITG")
func4("IITD")
func4()

#return statement

def func9(a,b,c):#a=2,b=5,c=6
	d=a+b+c
	return d
e=func9(2,5,6)
print("func9 resultis",e)



#calling of one function  from ather and return statements

def func5(a,b):
	print("hi other function")
	c=a+b
	return c

def func6():
	print("hello,I am going to all other function")
	s=func5(2,7)
	print("addition is ",s)
func6()



#func2("saiteja")                                                                                                                                                                                                                            