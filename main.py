while True:
    print("\n--- My Task Manager ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Exit")
    
    choice = input("Enter 1, 2, or 3: ")
    
    if choice == '1':
        try:
            with open("tasks.txt", "r") as file:
                print("\nHere are your tasks:")
                print(file.read())
        except FileNotFoundError:
            print("\nNo tasks saved yet!")
            
    elif choice == '2':
        new_task = input("Type your new task: ")
        with open("tasks.txt", "a") as file:
            file.write(new_task + "\n")
        print("Task saved!")
        
    elif choice == '3':
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice, try again.")