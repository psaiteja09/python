import random

d=0
p=0
snl={8:37,13:34,38:9,11:2,28:4,40:68,52:81,76:97,65:46,93:64,89:70}
def rolldice():
	return random.randint(1,6)

#Get 1or 6 on the dice to rnter the game.
while True:
	r=input("Press r to rollthe dice, q to quit : ")
	if r == 'r' :
		d = rolldice()
		print("You get : ",d)

		if d == 6 or d == 1 :
			print("Congratulations,you're in game!")
			break
		else:
			print("you need to get 6 or 1 to start the game. Try again.")
	elif r =='q':
		exit()
while True:
	r=input("Press r to rollthe dice, q to quit : ")
	if r =='r':
		d = rolldice()
		print("You got",d)
		p = p+d
		if p == 100:
			print("Hurray! You Won!")
			exit()
		if p>100:
			p = p-d
			print("You need to get",100-p,"to reach home.")
		print("Your new position is",p)
		if p in snl:
			if p<snl[p]:
				print("Wow, you got a ladder.")
			else:
				print("Oooops, you got swallowed by a huge snake.")

			p = snl[p]
			print("move to ",p)
		elif r == 'q':
			exit()