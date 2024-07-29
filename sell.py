import view  # Importing the view module
import datetime  # Importing the datetime module
import update  # Importing the update module

ItemOrdered = {}  # Dictionary to store the ordered items and quantities
ItemName = []  # List to store the names of the ordered items
ItemQuantity = []  # List to store the quantities of the ordered items
shippingAmount = 0  # Variable to store the shipping amount

def sale():
    global shippingAmount, ItemOrdered
    
    ItemOrdered = {}  # Clear the ItemOrdered dictionary
    
    view.view()  # Call the view() function from the view module to display the available stock
    
    while True:
        CustomerName = input("\nEnter the customer Name: ")  # Prompt the user to enter the customer name
        
        if CustomerName.isalpha():
            break
        else:
            print("Please Enter the correct name format")
    
    while True:
        # Get the ItemList id and validate it
        while True:
            try:
                ItemId = int(input("\nEnter the S.N. of the laptop: "))  # Prompt the user to enter the laptop ID
                
                if ItemId > 0 and ItemId <= len(view.ItemList):
                    break
                else:
                    print("\nPlease Enter the Valid S.N.")
                
            except:
                print("\nPlease Enter the valid Id")
        
        while True:
            # Validate the quantityOrdered
            try:
                QuantityOrdered = int(input("\nEnter the amount of item you want to buy: "))  # Prompt the user to enter the quantity
                
                if quantityValidation(ItemId, QuantityOrdered):
                    view.ItemList[ItemId][3] = str(int(view.ItemList[ItemId][3]) - QuantityOrdered)  # Update the quantity in the view.ItemList dictionary
                    ItemOrdered[ItemId] = QuantityOrdered  # Add the item and quantity to the ItemOrdered dictionary
                    break
                else:
                    print("\nPlease Enter the valid Quantity")
                
            except:
                print("\n Please Enter the valid id")
        
        userInput = input("\nDo you want to buy again Y or N? ")  # Prompt the user to continue buying or not
        
        if userInput.lower() == "y":
            continue
        else:
            break
    
    shippingInfo = input("\nDo you want to ship Y or N? ")  # Prompt the user for shipping information
    
    if shippingInfo.lower() == "y":
        while True:
            try:
                shippingAmount = int(input("\nEnter the shipping amount: "))  # Prompt the user to enter the shipping amount
                break
            except:
                print("\nPlease Enter the valid Shipping fees")
    
    update.itemUpdate()  # Call the itemUpdate() function from the update module to update the text file
    billGenerate(CustomerName, ItemOrdered)  # Call the billGenerate() function to generate the bill

    



def quantityValidation(ItemId, QuantityOrdered):
    """Function to validate the quantity"""
    quantityAvailable = int(view.ItemList[ItemId][3])  # Get the available quantity from the ItemList dictionary
    if QuantityOrdered > 0 and QuantityOrdered <= quantityAvailable:
        return True
    else:
        return False
    

def billGenerate(customername, ItemOrdered):
    """Function to generate the bill in the console"""
    global ItemName, ItemQuantity, shippingAmount
    ItemName = []
    ItemQuantity = []
    print("--"*20)
    print("\t Bill Generate")
    print("--"*20)

    print("Customer Name: " + customername)
    print("Bill Date: " + str(datetime.datetime.now()))
    totalPrice = 0
    
    for i, j in ItemOrdered.items():
        ItemName.append(view.ItemList[i][1])  # Append the name of the ordered item to the ItemName list
        totalPrice += (int(view.ItemList[i][2].replace("$","0"))*j )+ int(shippingAmount)  # Calculate the total price by multiplying the item price with the quantity and adding the shipping amount
    
    print("Item Ordered: %s" % ItemName)
    print("Total Price: " + str(totalPrice))
    
    if shippingAmount > 0:
        print("Shipping Amount: " + str(shippingAmount))
    
    print("--"*20)
    textBillGenerate(customername, ItemOrdered, totalPrice)  # Call the textBillGenerate() function to generate the bill in a text file

def textBillGenerate(customerName, ItemOrdered, totalPrice):
    """Function to generate the bill in a text file"""
    global ItemName, shippingAmount
    ItemName = []
    date = datetime.datetime.now()
    fileName = customerName + str(date.second) + ".txt"  # Generate a unique file name using the customer name and current seconds
    file = open(fileName, "w")
    file.write("Customer Bill")
    file.write("\n")
    file.write("**"*20)
    file.write("\n")
    file.write("CustomerName: %s" % customerName)
    file.write("\n")
    file.write("OrderDate: %s" % (str(datetime.datetime.now())))
    file.write("\n")
    file.write("--"*25)
    file.write("\n")
    
    for i, j in ItemOrdered.items():
        file.write("Item Ordered: %s" % view.ItemList[i][1])
        file.write("\t")
        file.write("Quantity Ordered: %s" % j)
        file.write("\n")
    
    file.write("--"*25)
    file.write("\n")
    
    if shippingAmount > 0:
        file.write("Shipping Amount %s" % str(shippingAmount))
        file.write("\n")
    
    file.write("Total Price %s" % str(totalPrice))
    file.write("\n")
    file.close()
