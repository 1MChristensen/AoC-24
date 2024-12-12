import numpy as np
from tqdm import tqdm
filename = '/home/matt/AOC/24/data/test'
filename = '/home/matt/AOC/24/data/11.txt'

with open(filename, 'r') as file:
    data = file.read().split(' ')

stones = [str(i) for i in range(10)]

# find maximum integer for which under this there is closure

max_stones = np.max(np.array(data, dtype=int))
print(max_stones)

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