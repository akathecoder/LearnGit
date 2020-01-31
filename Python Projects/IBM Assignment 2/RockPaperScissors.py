# Program to find the result of a Rock Paper Scissors game.

player1 = input("Enter input by Player 1 : ")
player2 = input("Enter input by Player 2 : ")

if player1 == "rock":
    if player2 == "rock":
        print("Tie")
    elif player2 == "paper":
        print("Player 2 Wins.")
    elif player2 == "scissors":
        print("Player 1 Wins.")
    else:
        print("Wrong input by Player 2.")

elif player1 == "paper":
    if player2 == "paper":
        print("Tie")
    elif player2 == "scissors":
        print("Player 2 Wins.")
    elif player2 == "rock":
        print("Player 1 Wins.")
    else:
        print("Wrong input by Player 2.")

elif player1 == "scissors":
    if player2 == "scissors":
        print("Tie")
    elif player2 == "rock":
        print("Player 2 Wins.")
    elif player2 == "paper":
        print("Player 1 Wins.")
    else:
        print("Wrong input by Player 2.")

else:
    print("Wrong input by Player 1.")