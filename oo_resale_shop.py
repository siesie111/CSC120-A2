# Import from the typing module
from typing import Dict, Optional

class ResaleShop:
    
    # attributes
    inventory : list
    item_id: int
    computer: Dict
    new_price: int
    new_OS: str

    #constructor
    def __init__(self, inventory, item_id, computer, new_price, new_OS):
        self.inventory = inventory
        self.item_id = item_id
        self.computer = computer
        self.new_price = new_price
        self.new_OS = new_OS

    # methods:
    # input computer dictionary, add additional computer info, and return the index of the newly added computer
    def buy(self, computer: Dict):
        self.inventory.append(computer)
        return self.inventory.index(computer)

    # input item id, remove the computer if its in the inventory
    def sell(self, item_id: int):
        if self.inventory[item_id] is not None:
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    # input item id and the new price, and change the inventory with the new price
    def update_price(self, item_id: int, new_price: int):
        if self.inventory[item_id] is not None:
            self.inventory[item_id]["price"] = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")

    #input item id and the new os, update the inventory with the new os
    def update_os(self, item_id: int, new_os: str):
        if self.inventory[item_id] is not None:
            self.inventory[item_id]["operating_system"] = new_os
        else: 
            print("Item", item_id, "not found. Cannot update the operating system.")

    # print the inventory to the terminal
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item in self.inventory:
                # Print its details
                print(f'Item ID: {self.inventory.index(item)} : {item}')
        else:
            print("No inventory to display.")

    # refurbish the computer
    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if self.inventory[item_id] is not None:
            computer = self.inventory[item_id] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff

            if new_os is not None:
                computer["operating_system"] = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")

def main():
    myComputer : ResaleShop = ResaleShop([1, 2], 567, {"description":"2019 MacBook Pro", "processor_type":"Intel", "hard_drive_capacity":256, "memory":16, "operating_system":"High Sierra", "year_made":2019, "price":1000}, 8999, "Sequola")
    myComputer.buy({"description":"2019 MacBook Pro", "processor_type":"Intel", "hard_drive_capacity":256, "memory":16, "operating_system":"High Sierra", "year_made":2019, "price":1000})
    myComputer.print_inventory()

main()
