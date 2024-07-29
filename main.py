1
import Buy  # Importing the Buy module
import sell  # Importing the sell module
import view  # Importing the view module

def interaction():
    # Function for interacting with the user

    while True:
        # Displaying the shop name as ASCII art
        print("░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗")
        print("░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝")
        print("░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░")
        print("░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░")
        print("░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗")
        print("░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝")
        
        print("-"*12, "Welcome to the gau basti computers", "-"*18)

        # Displaying the available options to the user
        print("1) View stock \n2) Buy from manufacturer \n3) Sell to customers \n4) Exit")
        print("-"*66)
        
        while True:
            try:
                userOption = int(input("\nWhich option do you want to choose? "))  # Prompt the user to choose an option
                break
            except:
                print("\nPlease Enter a Valid Option")
        
        # Handling the selected option
        if userOption == 1:
            view.view()  # Calling the view() function from the view module
        elif userOption == 2:
            Buy.buy()  # Calling the buy() function from the Buy module
        elif userOption == 3:
            sell.sale()  # Calling the sale() function from the sell module
        elif userOption == 4:
            print("\nThank You For using our shop")  # Exit the program
            break
        else:
            print("\nPlease Enter a Valid Option")  # Prompt the user to enter a valid option

interaction()  # Start the interaction
