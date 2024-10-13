import random

def get_reaction(is_correct):
    correct_reacts = [
        "Well done!",
        "Great job!",
        "Nice work!",
        "Exactly right!",
        "Spot on!",
        "You nailed it!",
        "Impressive!",
        "You got it!",
        "Fantastic!",
        "Awesome answer!"
    ]
    
    wrong_reacts = [
        "Not quite!",
        "Almost there!",
        "Good try!",
        "Keep going!",
        "Not this time!",
        "Close, but no!",
        "Nice effort!",
        "So close!",
        "Try again!",
        "You’ll get it next time!"
    ]
    
    random_reacts = ""
    if is_correct == True:
        random_reacts = random.choice(correct_reacts)
    else:
        random_reacts = random.choice(wrong_reacts)
         
    return random_reacts
        