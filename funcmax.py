def maximum(a,b,c):#a=16,b=29,c=23

	if(a>b) and (a>c):
		largest = a

	elif(b>a) and (b>c):
		largest = b

	else:
		largest = c

	return largest
print(maximum(16,29,23))