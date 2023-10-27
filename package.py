
# Creates a class of a package for later creation of objects for each package that will have better searching
# and lookup
class Package:
    def __init__(self, package_id, delivery_address, delivery_city, delivery_zip, delivery_deadline, package_weight,
                 on_truck):
        self.package_id = package_id
        self.delivery_address = delivery_address
        self.delivery_city = delivery_city
        self.delivery_zip = delivery_zip
        self.delivery_deadline = delivery_deadline
        self.package_weight = package_weight
        self.on_truck = on_truck
        self.delivery_status = "At Hub"
        self.delivery_time = None
