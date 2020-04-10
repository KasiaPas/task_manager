#libraries

import task

#variables

list_of_tasks = []
gap_size = 5
gap = " " * gap_size

#functions

def print_menu():
    
    global gap
    global gap_size
    
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
        for i, t in enumerate(list_of_tasks):
            i = i + 1
            print(str(i) + ". " + t.title)
        
def show_details():
    
    global gap
    global gap_size
    
    while True:       
        
        chosen = input("Please pick task number from 1 to " + \
                       str(len(list_of_tasks)) + " to see details. \n")
        chosen = int(chosen)
        chosen_task = list_of_tasks[int(chosen)-1]
        print(chosen_task.detail_string())
            
        print(gap * 2 + "OPTIONS")
        print(gap + "1. Edit")
        print(gap + "2. See different task")
        print(gap + "3. Main menu")
            
        option = input("Please select the option by typing a number from 1 to 3.")
            
        if option == "1":
                
            print(gap * 2 + "EDIT")
            new_title = input("Enter the new title or empty to skip.\n")
                
            if new_title != "":
                chosen_task.title = new_title
    
            new_progress = input("Enter the progress or empty to skip.\n")
            if new_progress != "":
                chosen_task.progress = new_progress
                
            new_description = input("Enter the updated description or empty to skip.\n")
            if new_description != "":
                chosen_task.description = new_description
               
            new_due_date = input("Enter the updated deadline or empty to skip.\n")
            if new_due_date != "":
                chosen_task.due_date = new_due_date
               
            print("Your task has been updated.")    
            
            
        elif option == "2":
            continue
            
        elif option == "3":
            break
            
            
def add_task():
    
    global list_of_tasks
   
    while True:
        user = input("Please type your task or leave it empty to quit.\n")
        if user == "":
            break
        else:
            new_task = task.Task(user)
            
            list_of_tasks.append(new_task)
            print("Your task \"" + new_task.title + "\" has been submitted.\n")
            
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