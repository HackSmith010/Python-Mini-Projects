print("Welcome to the Treasure Cave!")

inventory = []

while True:
    print("\n" + "="*30)
    print("      MAIN MENU")
    print("="*30)
    print("1. Start the Adventure")
    print("2. Check Your Inventory")
    print("3. Quit Game")
    print("="*30)

    menu_choice = input("Enter your choice (1, 2, or 3): ")

    if menu_choice == '1':
        print("\n" + "-"*40)
        print("You stand at the entrance of a dark, spooky cave.")
        print("To light your way, you can take a 'torch' or a 'lantern'.")
        print("-"*40)
        
        choice1 = input("What do you choose? Type 'torch' or 'lantern': ").lower()

        if choice1 == 'torch':
            print("\nWith the torch held high, you enter the cave. The flame dances, revealing two paths.")
            print("One path leads across a rickety 'rope' bridge.")
            print("The other path leads across a sturdy 'stone' bridge.")
            
            choice2 = input("Which path do you take? Type 'rope' or 'stone': ").lower()

            if choice2 == 'stone':
                print("\nYou safely cross the stone bridge. You see a treasure chest!")
                
                if "Golden Key" in inventory:
                    print("You use the Golden Key you found earlier to open the chest.")
                    print("Inside, you find a pile of gold and a magnificent crown!")
                    print("🎉 --- CONGRATULATIONS, YOU WIN! --- 🎉")
                    inventory.append("Golden Crown")
                    
                else:
                    print("The chest is locked and you don't have a key.")
                    print("Maybe you missed something? You decide to turn back.")

            elif choice2 == 'rope':
                print("\nYou step onto the rope bridge. It creaks ominously... and then snaps!")
                print("You fall into the dark chasm below.")
                print("--- GAME OVER ---")
            
            else:
                print("\nInvalid choice. A gust of wind extinguishes your torch, leaving you in darkness.")
                print("--- GAME OVER ---")

        elif choice1 == 'lantern':
            print("\nYou pick up the dim lantern. As you step into the cave, you find a small, shiny key on the ground.")
            print("You have found the Golden Key!")
            inventory.append("Golden Key")
            
            print("You continue deeper, but the lantern's light is too weak. You stumble and fall into a pit.")
            print("--- GAME OVER ---")

        else:
            print("\nInvalid choice. You hesitate for too long and a giant spider blocks the way.")
            print("--- GAME OVER ---")

    elif menu_choice == '2':
        print("\n--- YOUR INVENTORY ---")
        
        if not inventory:
            print("Your inventory is empty.")
        else:
            for item in inventory:
                print(f"- {item}")
        
        print("--------------------")

    elif menu_choice == '3':
        print("\nThank you for playing!")
        break 


    else:
        print("\nInvalid choice. Please enter 1, 2, or 3.")