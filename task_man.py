#variables

list_of_tasks = []

#functions

def print_menu():
    
    gap_size = 5
    gap = " " * gap_size
    print(" " * 10 + "MENU\n")
    print(gap + "1.List")
    print(gap + "2.Details")
    print(gap + "3.Add")
    print(gap + "4.Remove")
    print(gap + "5.Exit\n")
    
def show_list():
    
    global list_of_tasks
    if len(list_of_tasks) == 0:
        print("Your list is empty! Pick option 3 to add your first task.\n")
    else:
        for i, task in enumerate(list_of_tasks):
            i = i + 1
            print(str(i) + ". " + task)
        
def show_details():
    pass

def add_task():
    
    
    global list_of_tasks
   
    while True:
        task = input("Please type your task or leave it empty to quit.\n")
        if task == "":
            break
        else:
            list_of_tasks.append(task)
            print("Your task \"" + task + "\" has been submitted.\n")
            
def remove_task():
    pass
    
if __name__ == "__main__":
    
    print("Hello! Welcome to your personal task manager!")
    
    while True:
        print_menu()
        option = input("Please pick the option by typing a number from 1-5\n")
        print()
        if option == "1":
            show_list()
            
        elif option == "2":
            show_details()
            
        elif option == "3":
            add_task()
        
        elif option == "4":
            remove_task()
        
        elif option == "5":
            break