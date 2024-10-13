from quiz import start_quiz

print("Welcome to my computer quiz")

def accept_play():
    playing = input("Do you want to play? (Y)es (N)o \n")
    if(playing.capitalize() == "Y"):
        print("cool")
        score = start_quiz()
        
        greeting = ""
        if score > 5 : greeting = 'Congratulations!'
        else: "Nice try!"
        
        print(f"{greeting} you got {score} out of 10!")
        
    elif(playing.capitalize() == "N"):
        print("See you next time")
        quit()
    else: 
        print("Please select valid choice")
        accept_play()
    
accept_play()