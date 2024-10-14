import random
def number_guessing_game():
    while True:
        max_num = input("Type any number greater than 0: \n (Q)uit\n")
        if max_num.capitalize()=="Q":
            print("See you next time")
            quit()
            
        if max_num.isdigit:
            if int(max_num)<2:
                print("Please input a number greater than 2")
                continue
            max_num = int(max_num)
            break
        else: 
            print("Please input a number next time. \n")
            continue
            
    print("game started")
    random_num = random.randint(0, max_num)
    user_guess_count = 0

    while True: 
        user_guess_count += 1
        user_guess = input("Guess the number: ")
        
        if user_guess.isdigit:
            user_guess = int(user_guess)
        else: 
            print("Please input a number next time \n")
            
        if user_guess == random_num:
            print("Great Job! You got it in", user_guess_count, "guesses!")
            play_again = input("Do you want to play again? (Y)es / Press any key to exit\n")
            if(play_again.capitalize() == "Y"):
                number_guessing_game()
            print("Thank you for playing!")
            quit()
        elif user_guess > random_num:
            print("Guess is higher")
        else: 
            print("Guess is lower")
    
number_guessing_game()