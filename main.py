while True:
    print("\n*** Bhanu's Daily Tasks ***")
    print("1. See my tasks")
    print("2. Add a new task")
    print("3. Quit program")
    
    choice = input("Select an option (1-3): ")
    
    if choice == '1':
        try:
            with open("tasks.txt", "r") as file:
                print("\nSaved tasks:")
                print(file.read())
        except FileNotFoundError:
            print("\nYou don't have any tasks saved yet.")
            
    elif choice == '2':
        new_task = input("What do you need to do? ")
        with open("tasks.txt", "a") as file:
            file.write(new_task + "\n")
        print("Successfully saved!")
        
    elif choice == '3':
        print("See you later!")
        break
        
    else:
        print("That is not a valid choice, please try again.")