print("📚 Student Task Manager")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete All Tasks")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        with open("tasks.txt", "a") as f:
            f.write(task + "\n")

    elif choice == "2":
        with open("tasks.txt") as f:
            print("\nTasks:")
            print(f.read())

    elif choice == "3":
        open("tasks.txt", "w").close()
        print("🗑️ All tasks deleted!")

    elif choice == "4":
        break
