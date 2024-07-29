# Function to view items in the ItemList

ItemList = {}  # Dictionary to store items

def view():
    fileDetails = open("laptop.txt",'r')  # Open file "laptop.txt" in read mode
    fileData = fileDetails.read().split('\n')  # Read the contents of the file and split by new lines

    while("" in fileData):
        fileData.remove("")  # Remove any empty lines from the fileData list

    length = 1  # Initialize length variable to 1
    for data in range(len(fileData)):
        ItemList[length] = fileData[data].split(',')  # Split each line by comma and assign to ItemList with key as length
        length += 1  # Increment length by 1 for the next item

    # Print header
    print("--"*45)
    print("S.N. \tProduct Company Price Quantity  CPU Info \tGPU Info")
    print("--"*45)  

    # Iterate over the keys in ItemList
    for id in ItemList.keys():
        print(id, end="\t")  # Print the key (S.N.) followed by a tab character
        for data in range(len(ItemList[id])):
            print(ItemList[id][data], end='\t')  # Print each value in the corresponding ItemList
        print()  # Print a new line after printing all values for a specific key

    print("--"*45)


