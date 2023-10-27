from datetime import timedelta


class ManageDelivery:

    @staticmethod
    def get_nearest_neighbor(adjacency_matrix, nodes_to_visit, start_node=0, current_time=None):
        # Uses Nearest Neighbor algorithm to determine a short path for deliveries.
        # Uses an adjacency matrix representing distances between hubs.
        # Sets the start_hub: the hub from which to start the journey.
        # Returns the path in the order of hubs visited.
        # Returns the total distance traveled.

        # Number of hubs
        num_hubs = len(adjacency_matrix)

        # List to keep track of visited hubs
        visited = [False] * len(adjacency_matrix)

        # Start from the given hub
        current_hub = start_node
        visited[current_hub] = True

        # List to store the order of hubs visited
        path = [current_hub]

        # Total distance traveled
        total_distance = 0

        # Convert nodes_to_visit to a set
        for node in nodes_to_visit:
            if node >= num_hubs:
                raise ValueError(f'Invalid hub index {node} in nodes_to_visit. Maximum valid index is {num_hubs - 1}.')

        nodes_to_visit_set = set(nodes_to_visit)

        # Loop until all nodes have been visited

        while nodes_to_visit_set:
            nearest_distance = float('inf')  # Set to infinity initially
            nearest_hub = None

            # Find the nearest unvisited hub
            for j in nodes_to_visit_set:
                if not visited[j] and 0 < adjacency_matrix[current_hub][j] < nearest_distance:
                    nearest_distance = adjacency_matrix[current_hub][j]
                    nearest_hub = j

            if nearest_hub is None:
                break

            # Move to the nearest hub
            visited[nearest_hub] = True
            path.append(nearest_hub)
            total_distance += nearest_distance
            current_hub = nearest_hub

            nodes_to_visit_set.remove(current_hub)  # Remove the current hub from nodes to visit set

            # Update travel time
            travel_time = timedelta(hours=nearest_distance / 18)
            current_time += travel_time

        # Return to the starting hub
        path.append(start_node)
        total_distance += adjacency_matrix[current_hub][start_node]

        # Calculate end time based on the distance traveled
        if current_time:
            hours_taken = total_distance / 18.0  # Assuming 18 mph speed
            end_time = current_time + timedelta(hours=hours_taken)
            return path, total_distance, end_time
        else:
            return path, total_distance
