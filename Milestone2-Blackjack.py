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
	
	def hit():
		pass
	
	def stay():
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

	def hit():
		pass

	def stay():
		pass

#Game setup
reg_player = Player("You")
reg_player_cards = []


Dealer = Dealer()
Dealer_cards = []

#Game starts
game_on = True

Playing_Deck = Deck()
Playing_Deck.shuffle_deck()

for n in range(2):
	reg_player_cards.append(Playing_Deck.deal_one())
	Dealer_cards.append(Playing_Deck.deal_one())

print(reg_player_cards)
print(f'Those are the Dealers cards: {Dealer_cards[0]} and the other one is hidden')

 












