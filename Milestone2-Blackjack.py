import random
#Global Variables

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11, 'Ace':1}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# Banc account
class Banc_acc():
	def __init__(self,owner, balance):
		self.owner = owner
		self.balance = balance
	
	def add_money(money_in):
		self.balance += money_in
		print("Money successfully withdrawn")

	def withdraw_money(money_out):
		if money_out > self.balance:
			print("There is not enough money in your account")
		if money_out <= self.balance:
			balance -= money_out
			print("Money successfully withdrawn")

#Cards
class Card():
	def __init__(self,suit,rank,):
		self.rank = rank
		self.suit = suit
		self.value = values[rank]

	def __str__(self):
		return f'{self.rank} of {self.suit}'

#Decks
class Deck():
	def __init__(self):
		self.new_deck=[]

		for suit in suits:
			for rank in ranks:
				self.new_deck.append(Card(suit,rank))

	def shuffle_deck(self):
		random.shuffle(self.new_deck)
	
	def deal_one(self):
		return self.new_deck.pop()

	def remove_one(self):
		self.new_deck.pop(0)

	def __str__(self):
		for n in self.new_deck:
			print(n)


#Player
class Player():
	def __init__(self,name):
		self.name = name
		self.cards = []
		self.value_count = 0

	def __str__():
		return f'This is player {self.name}'
	
	def hit(self,new_cards):
		self.cards.append(new_cards)
	
	def stay(self):
		pass


class Dealer():
	def __init__(self):
		self.name = "Dealer"
		self.cards = []
		self.value_count = 0

	def __str__():
		return 'This is the Dealer'
	
	def hit_dealer(self,new_cards):
		self.cards.append(new_cards)
	
	def stay(self):
		pass
		







#Game setup
reg_player = Player("You")

Dealer = Dealer()


#Game starts
game_on = True

Playing_Deck = Deck()
Playing_Deck.shuffle_deck()

	
while game_on == True: 

	for n in range(2):
		reg_player.cards.append(Playing_Deck.deal_one())
		Dealer.cards.append(Playing_Deck.deal_one())
	'''
	Bettings from the player with an input a type(int) or .digit check and
	if it's bigger than balance is checked by method, still try again has to be implemented
	'''	

	print(f"\nThose are the Your cards: ")
	for item in reg_player.cards:
		print(item)
	
	for item in reg_player.cards:
		reg_player.value_count += item.value
	print(f"The current sum of values is: {reg_player.value_count}")

	print(f'\nThose are the Dealers cards:\n {Dealer.cards[0]} and the other one is hidden')

	
	# game after cards are dealt

	while reg_player.value_count < 21:
		
		# user input and check whether it is valid

		while True:
			user_input = input("Do you want to hit or stay? ")

			if user_input != "hit" and user_input != "stay":
				print("Please provide either 'hit' or 'stay'.\nPS:check the whitespaces\n")
				continue
			else:
				break

		#Input execution

		if user_input == "hit":
			reg_player.hit(Playing_Deck.deal_one())
			reg_player.value_count += reg_player.cards[-1].value
			print(f"\nThose are Your cards: ")
			for item in reg_player.cards:
				print(item)
			print(f"The current sum of values is: {reg_player.value_count}")


		if user_input == "stay":
			break
	
	if reg_player.value_count == 21:
		print("Your cards's combined value is 21. Blackjack.")

	elif reg_player.value_count > 21:
		print(f"Your cards' combined value is bigger than 21, it's: {reg_player.value_count} ")
		break
	
	print(f"The Dealer's second card is {Dealer.cards[1]}, so he has a {Dealer.cards[0]} and a {Dealer.cards[1]}")

	for item in Dealer.cards:
		Dealer.value_count += item.value

	while Dealer.value_count < 21 and Dealer.value_count < reg_player.value_count :
		hit_dealer(Playing_Deck.deal_one())
		Dealer.value_count += Dealer_cards[-1]

	if Dealer.value_count > reg_player.value_count:
		print(f" The Dealer's card have a higher total value: {Dealer.value_count} than your cards {value_count_player}. \nYou loose! ")
		#Take money from the pot 

	elif Dealer.value_count > 21:
		print(f"The Dealer's card's combined value is bigger than 21, it's: {reg_player.value_count} ")
		print(" You win")
		#deposit money into player account

	elif reg_player.value_count == Dealer.value_count:
		print(f"Your and the dealer's cards have the same value: {Dealer.value_count}. It's a draw")





	'''
	Do you want to play another round? = input with a game_on change in case of not
	to break out of bigger loop
	'''






