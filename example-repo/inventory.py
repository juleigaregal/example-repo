# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 07:08:08 2025

@author: juleigar
"""

from tabulate import tabulate

# ======== The beginning of the class ==========
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """Return the cost of the shoe."""
        return self.cost

    def get_quantity(self):
        """Return the quantity of the shoes."""
        return self.quantity

    def __str__(self):
        """Return a string representation of a Shoe object."""
        return (
            f"{self.product}', code='{self.code}', "
            f"country='{self.country}', cost={self.cost}, quantity={self.quantity})"
        )


# ============= Shoe list ===========
# The list will be used to store a list of objects of shoes.
shoe_list = []


# ========== Functions outside the class ==============
def read_shoes_data():
    """Read shoe data from inventory.txt and populate shoe_list."""
    try:
        global shoe_list
        shoe_list.clear()
        with open("inventory.txt", "r+") as file:
            next(file)  # Skip header
            for line in file:
                country, code, product, cost, quantity = line.strip().split(",")
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
        return shoe_list
    except FileNotFoundError:
        print("The file does not exist. Please check the file path and try again.")
        return []


def capture_shoes():
    """Capture a new shoe entry from user input and add it to the shoe list."""
    global shoe_list
    country = input("Enter Country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")

    while True:
        cost_input = input("Enter cost: ")
        if cost_input == "":
            print("Cost must be a number: ")
            continue
        try:
            cost = float(cost_input)
            break
        except ValueError:
            print("Invalid cost. Please enter a number.")

    while True:
        quantity_input = input("Enter quantity: ")
        if quantity_input == "":
            print("Quantity must be a number")
            continue
        try:
            quantity = int(quantity_input)
            break
        except ValueError:
            print("Invalid quantity. Please enter a number.")

    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    print(shoe)


def view_all():
    """Display all shoes in tabular format."""
    shoe_data = []
    for i in shoe_list:
        row = [i.country, i.code, i.product, i.cost, i.quantity]
        shoe_data.append(row)

    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    print(tabulate(shoe_data, headers=headers, tablefmt="grid"))


def re_stock():
    """Restock the shoe with the lowest quantity."""
    low_stock = min(shoe_list, key=lambda s: s.quantity)
    print(f"This item is low on stock: {low_stock}")

    restock = input("Do you want to restock this item? (yes/no): ").strip().lower()
    if restock == "yes":
        while True:
            restock_value_input = input("Enter quantity: ")
            if restock_value_input == "":
                print("Quantity must be a number.")
                continue
            try:
                restock_value = int(restock_value_input)
                break
            except ValueError:
                print("Invalid quantity. Please enter a number.")

        # Update low stock item
        low_stock.quantity += restock_value
        print(f"Stock has been updated to {low_stock.quantity}")

        # Update the text file
        with open("inventory.txt", "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for s in shoe_list:
                file.write(
                    f"{s.country},{s.code},{s.product},{s.cost},{s.quantity}\n"
                )

    else:
        print("No restock chosen.")


def search_shoe():
    """Search for a shoe by code."""
    find_shoe = input("Enter shoe code: ")
    for i in shoe_list:
        if find_shoe == i.code:
            print(i)
            return
    print("Code not found.")


def value_per_item():
    """Calculate and print the value of each shoe item."""
    for shoes in shoe_list:
        value = shoes.cost * shoes.quantity
        print(
            f"Code: {shoes.code}, Product: {shoes.product} "
            f"has a value of: {value}"
        )


def highest_qty():
    """Find and display the shoe with the highest quantity."""
    high_stock = max(shoe_list, key=lambda hs: hs.quantity)
    print(
        f"Code: {high_stock.code}, Product: {high_stock.product} - "
        f"This item is on sale with {high_stock.quantity} in stock."
    )


# ========== Main Menu =============
# Create a menu that executes each function above.
# This menu should be inside the while loop. Be creative!
def main_menu():
    """Display the main menu and handle user input."""
    while True:
        print("\n=== Shoe Inventory Menu ===")
        print("1. View all shoes")
        print("2. Capture a new shoe")
        print("3. Restock shoes")
        print("4. Search for a shoe by code")
        print("5. Calculate value per item")
        print("6. Display product with highest quantity")
        print("7. Exit")

        choice = input("Enter your choice (1–7): ").strip()

        if choice == "1":
            view_all()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            search_shoe()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            print("Exiting program. Have a nice day!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 7.")


if __name__ == "__main__":
    read_shoes_data()  # Load data at startup
    main_menu()
