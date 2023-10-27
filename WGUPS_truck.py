import datetime


# Creates a truck class for later to create truck objects with the attributes
class Truck:
    def __init__(self, truck_id, capacity, start_time_str, hash_table):
        self.current_location = None
        self.truck_id = truck_id
        self.capacity = capacity
        self.start_time = datetime.datetime.strptime(start_time_str, "%I:%M %p")
        self.packages = []
        self.mileage = 0
        self.total_time = datetime.timedelta()  # initialize total time to zero
        self.route = []
        self.current_location = 0  # Start from the hub
        self.hash_table = hash_table  # Store a reference to the hash table

    def set_route(self, route):
        self.route = route

    def add_package(self, package):
        if len(self.packages) <= int(self.capacity):  # Ensures truck is not over capacity
            self.packages.append(package)
            package.delivery_status = "En Route"
        else:
            print(f"Truck {self.truck_id} is at full capacity!")

    def deliver_package(self, package, distance):
        self.mileage += float(distance)
        delivery_time = distance / 18  # in hours
        self.total_time += datetime.timedelta(hours=delivery_time)

        # Update the package status in the hash table
        package.delivery_status = "Delivered"
        package.delivery_time = self.start_time + self.total_time

        # Update the current location
        if self.route:
            self.current_location = self.route.pop(0)

    def display_delivery_time(self):
        hours, remainder = divmod(self.total_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

    def display_packages(self):
        package_ids = [package.package_id for package in self.packages]
        print(f"Truck {self.truck_id} has packages: {', '.join(package_ids)}")

    def add_mileage(self, distance):
        self.mileage += float(distance)

    def get_mileage(self):
        return self.mileage

    def update_package_status(self, package_id, status):
        package = self.hash_table.lookup(package_id)
        if package:
            package.delivery_status = status

    # Calculates the time based on the distance traveled from the distance matrix and the speed of truck
    def manage_deliveries(self, distance_matrix, hub_index, address_to_index):
        current_time = self.start_time
        for i in range(len(self.route) - 1):
            start_node = self.route[i]
            end_node = self.route[i + 1]
            distance = distance_matrix[start_node][end_node]
            travel_time = distance / 18
            current_time += datetime.timedelta(hours=travel_time)

            # Deliver packages for the end_node destination
            for package in self.packages:
                if address_to_index[package.delivery_address] == end_node:
                    self.deliver_package(package, distance)
