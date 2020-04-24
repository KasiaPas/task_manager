#libraries
import task
import os

#variables
list_of_tasks = []
gap_size = 5
gap = " " * gap_size

#functions

def search_load():
    
    global list_of_tasks
    
    if os.path.exists("list_file.txt"):
        
        list_file = open("list_file.txt")
        content = list_file.readlines()
        new_content = []
        for ss in content:
            z = ss.strip("\n")
            new_content.append(z)
        
        content = new_content

        pos = 0
        number_of_tasks = int(len(content) / 6)
        
        for i in range(number_of_tasks):
            t = task.Task(str(content[pos]))
            pos = pos + 1
            
            t.progress = content[pos]
            pos = pos + 1
            
            t.creation_date = content[pos]
            pos = pos + 1
            
            t.description = content[pos]
            pos = pos + 1
            
            t.due_date = content[pos]
            pos = pos + 1
            
            t.last_update = content[pos]
            pos = pos + 1
            
            list_of_tasks.append(t)
    
    else:
        list_file = open("list_file.txt", "w")
        list_file.close()
        
def save_list():
    
    list_file = open("list_file.txt", "w")

    for t in list_of_tasks:

        list_file.write(t.title + "\n")
        list_file.write(str(t.progress) + "\n")
        list_file.write(t.creation_date + "\n")
        list_file.write(t.description + "\n")
        list_file.write(t.due_date + "\n")
        list_file.write(t.last_update + "\n")
        
    list_file.close()
        
def print_menu():
    
    global gap
    global gap_size
    
    print(" " * 10 + "MENU\n")
    print(gap + "1.List")
    print(gap + "2.Details")
    print(gap + "3.Add")
    print(gap + "4.Remove")
    print(gap + "5.Save and exit\n")
    
    
def show_list(list_of_tasks):
    """
    Show
    """
    
    if len(list_of_tasks) == 0:
        print("Your list is empty! Pick option 3 to add your first task.\n")
    
    else:
        print(" " * gap_size + "LIST OF TASKS:\n")
        for i, t in enumerate(list_of_tasks):
            i = i + 1
            print(str(i) + ". " + t.title)
        
def show_details():
    
    global gap
    global gap_size
    
    while True:       
        
        if len(list_of_tasks) == 0:
            print("You don\'t have any tasks on your list yet.")
            print("Please pick option 3 in main menu to add new tasks!")
            break
        
        else:
            print("You have " + str(len(list_of_tasks)) + " ongoing tasks.")
            chosen = input("Please pick task number from 1 to " + \
                       str(len(list_of_tasks)) + " to see details  or leave it empty to quit. \n")
                      

            
            if chosen == "":
                break
        
            try:
                chosen = int(chosen)
                
                if chosen not in list(range(1, len(list_of_tasks) + 1)):
                    print("Sorry! You don\'t have task number " + str(chosen) + ".")
                    continue
                
                chosen_task = list_of_tasks[int(chosen)-1]
                print(chosen_task.detail_string())
                
                print(gap * 2 + "OPTIONS")
                print(gap + "1. Edit")
                print(gap + "2. See different task")
                print(gap + "3. Main menu")
        
                option = input("Please select the option by typing a number from 1 to 3.\n")
        
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
    
                else:
                    print("Sorry! " + option + " is not a number from 1 - 3.")
        
        
            except ValueError:
                print("Sorry! " + chosen + " is not a number!")
                continue
            
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
    
    global list_of_tasks
    
    while True:
                
        if len(list_of_tasks) == 0:
            print("You don\'t have any tasks on your list yet.")
            print("Please pick option 3 in main menu to add new tasks!")
            break
        
    
        if len(list_of_tasks) == 1:
             print("You have " + str(len(list_of_tasks)) + " ongoing task.")
             
        else:
            print("You have " + str(len(list_of_tasks)) + " ongoing tasks.")
        
        chosen = input("Please pick task number from 1 to " + 
                       str(len(list_of_tasks)) + " to remove it or leave it " +
                       "empty to quit. \n")
            
        if chosen == "":
            break
    
        try:
            chosen = int(chosen)
            
            if chosen not in list(range(1, len(list_of_tasks) + 1)):
                print("Sorry! You don\'t have task number " + str(chosen) + ".")
                continue
            
            print("OK. I am removing task nr " + str(chosen) + " from your list.")
            confirm = input("Please type y to confirm or leave empty to quit.")
            if confirm == "y":
                list_of_tasks.remove(list_of_tasks[chosen - 1])
                print("Task removed!")
            
        
        except ValueError:
            print("Sorry! " + chosen + " is not a number!")
            
    
    
if __name__ == "__main__":
    
    print("Hello! Welcome to your personal task manager!")
    search_load()
    while True:
        print_menu()
        option = input("Please pick the option by typing a number from 1-5\n")
        print()
        if option == "1":
            show_list(list_of_tasks)
            
        elif option == "2":
            show_details()
            
        elif option == "3":
            add_task()
        
        elif option == "4":
            remove_task()
        
        elif option == "5":
            save_list()
            break
        
        else:
            print("Sorry! " + option + " is not a number from 1 to 5.")
        