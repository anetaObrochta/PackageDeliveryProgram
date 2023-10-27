# Created by Aneta Obrochta

# Import other necessary project files to run the program
from WGUPS_truck import Truck
from hash_data_structure import HashTable
from manage_delivery import ManageDelivery
from parse_csv_data import parse_package_data, parse_distance_data
from truck_util import load_packages_onto_truck, manage_truck_movement
import datetime

# Parse the package details CSV file
parsed_packages = parse_package_data()
# Parse the distance data CSV to get the adjacency matrix
distance_matrix, address_to_index = parse_distance_data()
# Initialize the size of the hash table
hash_table = HashTable(size=100)
# Initialize the package loading method
hash_table.load_package_data(parsed_packages)
# Initialize the displays contents of the hash table
hash_table_contents = hash_table.display_contents()

# Create truck objects with initialized truck ID number and their start time
truck1 = Truck("1", "16", "8:00 AM", hash_table)
truck2 = Truck("2", "16", "9:10 AM", hash_table)
# Create truck3 after truck1 returns
truck3 = Truck("3", "16", "11:00 AM", hash_table)

# Dictionary for easy truck access
trucks = {
    "1": truck1,
    "2": truck2,
    "3": truck3
}
hub_index = 0
# Load packages into trucks and manage movements
for truck_id in ["1", "2", "3"]:
    load_packages_onto_truck(truck_id, hash_table_contents, trucks)
    truck_package_addresses = [package.delivery_address for package in trucks[truck_id].packages]
    manage_truck_movement(trucks[truck_id], truck_id, truck_package_addresses, ManageDelivery,
                          distance_matrix, hub_index, address_to_index)

# For truck1, after loading its packages, sets the addresses it will visit based on the packages loaded
truck1_package_addresses = [package.delivery_address for package in truck1.packages]

nodes_to_visit_for_truck1 = [hub_index] + [address_to_index[address] for address in truck1_package_addresses]

# Run nearest neighbor algorithm for truck1
path1, total_distance1, truck1_end_time = ManageDelivery.get_nearest_neighbor(
    distance_matrix, start_node=hub_index, nodes_to_visit=nodes_to_visit_for_truck1, current_time=truck1.start_time)

# Update truck1 mileage
truck1.add_mileage(total_distance1)
truck1.end_time = truck1_end_time  # Update truck1's end time

# For truck2, after loading its packages, sets the addresses it will visit based on the packages loaded
truck2_package_addresses = [package.delivery_address for package in truck2.packages]

nodes_to_visit_for_truck2 = [hub_index] + [address_to_index[address] for address in truck2_package_addresses]

# Run nearest neighbor algorithm for truck2
path2, total_distance2, truck2_end_time = ManageDelivery.get_nearest_neighbor(
    distance_matrix, start_node=hub_index, nodes_to_visit=nodes_to_visit_for_truck2, current_time=truck2.start_time)

# Update truck2 mileage
truck2.add_mileage(total_distance2)
truck2.end_time = truck2_end_time  # Update truck2's end time

# For truck3, after loading its packages, sets the addresses it will visit based on the packages loaded
truck3_package_addresses = [package.delivery_address for package in truck3.packages]

nodes_to_visit_for_truck3 = [hub_index] + [address_to_index[address] for address in truck3_package_addresses]

# Run nearest neighbor algorithm for truck3
path3, total_distance3, truck3_end_time = ManageDelivery.get_nearest_neighbor(
    distance_matrix, start_node=hub_index, nodes_to_visit=nodes_to_visit_for_truck3, current_time=truck3.start_time)

# Update truck3 mileage
truck3.add_mileage(total_distance3)


def display_package_details(package, status, delivery_time=None):
    # Display the details of a single package in a structured format.
    details = {
        "Package ID": package.package_id,
        "Delivery Status": status,
        "Delivery Time": delivery_time,
        "Delivering on Truck": package.on_truck,
        "Delivery Deadline": package.delivery_deadline,
        "Delivery Address": package.delivery_address,
        "City": package.delivery_city,
        "Zip Code": package.delivery_zip,
        "Package Weight": package.package_weight,
    }
    print("-" * 40)
    for key, value in details.items():
        print(f"{key}: {value}")
    print("-" * 40)


# Display the details of all packages in a condensed format
def display_package_details_compact(package, status, delivery_time=None, row_number=None):
    # Determine the color based on row number to make every other row a light gray
    default_color = "\33[0m"
    light_gray_color = "\33[37m"

    color = light_gray_color if row_number % 2 == 0 else default_color

    # Adjust the widths of the fields to align the columns properly and specifies the color change for every other row
    print(f"{color}Package ID: {package.package_id:<2} | "
          f"Delivery Status: {status}{color} | "
          f"Delivery Time: {delivery_time:<8} | "
          f"Delivering on Truck: {package.on_truck} | "
          f"Delivery Deadline: {package.delivery_deadline:<8} | "
          f"Address: {package.delivery_address:<38} | "
          f"City: {package.delivery_city:<16} | "
          f"Zip Code: {package.delivery_zip:<5} | "
          f"Weight: {package.package_weight:<2} | "
          )


# Command Line Interface for user interaction with given options to view a single package, all the packages, or the
# total mileage for each and all trucks
def command_line_interface(hash_table_use, hash_table_contents_display):
    while True:
        print()
        print("Please select from the following options:")
        print("[ 1 ] View all packages information and status")
        print("[ 2 ] Enter a package ID to view a single package with its information and status")
        print("[ 3 ] View delivery trip mileage for all trucks and their finished delivery time")
        print("[ 4 ] End this program\n")

        choice = input("Enter the number of the option you want to proceed with: ")

        if choice == '1':
            # Get the current time from the user
            current_time = input("Enter the time you want to view package information (HH:MM AM/PM): ")
            try:
                datetime.datetime.strptime(current_time, "%I:%M %p")
            # Raises a prompt to re-enter the time in correct format
            except ValueError:
                print("Invalid time format. Please enter the time in the HH:MM AM/PM format.")
                continue  # Restart the loop
            # Sorts the package ID numbers to display the packages in ascending order from 1-40 for better viewing
            for index, package in enumerate(sorted(hash_table_contents_display, key=lambda x: int(x.package_id))):
                # Runs the function to change the address for package 9
                change_package_9_address(package, current_time)
                # Gets the status of each package and provides the delivery time
                status, delivery_time = get_package_status(package, current_time)
                display_package_details_compact(package, status, delivery_time, row_number=index)

        elif choice == '2':
            # Get the current time from the user
            current_time = input("Enter the time you want to view package information (HH:MM AM/PM): ")
            try:
                datetime.datetime.strptime(current_time, "%I:%M %p")
            # Raises a prompt to re-enter the time in correct format
            except ValueError:
                print("Invalid time format. Please enter the time in the HH:MM AM/PM format.")
                continue  # Restart the loop
            package_id = input("Enter the package ID: ")
            # Uses the Hash Table look up function to get the package details based on the package ID as the key
            package = hash_table_use.lookup(package_id)

            # Check if the package exists
            if package:
                # Calls the function to change the address for package 9
                change_package_9_address(package, current_time)

                # Gets the status of each package and provides the delivery time
                status, delivery_time = get_package_status(package, current_time)
                display_package_details(package, status, delivery_time)
            else:
                print("Invalid package ID. Please try again.")

        elif choice == '3':
            # Displays mileage for each truck and provides total mileage for all 3 trucks
            print(f"Total mileage for Truck 1: {total_distance1} miles")
            print(f"Total mileage for Truck 2: {total_distance2} miles")
            print(f"Total mileage for Truck 3: {total_distance3} miles")
            print(f"Overall total mileage: {total_distance1 + total_distance2 + total_distance3} miles\n")

        elif choice == '4':
            # Ends the program
            print("Goodbye!\n")
            break

        else:
            print("Invalid choice. Please select a valid option.")


# Creates a dictionary to keep track of the addresses for package 9
package_9_addresses = {
    "before_10_20_am": {
        "address": "300 State St",
        "zip_code": "84103"
    },
    "after_10_20_am": {
        "address": "410 S State St",
        "zip_code": "84111"
    }
}


# Function to change package 9 address based on current time
def change_package_9_address(package, current_time_str):
    change_address_start = datetime.datetime.strptime("10:20 AM", "%I:%M %p")
    if package.package_id == '9':
        current_time = datetime.datetime.strptime(current_time_str, "%I:%M %p")

        if current_time < change_address_start:
            # Change the address and zip code to the original values before 10:20 AM
            package.delivery_address = package_9_addresses["before_10_20_am"]["address"]
            package.delivery_zip = package_9_addresses["before_10_20_am"]["zip_code"]
        else:
            # Change the address and zip code to the new address after 10:20 AM
            package.delivery_address = package_9_addresses["after_10_20_am"]["address"]
            package.delivery_zip = package_9_addresses["after_10_20_am"]["zip_code"]


# Checks the package status of each package based on each truck's start time
def get_package_status(package, current_time_str, truck1_start="8:00 AM", truck2_start="9:10 AM",
                       truck3_start="11:00 AM"):
    # Convert the current_time_str to a datetime object
    current_time = datetime.datetime.strptime(current_time_str, "%I:%M %p")
    truck1_time = datetime.datetime.strptime(truck1_start, "%I:%M %p")
    truck2_time = datetime.datetime.strptime(truck2_start, "%I:%M %p")
    truck3_time = datetime.datetime.strptime(truck3_start, "%I:%M %p")

    # Sets default values for package status and delivery time
    status = "Unknown"
    delivery_time = "N/A"

    # Check for Truck 1
    if package.on_truck == "1":
        if current_time < truck1_time:
            status = "\33[34mAt Hub   \33[0m"
        elif current_time >= truck1_time:
            if package.delivery_time and current_time < package.delivery_time:
                status = "\33[33mEn Route \33[0m"
            elif package.delivery_time and current_time >= package.delivery_time:
                status = "\33[32mDelivered\33[0m"
                delivery_time = package.delivery_time.strftime("%I:%M %p")
    # Check for Truck 2
    elif package.on_truck == "2":
        if current_time < truck2_time:
            status = "\33[34mAt Hub   \33[0m"
        elif current_time >= truck2_time:
            if package.delivery_time and current_time < package.delivery_time:
                status = "\33[33mEn Route \33[0m"
            elif package.delivery_time and current_time >= package.delivery_time:
                status = "\33[32mDelivered\33[0m"
                delivery_time = package.delivery_time.strftime("%I:%M %p")
    # Check for Truck 3
    elif package.on_truck == "3":
        if current_time < truck3_time:
            status = "\33[34mAt Hub   \33[0m"
        elif current_time >= truck3_time:
            if package.delivery_time and current_time < package.delivery_time:
                status = "\33[33mEn Route \33[0m"
            elif package.delivery_time and current_time >= package.delivery_time:
                status = "\33[32mDelivered\33[0m"
                delivery_time = package.delivery_time.strftime("%I:%M %p")
    else:
        status = "\33[34mAt Hub   \33[0m"

    return status, delivery_time


command_line_interface(hash_table, hash_table_contents)
