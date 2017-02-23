import random
def suit(n):
	if(n<14):
		return "hearts"
	elif(n<27):
		return "diamonds"
	elif(n<40):
		return "clubs"
	else:
		return "spades"
	
def card(n):
	num = n%13
	if(num == 1):
		return "Ace"
	elif(num == 11):
		return "Jack"
	elif(num == 12):
		return "Queen"
	elif(num == 0):
		return "King"
	else:
		return num

def draw(deck):
	another = True
	while(another):
		temp=random.randint(1,53)
		if not(temp in deck):
			another = False
	deck.append(temp)
	return temp

def tell(suit,num):
	print(str(num) + " of " + suit)

def score(n,hand):
	num = n%13
	if(num == 1 and hand<11):
		return 11
	elif(num == 11 or num == 12 or num == 0):
		return 10
	else:
		return num

def pmoney(money):
	return ('$%.2f'%money)
print("Welcome to BlackJack!\nPress enter to start game")
input()
money = 20.00
play = True
print("Your total is " + pmoney(money))
while play and money>0.00:
	badb = True
	while(badb):
		bet = float(input("What do you bet on this hand?\n$"))
		if bet>money:
			print("Remember, you only have " + pmoney(money) + "\nplease give a valid bet")
			badb = True
		elif bet <= 0:
			print("Your bet must be a non-zero positive number")
			badb = True
		else:
			badb = False
	print("\nDealing first cards...")
	hand = 0
	deck = list()
	deck.clear()
	first = draw(deck)
	second = draw(deck)
	tell(suit(first),card(first))
	tell(suit(second),card(second))
	hand = hand + score(first,hand)+score(second,hand)
	print("For a total of " + str(hand))
	cont = input("Hit?\n")
	if(cont == 'hit' or cont == 'Hit' or cont == 'yes' or cont == 'Yes' or cont == 'y' or cont == 'Y'):
		again = True
	else:
		again = False
	while again:
		print("Dealing next card...")
		ncard = draw(deck)
		tell(suit(ncard),card(ncard))
		hand += score(ncard,hand)
		print("For a new total of " + str(hand))
		if hand<22:
			cont = input("Hit?\n")
			if(cont == 'hit' or cont == 'Hit' or cont == 'yes' or cont == 'Yes' or cont == 'y' or cont == 'Y'):
				again = True
			else:
				again = False
		else:
			print("You busted!")
			again = False
	if hand < 17:
		money -= (bet*.5)
	elif hand <19:
		money = money
	elif hand <21:
		money += (bet*.5)
	elif hand == 21:
		money += bet
	else:
		money -= bet
	if money>=0.05:
		print("Your total is now " + pmoney(money))
		ans = input("Play again?")
		if (ans == "yes" or ans == "Yes" or ans == "Y" or ans == "y" or ans == "yeah" or ans == "Yeah"):
			play = True
		else:
			break
	else:
		print("You have less than " + pmoney(.05) + ", Try your luck elsewhere...")
		break
print("Your final total is " + pmoney(money))
print("Thank you for playing!")

	
