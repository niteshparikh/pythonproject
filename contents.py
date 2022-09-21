import sys
sys.path.append(r'C:\Users\niteshparikh\AppData\Local\Programs\Python\Python310\Lib\site-packages')
#print(sys.path)
import tabulate
from tabulate import tabulate

class VendingMachine:

    def __init__(self, itemID,price, iname, quantity):
        super().__init__()
        self.itemID = itemID
        self.price = price
        self.iname = iname
        self.quantity = quantity

    def description(self):
        print(f"The Item_ID is {self.itemID} ,Item_name is {self.iname} ,Item_Price is {self.price} and Item_quantity is {self.quantity}")
        #d = [[self.itemID, self.iname, self.price,self.quantity]]
        #print(tabulate(d, headers=["ItemID", "Item Name", "Price","Quantity"]))