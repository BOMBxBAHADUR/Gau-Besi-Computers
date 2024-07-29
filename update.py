import view  # Importing the view module

def itemUpdate():
    file = open("laptop.txt", "w")  # Open the "laptop.txt" file in write mode
    
    # Loop to update all the values in the text file
    for values in view.ItemList.values():
        updatedData = ",".join(values)  # Join the values with commas to form a string
        file.write(updatedData)  # Write the updated data to the file
        file.write("\n")  # Write a new line after each item
        
    file.close()  # Close the file
