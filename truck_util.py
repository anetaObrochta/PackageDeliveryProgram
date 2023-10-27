

# Loads packages onto a truck based on the given truck ID and uses the list of all packages from the hash table
def load_packages_onto_truck(truck_id, hash_table_contents, trucks):
    # Get the truck object based on truck_id
    truck = trucks.get(truck_id)

    # Iterate through the hash_table_contents to find all the packages assigned to the given truck
    for package in hash_table_contents:
        # CHeck if the package is assigned to the current truck
        if package.on_truck == truck_id:
            # Directly add the existing package object to the truck
            truck.add_package(package)


# Responsible for the movement of truck and delivering the packages
def manage_truck_movement(truck, truck_id, truck_package_addresses, ManageDelivery,
                          distance_matrix, hub_index, address_to_index):

    # Identifies the
    nodes_to_visit = [hub_index] + [address_to_index[address] for address in truck_package_addresses]
    path, total_distance, end_time = ManageDelivery.get_nearest_neighbor(
        distance_matrix, start_node=hub_index, nodes_to_visit=nodes_to_visit, current_time=truck.start_time)

    # Deliver packages based on the path using the created distance matrix
    for i in range(len(path) - 1):  # loop until the penultimate node
        start_node = path[i]
        end_node = path[i + 1]
        distance_travelled = distance_matrix[start_node][end_node]

        delivery_address = list(address_to_index.keys())[list(address_to_index.values()).index(end_node)]
        # Flag identifies whether at least one package was delivered for the address
        delivered_at_least_one = False
        for package in truck.packages:
            if package.delivery_address == delivery_address:
                truck.deliver_package(package, distance_travelled)
                delivered_at_least_one = True
        # If no package was delivered for the address, we should not continue looking for more packages for this address
        if not delivered_at_least_one:
            break

    # Update truck's mileage and end time
    truck.end_time = end_time
