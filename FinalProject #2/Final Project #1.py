# Rayyan Rahman ID: 1893113

import csv
import datetime


def sort_by_manufacturer_and_date(item):
    manufacturer = item[1][0]
    manu_date = item[1][1]
    return manufacturer, manu_date


def sort_by_price(item):
    price = item[1][2]
    return price


def sort_by_ID(item):
    item_ID = item[0]
    return item_ID


class Inventory:
    def __init__(self, manufacturers_file, prices_file, services_dates_file, full_inventory_file, laptop_inventory_file,
                 past_service_date_file, damaged_file):
        # constructors
        self.full_inventory = {}
        self.laptop_inventory = {}
        self.past_service_date_inventory = {}
        self.damaged_inventory = {}
        self.manufacturer_data = []
        self.price_data = []
        self.service_dates_data = []
        self.full_inventory_file = full_inventory_file
        self.laptop_inventory_file = laptop_inventory_file
        self.past_service_date_file = past_service_date_file
        self.damaged_file = damaged_file

        # Read in data from input files
        with open(manufacturers_file, 'r') as manufacturers_file:
            manufacturer_reader = csv.reader(manufacturers_file)
            self.manufacturer_data = list(manufacturer_reader)

        with open(prices_file, 'r') as prices_file:
            price_reader = csv.reader(prices_file)
            self.price_data = list(price_reader)

        with open(services_dates_file, 'r') as services_dates_file:
            service_dates_reader = csv.reader(services_dates_file)
            self.service_dates_data = list(service_dates_reader)

    def generate_full_inventory(self):
        # Loop through the ManufacturerList data and add to dictionary
        for row in self.manufacturer_data:
            product_id = row[0]
            manufacturer = row[1]
            product_type = row[2]
            damaged = "" if len(row) < 4 else row[3]
            self.full_inventory[product_id] = [manufacturer, product_type, "", "", damaged]

        # Loop through the PriceList data and update dictionary
        for row in self.price_data:
            product_id = row[0]
            price = row[1]
            self.full_inventory[product_id][2] = price

        # Loop through the ServiceDatesList data and update dictionary
        for row in self.service_dates_data:
            product_id = row[0]
            service_date = row[1]
            self.full_inventory[product_id][3] = service_date

    def generate_laptop_data(self):

        # Loop through the items in the full_inventory dictionary
        for item_id, item_data in self.full_inventory.items():
            # Check if the product type is laptop
            product_type = item_data[1]
            if product_type == 'laptop':
                # Add the item to the laptop items list
                manufacturer = item_data[0]
                price = item_data[2]
                service_date = item_data[3]
                damaged = item_data[4]
                self.laptop_inventory[item_id] = [manufacturer, price, service_date,
                                                  damaged]

    def generate_past_service_date_inventory(self):
        # Get the current date
        current_date = datetime.datetime.now().date()

        # Loop through the items in the full_inventory dictionary
        for item_id, item_data in self.full_inventory.items():
            # Check if the service date is in the past
            service_date = item_data[3]
            if service_date and datetime.datetime.strptime(service_date, "%m/%d/%Y").date() < current_date:
                # Add the item to the past service date items list
                manufacturer = item_data[0]
                item_type = item_data[1]
                price = item_data[2]
                damaged = item_data[4]
                self.past_service_date_inventory[item_id] = [manufacturer, item_type, price, service_date,
                                                             damaged]

    def generate_damaged_inventory(self):
        # Iterate through the full inventory and add any damaged items to the list
        for item_id, item_data in self.full_inventory.items():
            if item_data[4] == 'damaged':
                # Add the item to the damaged items list
                manufacturer = item_data[0]
                product_type = item_data[1]
                price = item_data[2]
                service_date = item_data[3]
                self.damaged_inventory[item_id] = [manufacturer, product_type, price, service_date]

    def sort_data(self):
        # Convert dictionary to list of tuples and sort by manufacturer and date
        full_inventory_list = [(key, val) for key, val in self.full_inventory.items()]
        full_inventory_sorted = sorted(full_inventory_list, key=sort_by_manufacturer_and_date)

        # sort Laptop Inventory
        laptop_inventory_list = [(key, val) for key, val in self.laptop_inventory.items()]
        laptop_inventory_sorted = sorted(laptop_inventory_list, key=sort_by_ID)

        # sort Past service date inventory
        past_service_date_inventory_list = [(key, val) for key, val in self.past_service_date_inventory.items()]
        past_service_date_inventory_sorted = sorted(past_service_date_inventory_list, key=sort_by_manufacturer_and_date)

        # sort Damaged Inventory
        damaged_inventory_list = [(key, val) for key, val in self.damaged_inventory.items()]
        damaged_inventory_sorted = sorted(damaged_inventory_list, key=sort_by_price)

        # Open the output files in write mode and use the csv.writer to write CSV files.
        with open(self.full_inventory_file, 'w', newline='') as full_file, \
                open(self.laptop_inventory_file, 'w', newline='') as laptop_file, \
                open(self.past_service_date_file, 'w', newline='') as past_service_file, \
                open(self.damaged_file, 'w', newline='') as damaged_inventory_file:
            # Create a csv.writer object for each output file
            full_writer = csv.writer(full_file)
            laptop_writer = csv.writer(laptop_file)
            past_writer = csv.writer(past_service_file)
            damaged_writer = csv.writer(damaged_inventory_file)

            # Write data rows to FullInventory.csv
            full_rows = [[item[0], item[1][0], item[1][1], item[1][2], item[1][3], item[1][4]] for item in
                         full_inventory_sorted]
            full_writer.writerows(full_rows)

            # Write data rows to LaptopInventory.csv
            laptop_rows = [[item[0], item[1][0], item[1][1], item[1][2], item[1][3]] for item in
                           laptop_inventory_sorted]
            laptop_writer.writerows(laptop_rows)

            # Write data rows to PastServiceDateInventory.csv
            past_rows = [[item[0], item[1][0], item[1][1], item[1][2], item[1][3], item[1][4]] for item in
                         past_service_date_inventory_sorted]
            past_writer.writerows(past_rows)

            # Write data rows to DamagedInventory.csv
            damaged_rows = [[item[0], item[1][0], item[1][1], item[1][2], item[1][3]] for item in
                            damaged_inventory_sorted]
            damaged_writer.writerows(damaged_rows)

    def query_inventory(self):
        while True:
            user_input = input("Enter the manufacturer and item type separated by a comma (or 'q' to quit): ")
            if user_input.lower() == 'q':
                break

            # Extract manufacturer and item type from user input
            manufacturer, item_type = [x.strip().lower() for x in user_input.split(',')]

            # Read FullInventory.csv to check if manufacturer and item type are present
            with open(self.full_inventory_file, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                matching_items = []
                for row in reader:
                    if row[1].strip().lower() == manufacturer and row[2].strip() == item_type:
                        if row[5].lower() == 'damaged' or datetime.datetime.strptime(row[4], "%m/%d/%Y").date() < datetime.datetime.now().date():
                            # Item is damaged or past its service date
                            continue
                        item_price = float(row[3])
                        matching_items.append((row, item_price))

                if not matching_items:
                    # No item found
                    print("No such item in inventory")
                    continue
                elif len(matching_items) > 1:
                    # More than one item found
                    print("More than one item found. Please provide more specific information.")
                    continue

                # Find the most expensive item of the same type from a different manufacturer
                max_price = 0
                similar_item = None
                with open(self.full_inventory_file, 'r', newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        if row[2].strip().lower().capitalize() == item_type and row[1].strip().lower() != manufacturer:
                            if row[4].lower() == 'damaged' or row[3] != '':
                                # Item is damaged or past its service date
                                continue
                            price = float(row[2])
                            if price > max_price:
                                max_price = price
                                similar_item = row

                # Print the output item and a similar item of the same type from another manufacturer
                output_item, item_price = matching_items[0]
                print("Your item is: {}, {}, {}, ${:.2f}".format(output_item[0], output_item[1],
                                                                 output_item[2], item_price))
                if similar_item:
                    print("You may also consider: {}, {}, {}, ${:.2f}".format(similar_item[0],
                                                                              similar_item[1],
                                                                              similar_item[2], max_price))


# Accept input of files

manufacturer_file = input("Enter the name of the ManufacturerList file: ")
price_file = input("Enter the name of the PriceList file: ")
service_dates_file = input("Enter the name of the ServiceDatesList file: ")

inventory = Inventory(manufacturer_file, price_file, service_dates_file, 'FullInventory.csv',
                      'LaptopInventory.csv', 'PastServiceDateInventory.csv', 'DamagedInventory.csv')

# Function calling
inventory.generate_full_inventory()
inventory.generate_laptop_data()
inventory.generate_past_service_date_inventory()
inventory.generate_damaged_inventory()
inventory.sort_data()
inventory.query_inventory()
