# Package Delivery Routing Program

# PROJECT SUMMARY

I created this project for a school assignment for Data Structures and Algorithms II class. It includes command line application built in Python to simulate a package delivery system. It uses csv file of packages with various delivery constraints and marked which trucks they will be loaded on. It also uses a csv file of an adjacency matrix of distances from each location the packages must be delivered. The program uses a Nearest Neighbor algorithm to find the the closest location to visit next, deliver all packages at that collection and keep repeating until all locations are visited once, and returns to the HUB.

# USAGE

To get the code run this from the command line:
```
git clone https://github.com/anetaObrochta/PackageDeliveryRoutingProgram.git

```

Once that is done, in the main directory where **main.py** is located run:
```
python3 main.py
```
depending on python version^^^

From there you should see the Command Line Interface like this:

![CLI Start](https://github.com/anetaObrochta/PackageDeliveryRoutingProgram/assets/141801067/919ffdb1-091e-49ca-b65b-5e4dc8216907)

# PROJECT SCENARIO

The Parcel Service needs to determine the best route and delivery distribution for their Daily Local Deliveries (DLD) because packages are not currently being consistently delivered by their promised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver 
each day; each package has specific criteria and delivery requirements.

Your task is to determine the best algorithm, write code, and present a solution where all 40 packages, listed in the attached csv file will be delivered on time with the least number of miles added to the combined mileage total of all trucks.

Take into consideration the specific delivery time expected for each package and the possibility that the delivery requirements—including the expected delivery time—can be changed by management at any time and at any point along the chosen route. In addition, you should keep in mind that the supervisor should be able to see, at assigned points, the progress of each truck and its packages by any of the variables listed in the csv file including what has been delivered and what time the delivery occurred.

# ASSUMPTIONS

- Each truck can carry a maximum of 16 packages.
- Trucks travel at an average speed of 18 miles per hour.
- Trucks have a “infinite amount of gas” with no need to stop.
- Each driver stays with the same truck as long as that truck is in service.
- Drivers leave the hub at 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed. The day ends when 
  all 40 packages have been delivered.
- Delivery time is instantaneous, i.e., no time passes while at a delivery (that time is factored into the average speed of the 
  trucks).
- There is up to one special note for each package.
- The wrong delivery address for package #9, Third District Juvenile Court, will be corrected at 10:20 a.m. The correct address 
  is 410 S State St., Salt Lake City, UT 84111.
- The package ID is unique; there are no collisions.
- No further assumptions exist or are allowed.

# CLI EXAMPLES
**Status check of all packages at 10:21 AM**
![status check at 1021 am](https://github.com/anetaObrochta/PackageDeliveryRoutingProgram/assets/141801067/e8845103-bb15-4a13-92e1-a4dc587a88e6)

**Checking specific package based on package ID**
![CLI](https://github.com/anetaObrochta/PackageDeliveryRoutingProgram/assets/141801067/288215e7-02ed-40a4-a6e1-618bfc31f825)
