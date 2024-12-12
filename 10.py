import numpy as np
filename = '/home/matt/AOC/24/data/test'
#filename = '/home/matt/AOC/24/data/11.txt'
with open(filename, 'r') as file:
    data = file.read().split('\n')
trail_heads = []
nines = []
for x, line in enumerate(data):
    for y, letter in enumerate(line):
        if letter == '0':
            trail_heads.append((x,y))
        if letter == '9':
            nines.append((x,y))
data = np.array([[s for s in string] for string in data])
#print(data)
scores = 0
for head in trail_heads:
    elev = 0
    coords = [head]
    while (elev < 9):
        tmp_coords = []
        for i, coord in enumerate(coords):
            # Check up down left right
            x_co = coord[0]
            y_co = coord[1]    
            N = len(data)-1
            # Check below
            if (x_co - 1 >= 0):
                if (data[x_co - 1, y_co] == str(elev + 1)):
                    tmp_coords.append((x_co-1, y_co))
            # Check above
            if (x_co + 1 <= N):
                if (data[x_co + 1, y_co] == str(elev + 1)):
                    tmp_coords.append((x_co+1, y_co))
            # Check left
            if (y_co - 1 >= 0):
                if (data[x_co, y_co - 1] == str(elev + 1)):
                    tmp_coords.append((x_co, y_co-1))
            # Check above
            if (y_co + 1 <= N):
                if (data[x_co, y_co + 1] == str(elev + 1)):
                    tmp_coords.append((x_co, y_co+1))
        #print(coords)
        if len(tmp_coords) == 0:
            break
        coords = tmp_coords
        elev +=1
    
    if elev == 9:
        coords = coords
        scores += len(coords)
print(scores)

def traverse(elev, coords):
    
    tmp_coords = []
    
    for i, coord in enumerate(coords):
        # Check up down left right
        x_co = coord[0]
        y_co = coord[1]    
        N = len(data)-1
        # Check below
        if (x_co - 1 >= 0):
            if (data[x_co - 1, y_co] == str(elev + 1)):
                tmp_coords.append((x_co-1, y_co))
        # Check above
        if (x_co + 1 <= N):
            if (data[x_co + 1, y_co] == str(elev + 1)):
                tmp_coords.append((x_co+1, y_co))
        # Check left
        if (y_co - 1 >= 0):
            if (data[x_co, y_co - 1] == str(elev + 1)):
                tmp_coords.append((x_co, y_co-1))
        # Check above
        if (y_co + 1 <= N):
            if (data[x_co, y_co + 1] == str(elev + 1)):
                tmp_coords.append((x_co, y_co+1))

        coords = tmp_coords

        if len(coords) == 0:
            result = elev, coords
            #print(elev, coords)
        elif elev < 9:
            #print(elev, coords)
            result = traverse(elev+1, coords)

        return result
    

#print(traverse(0, [trail_heads[-1]]))