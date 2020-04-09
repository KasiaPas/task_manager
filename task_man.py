def print_menu():
    
    gap_size = 5
    gap = " " * gap_size
    print(" " * 10 + "MENU\n")
    print(gap + "1.List")
    print(gap + "2.Details")
    print(gap + "3.Add")
    print(gap + "4.Remove")
    print(gap + "5.Exit\n")
    
if __name__ == "__main__":
    
    print("Hello! Welcome to your personal task manager!")
    
    while True:
        print_menu()
        option = input("Please pick the option by typing a number from 1-5\n")
        if option == "5":
            break