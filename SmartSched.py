# SmartSched System (Terminal Based):Manage Time and Tasks for PHINMA COC Main Campus Information Technology Students

tasks = []

while True:
    print("\n=== SmartSched System ===")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task name: ")
        deadline = input("Enter deadline: ")
        tasks.append([task, deadline, "Pending"])
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i][0]} - {tasks[i][1]} - {tasks[i][2]}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to mark.")
        else:
            num = int(input("Enter task number: "))
            tasks[num-1][2] = "Done"
            print("Task marked as done!")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            num = int(input("Enter task number: "))
            removed = tasks.pop(num-1)
            print(f"Deleted task: {removed[0]}")

    elif choice == "5":
        print("Thank you for using SmartSched System!")
        break

    else:
       print("Invalid choice. Please try again.")

