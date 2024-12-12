import numpy as np
from tqdm import tqdm
filename = '/home/matt/AOC/24/data/test'
#filename = '/home/matt/AOC/24/data/11.txt'

with open(filename, 'r') as file:
    data = file.read().split(' ')

#print(data)

blinks = 75

stones = data[0]

for blink in tqdm(range(blinks)):
    new_stones = []
    #print(stones)
    for i, stone in enumerate(stones):
        if stone == '0':
            new_stones.append('1')

        elif len(stone)%2 == 0:
            l = len(stone)//2
            new_stones.append(stone[:l])
            new_stones.append(str(int(stone[l:])))

        else:
            new_stones.append(str(int(stone)*2024))

    stones = new_stones

#stones = np.array(stones, dtype=int)

print(len(stones))

