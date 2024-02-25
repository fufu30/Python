import random
#Global Variables

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11,}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

mon_enough = False
# Banc account
class Banc_acc():

	def __init__(self,owner,balance):
		self.owner = owner
		self.balance = balance
	
	def add_money(self,money_in):
		self.balance += money_in
		print("Money successfully deposited\n")

	def withdraw_money(self,money_out):
		global mon_enough	
		if money_out > self.balance:
			print("There is not enough money in your account")
			mon_enough = False
		if money_out <= self.balance:
			self.balance -= money_out
			print("Money successfully withdrawn")
			mon_enough = True
	def __str__(self):
		return f'Your Banc account has a balance of {self.balance}'

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
	
	def aces_check_and_adjust(self):
		ace_count_player = 0
		for item in self.cards:
			if item.rank =="Ace":
				ace_count_player += 1
		while self.value_count > 21 and ace_count_player > 0:
			self.value_count -=10
			ace_count_player -=1
		else:
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

	def aces_check_and_adjust(self):
		ace_count_dealer = 0
		for item in self.cards:
			if item.rank =="Ace":
				ace_count_dealer += 1
		while self.value_count > 21 and ace_count_dealer > 0:
			self.value_count -=10
			ace_count_dealer-=1
		else:
			pass


#Game setup
reg_player = Player("You")
reg_player_acc = Banc_acc("You",250)

Dealer = Dealer()


#Game starts
game_on = True



while game_on == True:

	game_decision = "Y"

	Playing_Deck = Deck()
	Playing_Deck.shuffle_deck()

	Dealer.cards = []
	Dealer.value_count = 0

	reg_player.cards = []
	reg_player.value_count = 0


	while True: 
		print(f"\n{reg_player_acc}")
		
		while True:
			player_bet = input("How much do you want to bet? ")

			if player_bet.isdigit() == False:
				print("Please provide a digit")
			else:
				player_bet_int = int(player_bet)
				reg_player_acc.withdraw_money(player_bet_int)
				if mon_enough == False:
					continue
				else:
					break



		for n in range(2):
			reg_player.cards.append(Playing_Deck.deal_one())
			Dealer.cards.append(Playing_Deck.deal_one())


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
				print(f"\nThose are Your cards: \n")
				for item in reg_player.cards:
					print(item)
				print(f"\nThe current sum of values is: {reg_player.value_count}")


			if user_input == "stay":
				break
		
		if reg_player.value_count == 21:
			print("Your cards's combined value is 21. Blackjack.")

		#Over 21 check reg_player
		reg_player.aces_check_and_adjust()

		if reg_player.value_count > 21:
			print(f"Your cards' combined value is bigger than 21, it's: {reg_player.value_count}")
			print(f"You loose! Casino takes the money! You have {reg_player_acc.balance} left")
			break
		
		#Dealer playing

		#Dealer's cards

		print(f"\nThe Dealer's second card is {Dealer.cards[1]}, so he has a {Dealer.cards[0]} and a {Dealer.cards[1]}")
		for item in Dealer.cards:
			Dealer.value_count += item.value
		print(f"\nThe Dealer's card's are worth {Dealer.value_count}")

		#Dealer action

		while Dealer.value_count < 21 and Dealer.value_count < reg_player.value_count :
			Dealer.hit_dealer(Playing_Deck.deal_one())
			Dealer.value_count += Dealer.cards[-1].value
			print("The Dealer's new cards are:")
			for item in Dealer.cards:
				print(item)
			print(f"They are now worth combined: {Dealer.value_count}")

		#checking results
		Dealer.aces_check_and_adjust()
		
		if Dealer.value_count > 21:
			print(f"The Dealer's card's combined value is bigger than 21, it's: {Dealer.value_count} ")
			reg_player_acc.add_money(player_bet_int*(3/2))
			print(f" You win! You now have {reg_player_acc.balance}, {player_bet_int*(3/2)} more than before.")
			break

		elif Dealer.value_count > reg_player.value_count and Dealer.value_count <= 21:
			print(f" The Dealer's card have a higher total value: {Dealer.value_count} than your cards {reg_player.value_count}.")
			print(f"You loose! Casino takes the money! You have {reg_player_acc.balance} left")
			break


		elif Dealer.value_count < reg_player.value_count and reg_player.value_count <= 21:
			print("Your cards are worth more than the dealer's!")
			reg_player_acc.add_money(player_bet_int*(3/2))
			print(f" You win! You now have {reg_player_acc.balance}, {player_bet_int*(3/2)} more than before.")
			break

		elif reg_player.value_count == Dealer.value_count:
			print(f"Your and the dealer's cards have the same value: {Dealer.value_count}. It's a draw")
			reg_player_acc.add_money(player_bet_int)
			print(f"You get your money back! You have {reg_player_acc.balance} left")
			break

	game_decision = "unknown"
	while game_decision != "Y" and game_decision != "N":
		game_decision = input("Do you want to play another round? Yes(Y) or No(N)")
	if game_decision == "Y":
		game_on = True

	elif game_decision == "N":
		game_on = False
	else:
		print("Please try again! Please input either 'Y' for Yes or 'N' for No")











