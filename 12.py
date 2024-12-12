import numpy as np
from sklearn.cluster import DBSCAN

filename = '/home/matt/AOC/24/data/test'
#filename = '/home/matt/AOC/24/data/12.txt'

with open(filename, 'r') as file:
    data = file.read().split('\n')

data = np.array([[s for s in string] for string in data])
print(data)

# Find all the regions
regions = {}

# find distinct letters

plants = np.unique(data.flatten())

N = len(data[0])-1

def checkConnected(locations):

    if len(locations) == 1:
        return {0: locations}

    db = DBSCAN(eps=1, min_samples=1).fit(locations)
    labels = db.labels_


    regions = {}
    for label, point in zip(labels, locations):
        if label != -1: 
            regions.setdefault(label, []).append(point)

    return regions

price = 0
for plant in plants:
    locations = np.where(data == plant)

    locations = [(locations[0][i], locations[1][i]) for i in range(len(locations[0]))]

    # Check if all coords are connected

    regions = checkConnected(locations)


    for key in regions:
        # Find the area - the number of distinct points in each region
        area = len(regions[key])
        #print(plant, regions[key])
        # Find perimeter
        #perimeter = 0
        #for point in regions[key]:
        #    neighbour = 0

        #    # Check for number of neighbours
        #    x, y = point
        #    # Check up
        #    if (x - 1, y) in regions[key]:
        #        neighbour += 1
        #    
        #    # Check right 
        #    if (x, y + 1) in regions[key]:
        #        neighbour += 1
        #    
        #    # Check down
        #    if (x + 1, y) in regions[key]:
        #        neighbour += 1

        #    # Check left
        #    if (x, y - 1) in regions[key]:
        #        neighbour += 1

        #    air = 4 - neighbour

        #    perimeter += air

        #price += perimeter*area

        # Find number of sides
        sides = 0

        edges = []

        for point in regions[key]:
            x, y = point
            # look up
            if (x - 1, y) not in regions[key]:
                edges.append((x,y,0))

            # look right
            if (x, y + 1) not in regions[key]:
                edges.append((x,y,1))

            # look down
            if (x + 1, y) not in regions[key]:
                edges.append((x,y,2))

            # look left
            if (x, y - 1) not in regions[key]:
                edges.append((x,y,3))

        # Now look in each direction, and see if the points are adjacent
        # If they are not adjacent, append to a list

        direction = [0,1,2,3]

        for d in direction:
            edge = [edge for edge in edges if edge[2] == d]
            #print(len(checkConnected(edge)))
            sides += len(checkConnected(edge))


        #print(plant, edges)
        #print(sides)
        price += sides*area

print(price)