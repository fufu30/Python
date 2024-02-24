#Global variables:
fieldls = [" "," "," "," "," "," "," "," "," "]
fieldcoordls = ["1","2","3","4","5","6","7","8","9"]
already_used_ls = []
already_used = True
acceptable_range=list(range(1,10))
game_choice = "Y"
someone_won = False	
tie = False

#Functions
def display_coord_board():
	print(f" {fieldcoordls[0]}| {fieldcoordls[1]} | {fieldcoordls[2]}\n---------\n {fieldcoordls[3]}| {fieldcoordls[4]} | {fieldcoordls[5]}\n---------\n {fieldcoordls[6]}| {fieldcoordls[7]} | {fieldcoordls[8]}\n")

def display_board():
	print(f" {fieldls[0]}| {fieldls[1]} | {fieldls[2]}\n---------\n {fieldls[3]}| {fieldls[4]} | {fieldls[5]}\n---------\n {fieldls[6]}| {fieldls[7]} | {fieldls[8]}\n")

def user_choice():
    global already_used_ls  
    choice = "wrong"
    within_range = False
    
    while True:  
        choice = input("Please enter a number between 1 and 9: ")
        
        if not choice.isdigit():
            print("Sorry, that's not a digit.")
            continue  
        
        choice_int = int(choice)  
        if choice_int not in acceptable_range:
            print("Sorry, you are out of acceptable range.")
            continue  
        
        if choice_int -1 in already_used_ls:
            print("This position is already taken, please choose another.")
            continue  
        
        break  
    return choice_int - 1  # Adjust for 0-indexing


def game_on_choice():
	global game_choice
	game_choice = input("Do you want to continue playing (Y or N)?")
	while game_choice not in ["Y", "N"]:
		print("Sorry, I do not understand you. Please try again!")
		game_choice = input("Do you want to continue playing (Y or N)?")

#Gamelogik
def win_check_x():
	global someone_won 
	x = 0
	for x in range(0,9,3):
			if fieldls[x] == "x" and fieldls[x+1] == "x" and fieldls[x+2] == "x":
				someone_won = True
				print("Congratulations, you won! ")
				return someone_won

				
	for x in range(0,3):
			if fieldls[x] == "x" and fieldls[x+3] == "x" and fieldls[x+6] == "x":
				someone_won = True
				print("Congratulations, you won! ")
				return someone_won

	if fieldls[0] == "x" and fieldls[4] == "x" and fieldls[8] == "x":
				someone_won = True
				print("Congratulations, you won!")
				return someone_won
	
	if fieldls[2] == "x" and fieldls[4] == "x" and fieldls[6] == "x":
				someone_won = True
				print("Congratulations, you won!")
				return someone_won

def win_check_o():
	global someone_won 
	x = 0
	for x in range(0,9,3):
			if fieldls[x] == "o" and fieldls[x+1] == "o" and fieldls[x+2] == "o":
				someone_won = True
				print("Congratulations, you won! ")
				return someone_won

				
	for x in range(0,3):
			if fieldls[x] == "o" and fieldls[x+3] == "o" and fieldls[x+6] == "o":
				someone_won = True
				print("Congratulations, you won! ")
				return someone_won

	if fieldls[0] == "o" and fieldls[4] == "o" and fieldls[8] == "o":
		someone_won = True
		print("Congratulations, you won!")
		return someone_won
	
	if fieldls[2] == "o" and fieldls[4] == "o" and fieldls[6] == "o":
		someone_won = True
		print("Congratulations, you won!")
		return someone_won

def tie_check():
	occup_field = 0
	global tie 
	for item in fieldls:
		if item == "x" or item == "o":
			occup_field +=1
		else:
			continue
	if occup_field == 9:
		tie = True
		print("Game over! It's a tie!\n")


#Executing code
display_coord_board()

while game_choice == "Y" and someone_won == False and tie == False :
	
#Player 1's go
	display_board()

	position = user_choice() 
	already_used_ls.append(position)
	
	fieldls[position] = "x"  

	display_board()

	win_check_x()
	if someone_won == True:
		break 

	tie_check()
	if tie == True:
		break

#Player 2's go
	position = user_choice() 
	already_used_ls.append(position)
	fieldls[position] = "o"  
	
	win_check_o()

	tie_check()

	display_board()

#Game continue check
	game_on_choice()


else:
	print("Game aborted\n")

