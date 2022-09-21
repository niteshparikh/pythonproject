import contents

items = []


def load_vm():
    global items
    vm1 = contents.VendingMachine("A1", 10, "Water", 2)
    vm2 = contents.VendingMachine("A2", 20, "Chips", 4)
    vm3 = contents.VendingMachine("A3", 30, "Chocolate", 10)
    vm4 = contents.VendingMachine("A4", 40, "Juice", 10)
    items.append(vm1)
    items.append(vm2)
    items.append(vm3)
    items.append(vm4)
    a=len(items)
    print(a)


def disp():
    # show recipts to the user
    global items
    for i in items:
        i.description()



def add_item():
    global items
    print("  add   items")
    itemID = input("Enter item id : ")
    price = float(input(" price : $ "))
    iname = input("Item name: ")
    quantity = int(input("How many items you are adding ?"))
    addingItem = search(itemID)
    if addingItem != None:
        #means this items already exists , so we just need to inc. the quantity
        addingItem.quantity += quantity
    else:
        vm=contents.VendingMachine(itemID, price, iname, quantity)
        items.append(vm)


def buy_item(opt):
    print("   purchase item    ")
    global items
    itemID = input("enter the item id:")
    buyItem = search(itemID)
    if buyItem!= None:
        buyItem.description()
        if 's' in opt:
            original_price=buyItem.price
            itemPrice = buyItem.price*80/100
            print(f"The item price for you is {itemPrice} and the original price was {original_price}")
        else:
            itemPrice = buyItem.price
        if calculate(itemPrice):
            buyItem.quantity -= 1
    else:
        print("Invalid input")


def calculate(price):
    print("please pay $", price)
    paid = float(input("enter your money $:"))
    if paid == price:
        print("Succesfull")
        return True
    elif paid > price:
        print(f"your change is ${paid-price}")
        return True
    else:
        print(f"you need to add more money $ {price-paid} to buy")
    return False


def search(itemID):
    global items
    for i in items:
        if i.itemID == itemID:
            return i
    return None


def quit_vm():
    print()
    print("terminating")
    exit(0)