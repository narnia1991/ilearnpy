import time
from questions import get_questions
from audience_react import get_reaction

def start_quiz(): 
    print("quiz started")
    quiz_questions = get_questions()
    score = 0
    
    for index, i in enumerate(quiz_questions):
        time.sleep(2)
        
        print(f"\n{index + 1} of 10")
        print(i["question"])
        
        answer = input(f"{i["choices"]} (Q)uit\n\n")
        
        if(answer.capitalize()=="Q"):
            print(f"Thank you for playing. You scored {score} out of 10.\n See you next time!")
            time.sleep(1)
            quit()
        elif(answer==i["answer"]):
            print(get_reaction(True))
            score+=1
        else: 
            print(get_reaction(False))
            
    return score
        