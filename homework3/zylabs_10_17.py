# Adil Ahmad
# 2278219
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.cost = 0.0

    def print_item_cost(self):
        cost = self.item_price * self.item_quantity
        self.cost = cost
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${cost:.0f}")


if __name__ == "__main__":
    print("Item 1")
    item1_name = str(input("Enter the item name:\n"))
    item1_price = float(input("Enter the item price:\n"))
    item1_quantity = int(input("Enter the item quantity:\n"))
    item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)

    print("\nItem 2")
    item2_name = str(input("Enter the item name:\n"))
    item2_price = float(input("Enter the item price:\n"))
    item2_quantity = int(input("Enter the item quantity:\n"))
    item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)

    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print(f"\nTotal: ${(item1.cost + item2.cost):.0f}")
