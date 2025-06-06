import random

print("Welcome to the Quiz Game...")

playing = input("Do you want to play the Quiz??(Type y for yes and N for no):")

if(playing.lower() != 'y'):
    quit()

print("Okay!! Let's Play")

questions = [
    "What does the term \"OOP\" stand for? ",
    "Which of these is NOT a programming paradigm?",
    "What is the purpose of Dijkstra's algorithm?",
    "What does SSL stand for?",
    "What does \"IDE\" stand for in programming?",
    "What is the binary representation of decimal 10?",
    "Which port does HTTP typically use?",
    "What type of language is Python?",
    "What is the purpose of a primary key?",
    "What is the main function of an operating system?"
]

options = [
    [("Object-Oriented Programming",True),("Operational Object Protocol",False),("Object-Oriented Protocol",False),("Operational Programming",False)],
    
    [("Functional",False),("Logical",False),("Structural",False),("Fractional",True)],
    
    [("Sorting numbers",False),("Finding shortest paths",True),("Encrypting data",False),("Compressing files",False)],
    
    [("Secure Socket Layer",True),("System Security Layer",False),("Software Security Layer",False),("Secure System Layer",False)],
    
    [("Integrated Development Environment",True),("International Development Environment",False),("Integrated Design Environment",False),("International Design Environment",False)],
    
    [("1000",False),("1010",True),("1100",False),("1110",False)],
    
    [("80",True),("443",False),("21",False),("25",False)],
    
    [("Compiled",False),("Interpreted",True),("Assembly",False),("Machine code",False)],
    
    [("To encrypt data",False),("To uniquely identify records",True),("To sort data alphabetically",False),("To create backups",False)],
    
    [("To manage hardware resources",True),("To create documents",False),("To design websites",False),("To program applications",False)]
]

quiz_data = []

for i in range (len(questions)):
    quiz_data.append(
        {
            "question":questions[i],
            "options":options[i]
        }
    )    

random.shuffle(quiz_data)

score = 0
letter_map = [
    'A','B','C','D'
]

for i,item in enumerate(quiz_data):
    print(f"\nQuestion {i+1}: {item['question']}")
    
    option_list = item["options"][:]
    random.shuffle(option_list)
    
    correct_letter = ""
    for i, (text, is_correct) in enumerate(option_list):
        print(f"{letter_map[i]}. {text}")
        if is_correct:
            correct_letter = letter_map[i]

    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == correct_letter:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer: {correct_letter}")
        print("Better Luck Next Time")
        break
    
print(f"\nYour final score: {score}/{len(quiz_data)}")
