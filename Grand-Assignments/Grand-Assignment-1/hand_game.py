A = input()
B = input()

if A == "Rock":
    if B == "Paper":
        print("Anjali Wins")
    elif B == "Scissors":
        print("Abhinav Wins")
    else:
        print("Tie")

elif A == "Paper":
    if B == "Rock":
        print("Abhinav Wins")
    elif B == "Scissors":
        print("Anjali Wins")
    else:
        print("Tie")
    
else:
    if B == "Paper":
        print("Abhinav Wins")
    elif B == "Rock":
        print("Anjali Wins")
    else:
        print("Tie")
