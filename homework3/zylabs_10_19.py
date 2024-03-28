# Adil Ahmad
# 2278219
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
        self.cost = 0.0

    def print_item_cost(self):
        cost = self.item_price * self.item_quantity
        self.cost = cost
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${cost:.0f}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        cart_items_string = []
        for i in self.cart_items:
            cart_items_string.append(i.item_name)
        if item_name not in cart_items_string:
            print("Item not found in cart. Nothing removed.\n")
        else:
            index_to_delete = cart_items_string.index(item_name)
            del self.cart_items[index_to_delete]
            print()

    def modify_item(self, item):
        cart_items_string = []
        for i in self.cart_items:
            cart_items_string.append(i.item_name)
        if item.item_name not in cart_items_string:
            print("Item not found in cart. Nothing modified.\n")
        else:
            index = cart_items_string.index(item.item_name)
            self.cart_items[index].item_quantity = item.item_quantity

    def get_num_items_in_cart(self):
        num_items = 0
        for x in self.cart_items:
            num_items += x.item_quantity
        return num_items

    def get_cost_of_cart(self):
        cost = 0.0
        for i in self.cart_items:
            cost += (i.item_price * i.item_quantity)
        return cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
        print(f"\nTotal: ${self.get_cost_of_cart():.0f}\n")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print(f"Item Descriptions")
        for i in self.cart_items:
            print(f"{i.item_name}: {i.item_description}")
        print()


def print_menu(cart):
    valid_choices = ["q", "a", "r", "c", "i", "o"]
    choice = ""
    while choice != "q":
        choice = ""
        print(
            "MENU\n"
            "a - Add item to cart\n"
            "r - Remove item from cart\n"
            "c - Change item quantity\n"
            "i - Output items' descriptions\n"
            "o - Output shopping cart\n"
            "q - Quit\n"
        )
        while choice not in valid_choices:
            choice = str(input("Choose an option:\n"))

            if choice == "a":
                print("ADD ITEM TO CART")
                new_name = str(input("Enter the item name:\n"))
                new_desc = str(input("Enter the item description:\n"))
                new_price = float(input("Enter the item price:\n"))
                new_quantity = int(input("Enter the item quantity:\n"))
                print()
                new_item = ItemToPurchase(new_name, new_price, new_quantity, new_desc)
                cart.add_item(new_item)

            if choice == "r":
                print("REMOVE ITEM FROM CART")
                item_to_remove = str(input("Enter name of item to remove:\n"))
                cart.remove_item(item_to_remove)

            if choice == "c":
                print("CHANGE ITEM QUANTITY")
                lookup_name = str(input("Enter the item name:\n"))
                modded_quantity = int(input("Enter the new quantity:\n"))
                temp_item = ItemToPurchase(item_name=lookup_name, item_quantity=modded_quantity)
                cart.modify_item(temp_item)

            if choice == "i":
                print("OUTPUT ITEMS' DESCRIPTIONS")
                cart.print_descriptions()

            if choice == "o":
                print("OUTPUT SHOPPING CART")
                cart.print_total()


if __name__ == "__main__":
    username = input("Enter customer's name:\n")
    userdate = input("Enter today's date:\n")
    cart1 = ShoppingCart(username, userdate)
    print(f"\nCustomer name: {username}")
    print(f"Today's date: {userdate}\n")
    print_menu(cart1)
