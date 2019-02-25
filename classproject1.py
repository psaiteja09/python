import random

d=0
p=0

while True:
		r=input("Press r to roll, q to quit : ")

		if r == 'r' :
			d = random.randint(1,6)
			print("You get : ",random.randint(1,6))
			if d == 6:
				print("Congratulations,you can play now.")
				break
			else:
				print("Roll again, till you get 6.")

while True:
	r=input("Press r to roll, q to quit : ")

	if r == 'r' :
		d = random.randint(1,6)
		print("You get : ",d)

		p=p+d
		if p > 100:
			p = p-d
			print("Wait till you get", 100-p)

		print("Your new position is :",p)

	if p == 100:
		print("You Won!")
		exit()
	if p == 8:
		p = 37
		print("Wow, a ladder. Go to ",p)
	if p == 11:
		p = 2
		print("No, snake bit you. Go to ",p)
	if p == 12:
		p = 34
		print("Wow, a ladder. Go to ",p)
	if p == 25:
		p = 4
		print("No, snake bit you. Go to ",p)
	if p == 38:
		p = 9
		print("No, snake bit you. Go to ",p)
	if p == 40:
		p = 68
		print("Wow, a ladder. Go to ",p)
	if p == 52:
		p = 81
		print("Wow, a ladder. Go to ",p)
	if p == 65:
		p = 46
		print("No, snake bit you. Go to ",p)
	if p == 76:
		p = 97
		print("Wow, a ladder. Go to ",p)
	if p == 89:
		p = 70
		print("No, snake bit you. Go to ",p)
	if p == 93:
		p = 64
		print("No, snake bit you. Go to ",p)