#Rayyan Rahman ID: 1893113


class ItemToPurchase:

    # Default constructor

    def __init__(self):
        # Initializing variables

        # with default values

        self.item_name = "none"

        self.item_price = 0

        self.item_quantity = 0

        # print the items

    def print_item_cost(self):
        # Display the item name, quantity and price

        print(self.item_name + " " + str(self.item_quantity) + " @ $"

              + str(self.item_price) + " = $" + str(self.item_price * self.item_quantity))


if __name__ == "__main__":
    # Type main section of code here

    # main function

    # print the item1

    print("Item 1")

    # Creating an object

    item1 = ItemToPurchase()

    # Creating an object to the class

    item2 = ItemToPurchase()

    # prompt and Read item1 details from the user

    item1.item_name = input('Enter the item name:\n')

    item1.item_price = int(input('Enter the item price:\n'))

    item1.item_quantity = int(input('Enter the item quantity:\n'))

    print("\nItem 2")

    # prompt and Read item2 details from the user

    item2.item_name = input('Enter the item name:\n')

    item2.item_price = int(input('Enter the item price:\n'))

    item2.item_quantity = int(input('Enter the item quantity:\n'))

    print("\nTOTAL COST")

    # call the method to print the details

    item1.print_item_cost()

    item2.print_item_cost()

    # Calculate the cost of items

    total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

    # Display the total cost

    print("\nTotal: $" + str(total))