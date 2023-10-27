import csv
from package import Package


# Used for opening the Package CSV file and correctly reading it
def parse_package_data():
    packages = []

    with open("Package_File.csv", "r") as package_data_file:
        read_package_csv = csv.DictReader(package_data_file)

        for line in read_package_csv:
            package = Package(
                package_id=line["package_id"],
                delivery_address=line["delivery_address"],
                delivery_city=line["delivery_city"],
                delivery_zip=line["delivery_zip"],
                delivery_deadline=line["delivery_deadline"],
                package_weight=line["package_weight"],
                on_truck=line["on_truck"]
            )

            packages.append(package)
        return packages


# Used for opening the Distance Table CSV file and correctly reading it
def parse_distance_data():
    matrix = []
    address_to_index = {}
    with open("Distance_Table_Data.csv", "r") as distance_csv:
        csvreader = csv.reader(distance_csv)

        # Read the header to get address information and initialize the address_to_index dictionary
        header = next(csvreader)
        for idx, address in enumerate(header[1:], start=0):
            address_to_index[address] = idx

        # Process the remaining rows to populate the distance matrix
        for row in csvreader:
            # Convert each string distance to float and store it in the matrix
            matrix.append([float(distance) for distance in row[1:]])

    return matrix, address_to_index
