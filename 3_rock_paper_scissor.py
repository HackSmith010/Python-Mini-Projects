import random

ai_score = 0
user_score = 0
options = ["rock","paper","scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == "q":
        break
            
    if user_input not in options:
        print("Type among Rock/Paper/Scissor to play")
        continue
    
    random_num = random.randint(0,2)
    ai_pick = options[random_num]
    
    print(f"AI pick {ai_pick}")
        
    if user_input == "rock" and ai_pick == "scissor":
        print("You Won")
        user_score += 1
    elif user_input == "scissor" and ai_pick == "paper":
        print("You Won")
        user_score += 1
    elif user_input == "paper" and ai_pick == "rock":
        print("You Won")
        user_score += 1
        
    else:
        print("You Lost")
        ai_score += 1
        
print(f"Your Score: {user_score}")
print(f"AI Score: {ai_score}")
        
print("GoodBye!! See you again...")
        