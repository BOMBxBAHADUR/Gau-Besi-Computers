import view
import datetime
import update

ItemBuy = {}
ItemName = []
ItemQuantity = []
vatAmount = 0

def buy():
    # Call the view function
    global ItemBuy
    ItemBuy = {}
    view.view()

    while True:
        CustomerName = input("\nEnter the customer Name: ")
        if CustomerName.isalpha():
            break
        else:
            print("Please enter the correct name format")

    while True:
        # Get the ItemId and validate
        while True:
            try:
                ItemId = int(input("\nEnter the S.N. of the laptop you want to purchase: "))
                if ItemId > 0 and ItemId <= len(view.ItemList):
                    break
                else:
                    print("\nPlease enter a valid S.N.")
            except:
                print("\nPlease enter a valid S.N.")
        
        while True:
            # Validate QuantityOrdered
            try:
                QuantityOrdered = int(input("\nEnter the amount of item you want to purchase: "))
                if QuantityOrdered > 0:
                    view.ItemList[ItemId][3] = str(int(view.ItemList[ItemId][3]) + QuantityOrdered)
                    ItemBuy[ItemId] = QuantityOrdered
                    break
                else:
                    print("\nPlease enter a valid quantity")
            except:
                print("\nPlease enter a valid quantity")
        
        userInput = input("\nDo you want to purchase another item? (Y or N) ")
        if userInput.lower() == "y":
            continue
        else:
            break
    
    update.itemUpdate()
    billGenerate(CustomerName, ItemBuy,)

    





    
def billGenerate(customername, ItemBuy,):
    """Generate bill in console"""
    global ItemName, ItemQuantity, VatAmount
    ItemName = []
    ItemQuantity = []
    VatAmount = 0
    print("--"*20)
    print("\t Bill Generate")
    print("--"*20)

    print("Customer Name: " + customername)
    print("Bill Date: " + str(datetime.datetime.now()))
    totalPrice = 0

    for i, j in ItemBuy.items():
        ItemName.append(view.ItemList[i][1])
        print(view.ItemList[i][2])
        totalPrice += int(view.ItemList[i][2].replace("$", "0")) * j

    VatAmount = 13/100 * totalPrice
    totalPrice += VatAmount

    print("Item Ordered: " + str(ItemName))
    print("Total Price: " + str(totalPrice))
    print("13% VAT: " + str(VatAmount))
    print("--"*20)

    textBillGenerate(customername, ItemBuy, totalPrice)


def textBillGenerate(customerName, ItemOrdered, totalPrice):
    """Generate bill in a text file"""
    global ItemName, VatAmount
    ItemName = []
    date = datetime.datetime.now()
    fileName = "purchase" + customerName + str(date.second) + ".txt"
    file = open(fileName, "w")
    file.write("Customer Bill")
    file.write("\n")
    file.write("--"*20)
    file.write("\n")
    file.write("Customer Name: %s" % customerName)
    file.write("\n")
    file.write("Order Date: %s" % (str(datetime.datetime.now())))
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
    file.write("VAT Amount: %s" % str(VatAmount))
    file.write("\n")
    file.write("Total Price: %s" % str(totalPrice))
    file.close()
