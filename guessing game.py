from random import*
rand_num= randint(1,100)
count = 1
previous_difference = 0

#first input

guess = int(input("Guess a number between 1 and 100: "))
if guess != rand_num:
	if guess< 1 or guess> 100:
		print("Out of bounds")
	elif abs(rand_num-guess) <= 10:
		print("Warm")
	elif abs(rand_num - guess) >= 10:
		print("Cold")
	previous_difference = (rand_num - guess)
	guess = int(input("Take another guess: "))
	count += 1  
else: 
	print(" Congratulations, you won! \nIt took you one guess!") 

# Game progress
while guess != rand_num:
	if guess< 1 or guess> 100:
		print("Out of bounds")
	elif abs(rand_num - guess) <= abs(previous_difference):
		print("Warmer")
	elif abs(rand_num - guess) >= abs(previous_difference) :
		print("Colder")
	previous_difference = (rand_num - guess)
	guess = int(input("Take another guess: "))
	count += 1  
	
else:
	print(f"Congratulations, you won! \nIt took you {count} guesses!")