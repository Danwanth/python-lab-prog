class Shopping:
    def __init__(self):
        self.shop = "RBI"
        self.cart = {}
        self.menu_items = {
            1: {"name": "Samsung Galaxy S88", "price": 999},
            2: {"name": "iPhone 14", "price": 1099},
            3: {"name": "Google Pixel 7", "price": 599}
        }

    def menu(self):
        print("=========MENU==========\n")
        for key, item in self.menu_items.items():
            print(f"[{key}] {item['name']} - ${item['price']}")

    def add_item(self):
        self.menu()
        cid1 = int(input("Enter the item number you want to add to the cart: "))
        if cid1 in self.menu_items:
            quantity = int(input("Input the quantity: "))
            if cid1 in self.cart:
                self.cart[cid1]['quantity'] += quantity
            else:
                self.cart[cid1] = {'quantity': quantity, 'name': self.menu_items[cid1]['name'], 'price': self.menu_items[cid1]['price']}
            print(f"Added {quantity} of {self.menu_items[cid1]['name']} to the cart.")
        else:
            print("Invalid item number.")

    def remove_item(self):
        item_id = int(input("Enter the item number you want to remove from the cart: "))
        if item_id in self.cart:
            del self.cart[item_id]
            print(f"Removed {self.menu_items[item_id]['name']} from the cart.")
        else:
            print("Item not found in the cart.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
            return
        print("Your cart contains:")
        for item_id, details in self.cart.items():
            print(f"{details['name']} - Quantity: {details['quantity']} - Price: ${details['price']}")

    def checkout(self):
        if not self.cart:
            print("Your cart is empty. Cannot checkout.")
            return
        total = sum(details['price'] * details['quantity'] for details in self.cart.values())
        print(f"Total amount to pay: ${total}")
        print("Thank you for shopping with us!")

# Main program
b = Shopping()
while True:
    print("\n===SHOPPING MART==\n")
    print(" [1] ADD TO CART \n [2] Remove from cart \n [3] View cart \n [4] Checkout \n [5] Exit \n")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        b.add_item()
    elif ch == 2:
        b.remove_item()
    elif ch == 3:
        b.view_cart()
    elif ch == 4:
        b.checkout()
    elif ch == 5:
        print("TERMINATING PROGRAM....")
        break
    else:
        print("Invalid choice. Please try again.")
		
