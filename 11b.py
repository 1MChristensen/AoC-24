import numpy as np
from tqdm import tqdm
filename = '/home/matt/AOC/24/data/test'
filename = '/home/matt/AOC/24/data/11.txt'

with open(filename, 'r') as file:
    data = file.read().split(' ')

#stones = [str(i) for i in range(10)]

# find maximum integer for which under this there is closure

max_stones = np.max(np.array(data, dtype=int))
#print(max_stones)

max_i = 0

foundClosure = False
#while not foundClosure:
#
#    stone = str(max_i)
#
#    new_stones = []
#
#    if stone == '0':
#        new_stones.append('1')
#
#    elif len(stone)%2 == 0:
#        l = len(stone)//2
#        new_stones.append(stone[:l])
#        new_stones.append(str(int(stone[l:])))
#
#    else:
#        new_stones.append(str(int(stone)*2024))
#
#    new_max = np.max(np.array(new_stones, dtype=int))
#    #print(max_i, new_max)
#
#    if (new_max < max_i) and (max_i > max_stones):
#        foundClosure = True
#    max_i += 1
#
#print('Found closure', max_i)

# Now need to find the number of rocks each number under this makes

max_i = 10000001
max_i = 100

def blink(stones):
    new_stones = []
    for stone in stones:
        stone = str(stone)
        if stone == '0':
            new_stones.append('1')

        elif len(stone)%2 == 0:
            l = len(stone)//2
            new_stones.append(stone[:l])
            new_stones.append(str(int(stone[l:])))

        else:
            new_stones.append(str(int(stone)*2024))


    return new_stones



print(data)

searched = []
to_search = data
next_search = []

paths = {}
depths = {}

depth = 0

while to_search:
    next_search = []
    for stone in to_search:
        #print(depth, stone)
        new_stones = blink([stone])

        if stone not in searched:
            paths[stone] = new_stones
            depths[stone] = depth
        
        searched.append(stone)


        next_search += [ns for ns in new_stones if ns not in searched]
    depth += 1
    to_search = next_search
    #print(to_search)
    #if depth == 2:break
print(len(searched))

blinks = 75

nodes = dict.fromkeys(searched, 0)

for stone in data:
    nodes[stone] = 1

for blink in range(blinks):

    new_nodes = dict.fromkeys(searched, 0)
    d = range(max(depths.values()))
    
    for node in nodes:
        for target_node in paths[node]:
            new_nodes[target_node] += nodes[node]

    nodes = new_nodes

print(sum(nodes.values()))