class Computer:

    # attributes
    description:str
    processor_type:str
    hard_drive_capacity:int
    memory:int
    operating_system:str
    year_made:int
    price:int

    # constructor
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # methods:
    # update the operating system to the new OS
    def update_os(self, new_os):
        if self.operating_system == new_os:
            print("This computer is already up to date.")
        else:
            self.operating_system = new_os
            print("This computer is now updates to the new OS.")

    # update the price of the computer
    def update_price(self, new_price):
        if self.price == new_price:
            print("This computer is already updated to the new price.")
        else:
            self.price = new_price
            print("This computer is now updates to the new price.")

def main():
    newComputer : Computer = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    newComputer.update_price(10500)

main()
