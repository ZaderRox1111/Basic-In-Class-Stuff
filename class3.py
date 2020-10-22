
def determine_rps_outcome(p1_choice, p2_choice):
    if (p1_choice == "rock" and p2_choice == "scissors") or (p1_choice == "paper" and p2_choice == "rock") or (p1_choice == "scissors" and p2_choice == "paper"):
        return "Player 1 wins"

    if (p2_choice == "rock" and p1_choice == "scissors") or (p2_choice == "paper" and p1_choice == "rock") or (p2_choice == "scissors" and p1_choice == "paper"):
        return "Player 2 wins"

    if p1_choice == p2_choice:
        return "tie"

def det_rps_outcome_using_dict(p1_choice, p2_choice):
    moves = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }

    if moves[p1_choice] == p2_choice:
        return "p1 wins"
    elif moves[p2_choice] == p1_choice:
        return "p2 wins"
    elif p1_choice == p2_choice:
        return "tie"


p1 = input("p1: ")
p2 = input("p2: ")

print(det_rps_outcome_using_dict(p1,p2))
