def menu():
    while True:
        try:
            print("--------------------📟​ Menu--------------------")
            print("Help: Type 'help' to know more about the commands.")
            print("Exit: Type 'exit' to exit the program.")
            print("Menu: Type 'menu' to return to the main menu.")
            print("1. Group1")
            print("2. Group2")
            print("3. Group3")
            print("4. Group4")
            print("5. Group5")
            prompt = input("Enter your command: ")
            if prompt == "help":
                print("Each command corresponds to a specific action, and you can select them by entering the corresponding number.")
                print("The initial commands are designed to group functions more systematically. For example, if you want to access the functions within a group, simply enter its number; you will then be able to access the commands associated with that group's title.")
                print("If you want to exit the program, simply type 'exit'.")
                print("If you want to return to the main menu, type 'menu'.")
            elif prompt == "exit":
                exit = True
                break
            elif prompt == "menu":
                print("You are already in the main menu.")
            elif prompt == "1":
                pass
            elif prompt == "2":
                pass
            elif prompt == "3":
                pass
            elif prompt == "4":
                pass
            elif prompt == "5":
                pass
            else:
                print("Invalid command. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
    if exit:
        print("Exiting the program. Goodbye!")

    