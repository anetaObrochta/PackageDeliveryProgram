from package import Package


class HashTable:
    def __init__(self, size):
        # Initialize a hash table with the set size in main.py file
        self.size = size
        self.buckets = [[] for _ in range(size)]

    # Calculate the index for the key
    def hash_function(self, key):
        return hash(key) % self.size

    # Insert key-value pair into the hash table
    def insert(self, key, item):
        index = self.hash_function(key)
        if not self.buckets[index]:
            self.buckets[index] = []
        self.buckets[index].append((key, item))

    # Retrieves package details values associated with the given package ID key
    def lookup(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for k, item in bucket:
            if k == key:
                return item
        return None

    # Used for later use to remove a package from the hash table
    def remove(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]

        for i, (k, item) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return item  # Return the removed item to confirm

        return None  # Return None if the key is not found

    # Loads the package data based on the package ID
    def load_package_data(self, package_data):
        for package in package_data:
            self.insert(package.package_id, package)
            package.delivery_status = "At Hub"

    def display_contents(self):
        # Display the content of the hash table and returns a list of package objects stored in a hash table
        contents = []
        for bucket in self.buckets:
            for _, item in bucket:
                if isinstance(item, Package):
                    contents.append(item)
        return contents
