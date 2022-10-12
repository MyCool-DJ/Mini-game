#day17 of 100days-of-code via REplit
from getpass import getpass as input

print("Welcome to the classic game of Rock, Paper, Scissors!")
print("")

player1_score = 0
player2_score = 0

while True:
	
	player1 = input("Player 1, enter your first turn: ")
	player2 = input("Player 2, enter your first turn: ")
	print("OK, let's see!")


	if (player1 == "Rock" or player1 == "rock"
	        or player1 == "🪨") and (player2 == "Paper" or player2 == "paper"
	                                or player2 == "📄"):
		    print("Player 2 wins!!")
	elif (player1 == "Paper" or player1 == "paper" or player1
		      == "📄") and (player2 == "Rock" or player2 == "rock" or player2 == "🪨"):
		    print("Player 1 wins!!")
	elif (player1 == "Rock" or player1 == "rock" or player1 == "🪨") and (
		        player2 == "Scissors" or player2 == "scissors") or player2 == "✂️":
		    print("Player 1 wins!")
	elif (player1 == "Scissors"
		      or player1 == "scissors") and (player2 == "Rock" or player2 == "rock"
		                                     or player2 == "🪨"):
		    print("Player 2 wins!")
	elif (player1 == "Paper" or player1 == "paper"
		      or player1 == "📄") and (player2 == "Scissors" or player2 == "scissors"):
		    print("Player 2 wins!")
	elif (player1 == "Scissors" or player1 == "scissors"
		      or player1 == "✂️") and (player2 == "Paper" or player2 == "paper"
		                               or player2 == "📄"):
		    print("Player 1 wins!")
	else:
		print("Draw!")
		continue

