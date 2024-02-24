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
	def remove_one(self):
		return self.all_cards.pop(0)

	def add_cards(self,new_cards):
		if type(new_cards) == type([]):
			self.all_cards.extend(new_cards)
		else:
			self.all_cards.append(new_cards)
	def __str__():
		return f'This is player {self.name}'
	
	def hit(self):
		self.all_cards.append(new_cards)
	
	def stay(self):
		pass


class Dealer():
	def __init__(self):
		pass
	def remove_one(self):
		return self.all_cards.pop(0)
    
	def add_cards(self,new_cards):
		if type(new_cards) == type([]):
			self.all_cards.extend(new_cards)
		else:
			self.all_cards.append(new_cards)

	def hit_dealer(self):
		self.all_cards.append(new_cards)
			


#Game setup
reg_player = Player("You")
reg_player_cards = []
value_count_player = 0


Dealer = Dealer()
Dealer_cards = []
value_count_dealer = 0

#Game starts
game_on = True

Playing_Deck = Deck()
Playing_Deck.shuffle_deck()

	
while game_on == True: 

	for n in range(2):
		reg_player_cards.append(Playing_Deck.deal_one())
		Dealer_cards.append(Playing_Deck.deal_one())
	'''
	Bettings from the player with an input a type(int) or .digit check and
	if it's bigger than balance is checked by method, still try again has to be implemented
	'''	

	print(f"\nThose are the Player's cards: ")
	for item in reg_player_cards:
		print(item)
	for item in reg_player_cards:
		value_count_player += item.value
	print(f"The current sum of values is: {value_count_player}")

	print(f'\nThose are the Dealers cards:\n {Dealer_cards[0]} and the other one is hidden')

	
	# game after cards are dealt

	while value_count_player < 21:
		
		# user input and check whether it is valid

		while True:
			user_input = input("Do you want to hit or stay")

			if type(user_input) != str:
				print("please provide a string")
				continue 

			if user_input != "hit" or user_input != "stay":
				print("Please provide either 'hit' or 'stay'.\nPS:check the whitespaces")
				continue
			else:
				break

		#Input execution

		if user_input == "hit":
			reg_player.hit()
			value_count_player += reg_player_cards[-1]

		if user_input == "stay":
			break
	
	elif value_count_player == 21:
		print("Your cards's combined value is 21. Blackjack.")

	elif value_count_player > 21:
		print(f"Your cards' combined value is bigger than 21, it's: {reg_player_cards.value} ")
	
	print(f"The Dealer's second card is {Dealer_cards[1]}")

	for item in Dealer_cards:
		value_count_dealer += item.value

	while value_count_dealer < 21 or value_count_dealer < value_count_player :
		hit_dealer()
		value_count_dealer += Dealer_cards[-1]

	elif value_count_dealer > value_count_player:
		print(f" The Dealer's card have a higher total value: {value_count_dealer} than your cards {value_count_player}. \nYou loose! ")
		#Take money from the pot 

	elif value_count_dealer > 21:
		print(f"The Dealer's card's combined value is bigger than 21, it's: {reg_player_cards.value} ")
		print(" You win")
		#deposit money into player account

	elif value_count_player == value_count_dealer:
		print(f"Your and the dealer's cards have the same value: {value_count_dealer}. It's a draw")
	




	'''
	Do you want to play another round? = input with a game_on change in case of not
	to break out of bigger loop
	'''






