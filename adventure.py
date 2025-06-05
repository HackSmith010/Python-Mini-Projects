import os
import sys

def restart_script():
    print("\nRestarting the game...\n")
    python = sys.executable
    os.execv(python, [python] + sys.argv)

def game_over(reason=""):
    if reason:
        print(f"\n{reason}")
    print("Game Over. Thanks for playing!")
    quit()

def left_path():
    answer = input("\nYou arrive at a rushing river. There's a rickety bridge and a boat tied to a tree.\nWould you 'cross the bridge' or 'take the boat'? ").lower()
    
    if answer == "cross the bridge":
        troll_bridge()
    elif answer == "take the boat":
        waterfall_path()
    else:
        print("Not a valid option. Choose among the valid options.")
        left_path()

def troll_bridge():
    answer = input("\nA troll blocks your way on the bridge! He demands a riddle answer to pass.\nWould you 'attempt to answer the riddle' or 'retreat back'? ").lower()

    if answer == "attempt to answer the riddle":
        riddle = input("\nThe troll asks: 'What has roots as nobody sees, is taller than trees, up, up it goes, and yet never grows?' ").lower()
        if riddle == "mountain":
            print("\nCorrect! The troll lets you pass and you find a chest of gold!")
        else:
            game_over("Wrong answer! The troll throws you off the bridge.")
    elif answer == "retreat back":
        left_path()
    else:
        print("Not a valid option. Choose among the valid options.")
        troll_bridge()

def waterfall_path():
    answer = input("\nThe boat carries you peacefully down the river until you hear a roaring sound... it's a waterfall!\nWhat would you do? 'try to swim to shore' or 'accept your fate'? ").lower()
    if answer == "try to swim to shore":
        print("\nYou make it to shore safely, soaked but alive.")
    elif answer == "accept your fate":
        game_over("You fall over the waterfall.")
    else:
        print("Not a valid option. Choose among the valid options.")
        waterfall_path()

def right_path():
    answer = input("\nYou find an old cabin. It looks abandoned, but the door is slightly open.\nWould you 'enter the cabin' or 'walk past the cabin into the woods'? ").lower()

    if answer == "enter the cabin":
        cabin_ghost()
    elif answer == "walk past the cabin into the woods":
        bear_path()
    else:
        print("Not a valid option. Choose among the valid options.")
        right_path()

def cabin_ghost():
    answer = input("\nInside the cabin, a ghost asks you why you're here.\nWould you 'say you're lost' or 'say you're hunting treasure'? ").lower()
    if answer == "say you're lost":
        print("\nThe ghost guides you to a secret path leading to safety. You survive the night.")
    elif answer == "say you're hunting treasure":
        game_over("The ghost curses you for your greed. You are never seen again.")
    else:
        print("Not a valid option. Choose among the valid options.")
        cabin_ghost()

def bear_path():
    answer = input("\nA huge bear is blocking the path. It hasn’t noticed you yet.\nWould you 'sneak around the bear' or 'run away'? ").lower()
    if answer == "sneak around the bear":
        print("\nYou find a peaceful clearing with a helicopter landing pad. You're rescued!")
    elif answer == "run away":
        print("\nYou are starting the game from the beginning.")
        restart_script()
    else:
        print("Not a valid option. Choose among the valid options.")
        bear_path()

def start_game():
    name = input("Enter your name: ")
    print(f"\nHello {name}! Welcome to the Adventure Game!")

    is_ready = input("Are you ready to play? (yes/no): ").lower()
    if is_ready != "yes":
        print("Goodbye! See you again...")
        quit()

    print("\nLet's Start the Adventure Game...")

    answer = input("\nYou wake up in a dark forest. The air is damp, and the only light is from the moon above.\nThere are two paths ahead: one to the left and one to the right.\nWhich path do you choose? ('left' or 'right'): ").lower()

    if answer == "left":
        left_path()
    elif answer == "right":
        right_path()
    else:
        print("Not a valid option. Choose among the valid options.")
        start_game()

# Start the game
start_game()
