from adventure_choices import adventure_story
import time
import os


# clear the terminal
def cls():
    os.system("cls" if os.name == "nt" else "clear")


cls()
name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

scenario_id = "1"

time.sleep(1)
while True:
    cls()
    scenario = adventure_story[scenario_id]

    # check if it's the end of the adventure
    if scenario["choice1_id"] == "" or scenario["choice2_id"] == "":
        print(scenario["scenario"])
        time.sleep(2)
        print("\n\nThe End")
        time.sleep(3)
        quit()

    scenario_1 = adventure_story[scenario["choice1_id"]]
    scenario_2 = adventure_story[scenario["choice2_id"]]

    # a = scenario1
    # b = scenario2
    answer = input(
        f'{scenario["scenario"]}:\n\n(a){scenario_1["choice"]}\n(b){scenario_2["choice"]}\n(q)Quit\n\n'
    )

    if answer.lower() == "q":
        print(
            "You bailed out of this adventure. You regret your decision the rest of your life."
        )
        time.sleep(5)
        quit()
    elif answer.lower() == "a":
        print(f"You chose to {scenario_1['choice']}")
        scenario_id = scenario["choice1_id"]
    elif answer.lower() == "b":
        print(f"You chose to {scenario_2['choice']}")
        scenario_id = scenario["choice2_id"]
    else:
        print("Please choose a valid answer")
    time.sleep(3)
