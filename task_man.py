print("Hello! Welcome to your personal task manager!")

gap_size = 5
gap = " " * gap_size
    
while True:
    print(" " * 10 + "MENU\n")
    print(gap + "1.List")
    print(gap + "2.Details")
    print(gap + "3.Add")
    print(gap + "4.Remove")
    print(gap + "5.Exit\n")
    option = input("Please pick the option by typing a number from 1-5\n")
    if option == "5":
        break