def load_tasks():
    try:
        with open("tasks.txt","r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open("tasks.txt","w") as file:
        for task in tasks:
            file.write(task + "\n")
            
tasks = load_tasks()

while True:
    print("\n1.Add Task ")
    print("2.View Tasks ")
    print("3.Delete Task ")
    print("4.Exit ")
    print("5.Clear All Tasks")
    print("6.Mark Tasks as Completed")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("Task added!")

    elif choice == "2":
        if len(tasks)== 0 :
            print("No task available.")
        else:
            for i, task in enumerate(tasks):
                print(f" {i+1}.{task}")
                

    elif choice == "3":
        task_no = int(input("Enter task number to delete : "))

        if 0 < task_no <= len(tasks):
            tasks.pop(task_no - 1)
            save_tasks(tasks)
            print("Task deleted!")
        else:
            print("Invalid task number")

    elif choice == "4":
        print("Goodbye!")
        break
    
    elif choice == "5":
        tasks.clear()
        save_tasks(tasks)
        print("All tasks cleared!")

    elif choice == "6":
        task_no = int(input("Enter task number to mark as completed: "))
        if 0 < task_no <= len(tasks):
            tasks[task_no - 1]+="{DONE AND DUSTED!!}"
            save_tasks(tasks)
            print("Tasks marked as completed!")
        else:
            print("Invalid task number")
    
    else:
        print("Invalid choice..")

    
 



           
    