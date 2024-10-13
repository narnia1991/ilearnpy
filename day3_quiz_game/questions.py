import random

questions = [
    {
        "question": "What is the capital of Japan?",
        "choices": ["Beijing", "Tokyo", "Seoul", "Bangkok"],
        "answer": "Tokyo"
    },
    {
        "question": "What color is the sun?",
        "choices": ["Blue", "Yellow", "Red", "Green"],
        "answer": "Yellow"
    },
    {
        "question": "How many days are in a leap year?",
        "choices": ["365", "366", "364", "380"],
        "answer": "366"
    },
    {
        "question": "What is 10 - 4?",
        "choices": ["6", "5", "4", "7"],
        "answer": "6"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Earth", "Venus", "Mars", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "What do you call a baby cat?",
        "choices": ["Kitten", "Puppy", "Cub", "Calf"],
        "answer": "Kitten"
    },
    {
        "question": "What is the main ingredient in bread?",
        "choices": ["Flour", "Sugar", "Water", "Salt"],
        "answer": "Flour"
    },
    {
        "question": "Which animal is known for its stripes?",
        "choices": ["Lion", "Tiger", "Bear", "Elephant"],
        "answer": "Tiger"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "choices": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": "Pacific"
    },
    {
        "question": "What is the capital of Italy?",
        "choices": ["Rome", "Madrid", "Paris", "Berlin"],
        "answer": "Rome"
    },
    {
        "question": "What is 5 times 6?",
        "choices": ["30", "28", "25", "32"],
        "answer": "30"
    },
    {
        "question": "What type of animal is a frog?",
        "choices": ["Mammal", "Bird", "Reptile", "Amphibian"],
        "answer": "Amphibian"
    },
    {
        "question": "What is the currency of the United States?",
        "choices": ["Dollar", "Euro", "Yen", "Pound"],
        "answer": "Dollar"
    },
    {
        "question": "What is the largest land animal?",
        "choices": ["Elephant", "Giraffe", "Rhino", "Hippo"],
        "answer": "Elephant"
    },
    {
        "question": "How many sides does a triangle have?",
        "choices": ["2", "3", "4", "5"],
        "answer": "3"
    },
    {
        "question": "What is the main language spoken in France?",
        "choices": ["English", "French", "German", "Spanish"],
        "answer": "French"
    },
    {
        "question": "What do you call a group of fish?",
        "choices": ["Herd", "Pack", "School", "Swarm"],
        "answer": "School"
    },
    {
        "question": "What is the tallest mountain in the world?",
        "choices": ["K2", "Kangchenjunga", "Mount Everest", "Lhotse"],
        "answer": "Mount Everest"
    },
    {
        "question": "What is 3 + 5?",
        "choices": ["8", "7", "9", "6"],
        "answer": "8"
    },
    {
        "question": "Which fruit is known as the 'king of fruits'?",
        "choices": ["Mango", "Durian", "Apple", "Banana"],
        "answer": "Durian"
    },
    {
        "question": "What do you call the first meal of the day?",
        "choices": ["Lunch", "Dinner", "Breakfast", "Brunch"],
        "answer": "Breakfast"
    },
    {
        "question": "What is the shape of a basketball?",
        "choices": ["Square", "Rectangle", "Circle", "Oval"],
        "answer": "Circle"
    },
    {
        "question": "What is the fastest land animal?",
        "choices": ["Cheetah", "Lion", "Horse", "Elephant"],
        "answer": "Cheetah"
    },
    {
        "question": "What is the capital of Canada?",
        "choices": ["Toronto", "Vancouver", "Ottawa", "Montreal"],
        "answer": "Ottawa"
    },
    {
        "question": "What instrument is used to measure temperature?",
        "choices": ["Barometer", "Thermometer", "Hygrometer", "Anemometer"],
        "answer": "Thermometer"
    },
    {
        "question": "What color are emeralds?",
        "choices": ["Red", "Green", "Blue", "Yellow"],
        "answer": "Green"
    },
    {
        "question": "What is 15 divided by 3?",
        "choices": ["4", "5", "6", "3"],
        "answer": "5"
    },
    {
        "question": "What is the main gas in the air we breathe?",
        "choices": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": "Nitrogen"
    },
    {
        "question": "What do you call a person who studies plants?",
        "choices": ["Botanist", "Biologist", "Geologist", "Astronomer"],
        "answer": "Botanist"
    },
    {
        "question": "Which planet is closest to the sun?",
        "choices": ["Venus", "Earth", "Mercury", "Mars"],
        "answer": "Mercury"
    },
    {
        "question": "How many colors are in a rainbow?",
        "choices": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "What is the main ingredient in sushi?",
        "choices": ["Rice", "Noodles", "Bread", "Potatoes"],
        "answer": "Rice"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "choices": ["Gold", "Iron", "Diamond", "Quartz"],
        "answer": "Diamond"
    },
    {
        "question": "What is the capital of Australia?",
        "choices": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
        "answer": "Canberra"
    },
    {
        "question": "What is 9 + 10?",
        "choices": ["18", "19", "20", "21"],
        "answer": "19"
    },
    {
        "question": "Which instrument has 88 keys?",
        "choices": ["Guitar", "Violin", "Piano", "Flute"],
        "answer": "Piano"
    },
    {
        "question": "What type of animal is a salmon?",
        "choices": ["Fish", "Mammal", "Bird", "Reptile"],
        "answer": "Fish"
    },
    {
        "question": "What is the chemical symbol for water?",
        "choices": ["H2O", "O2", "CO2", "NaCl"],
        "answer": "H2O"
    },
    {
        "question": "What is the smallest planet in our solar system?",
        "choices": ["Mars", "Earth", "Mercury", "Venus"],
        "answer": "Mercury"
    },
    {
        "question": "What is 20 - 7?",
        "choices": ["12", "13", "14", "15"],
        "answer": "13"
    },
    {
        "question": "What fruit is known for having seeds on the outside?",
        "choices": ["Banana", "Strawberry", "Blueberry", "Kiwi"],
        "answer": "Strawberry"
    },
    {
        "question": "What do you call a baby sheep?",
        "choices": ["Calf", "Puppy", "Lamb", "Kitten"],
        "answer": "Lamb"
    },
    {
        "question": "What is the hardest rock?",
        "choices": ["Granite", "Basalt", "Marble", "Diamond"],
        "answer": "Diamond"
    },
    {
        "question": "What is the name of the fairy in Peter Pan?",
        "choices": ["Tinkerbell", "Cinderella", "Belle", "Ariel"],
        "answer": "Tinkerbell"
    },
    {
        "question": "What do you call the process of water turning into vapor?",
        "choices": ["Condensation", "Evaporation", "Precipitation", "Sublimation"],
        "answer": "Evaporation"
    }]

def get_questions():
    random.shuffle(questions)
    return questions[0:9]