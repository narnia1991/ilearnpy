import random

user_score = 0
computer_score = 0

options = ["R","P","S"]

while True: 
    user_input = input("Type (R)ock (P)aper (S)cissors or (Q)uit: \n").capitalize()
    if user_input == "Q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    #  rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    
    print(f"Computer picked {computer_pick}.")
    
    if (user_input == "R" and computer_pick == "S") or (user_input == "P" and computer_pick == "R") or (user_input == "S" and computer_pick == "P"):
        print("You won!")
        user_score +=1
    else:
        computer_score +=1

print(f"You scored {user_score} points.")
print(f"Computer scored {computer_score} points.")

quit()