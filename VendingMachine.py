# ----------------------------------------
# VENDING MACHINE PROGRAM
# Created by: Efraim Botiquin
# AI assistance used for explanations and debugging suggestions
# from Perplexity AI - used for understanding only, not code generation
# NOTE: This program contains:
# - Categories
# - Stock system
# - Purchase suggestions
# - Input validation
# - Multiple purchases loop
# - Classes (OOP)
# - Functions that pass/return values
# - Clean user experience
# ---------------------------------------

class Item:
    """Represents a vending machine item."""
    def __init__(self, code, name, price, category, stock):
        self.code = code
        self.name = name 
        self.price = price
        self.category = category
        self.stock = stock


class VendingMachine:
    """Main vending machine system."""
    def __init__(self):
        # Dictionary of items
        self.items = {
            "A1": Item("A1", "Water", 1.00, "Drinks", 5),
            "A2": Item("A2", "Coke", 4.00, "Drinks", 5),
            "A3": Item("A3", "Sprite", 4.00, "Drinks", 5),
            "B1": Item("B1", "Chips", 2.00, "Snacks", 3),
            "B2": Item("B2", "Chocolate", 2.50, "Snacks", 3),
            "B3": Item("B3", "Biscuits", 1.50, "Snacks", 3),
            "C1": Item("C1", "Coffee", 1.50, "Hot Drinks", 4),
            "C2": Item("C2", "Tea", 1.00, "Hot Drinks", 4),
            "C3": Item("C3", "Hot Chocolate", 2.00, "Hot Drinks", 4),
        }

        # Simple suggestion pairs
        self.suggestions = {
            "Coffee": "Biscuits",
            "Coke": "Chips",
            "Chocolate": "Water"
        }

    def show_menu(self):
        """Displays items grouped by category."""
        print("\n-------------------------")
        print("       VENDING MENU      ")
        print("--------------------------")
        categories = {}

        for item in self.items.values():
            categories.setdefault(item.category, []).append(item)

        for cat, items in categories.items():
            print(f"\n[{cat}]")
            for it in items:
                stock_text = "OUT OF STOCK" if it.stock <= 0 else f"Stock: {it.stock}"
                print(f"{it.code} - {it.name} (AED {it.price:.2f}) {stock_text}")

    def get_item(self, code):
        """Returns item object if valid code."""
        return self.items.get(code.upper(), None)
    
    def handle_money(self, price):
        """Processes user money and returns change."""
        while True:
            try:
                money = float(input(f"Enter money (AED) - Price is AED {price:.2f}: "))
                if money < price:
                    print("Not enough money! Try again.")
                    continue
                return money - price
            except ValueError:
                print("Invalid input. Enter numbers only.")

    def suggest_item(self, bought_item):
        """Suggests another product if available."""
        if bought_item in self.suggestions:
            suggestion = self.suggestions[bought_item]
            print(f"Suggestion: You may also like **{suggestion}**!")

    def start(self):
        """Main vending process with repeat option."""
        print("WELCOME TO THE SMART VENDING MACHINE!")

        while True:
            self.show_menu()

            code = input("\nEnter item code: ")
            item = self.get_item(code)

            if item is None:
                print("Invalid code! Please try again.")
                continue

            if item.stock <= 0:
                print("Sorry. this item is out of stock!")
                continue

            print(f"\nYou selected: {item.name} - AED {item.price:.2f}")

            # Handle money
            change = self.handle_money(item.price)

            # Update stock
            item.stock -= 1

            print(f"\nDispensing {item.name}...")
            print(f"Your change: AED {change:.2f}")
            print("Thank you!")

            # Suggestion system
            self.suggest_item(item.name)

            # Ask for additional purchase
            again = input("\nDo you want to buy another item? (yes/no): ").lower()
            if again != "yes":
                print("Thank you for using the vending machine!")
                break


# Run program
if __name__ == "__main__":
    machine = VendingMachine()
    machine.start()
    