def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    if not tasks:
        print("📭 No tasks found.")
    else:
        print("\n📝 To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Done\n4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("✅ Task added.")
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            display_tasks(tasks)
            if tasks:
                try:
                    done = int(input("Enter task number to mark as done: "))
                    removed = tasks.pop(done - 1)
                    save_tasks(tasks)
                    print(f"✅ Task '{removed}' marked as done.")
                except:
                    print("❌ Invalid number.")
        elif choice == "4":
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()