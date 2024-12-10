import numpy as np
from tqdm import tqdm
import sys
filename = '/home/matt/AOC/24/data/test'
#filename = '/home/matt/AOC/24/data/8.txt'

np.set_printoptions(threshold=sys.maxsize)

with open(filename, 'r') as file:
    data = file.read()

#print(data)

s = []

for i in range(len(data)//2):
    s.append([i for _ in range(int(data[2*i]))])
    s.append([None for _ in range(int(data[2*i + 1]))])

s.append([i+1 for _ in range(int(data[2*i+2]))])


non_none = np.flip([x for xs in s for x in xs if x is not None])
N = len(non_none)
none = np.array([x for xs in s for x in xs if x is None])

replaced = 0

for i in range(len(data)//2):
    if replaced == len(none):
        break
    s[2*i+1] = non_none[:len(s[2*i+1])]
    non_none = non_none[len(s[2*i+1]):]
    replaced += len(s[2*i+1])
                        
s = [x for xs in s for x in xs]

s = s[:N]



def checksum(s):
    return sum([i*x for i, x in enumerate(s) if x is not None])

#print(s)
print(f'first star: {checksum(s)}')

s = []

for i in range(len(data)//2):
    s.append([i for _ in range(int(data[2*i]))])
    s.append([None for _ in range(int(data[2*i + 1]))])

s.append([i+1 for _ in range(int(data[2*i+2]))])


c = [x for xs in s for x in xs]

s = [x for x in s[::-1]]


print(c)

def get_lengths_gaps(c):
    l = 0
    lengths = []
    for i in range(len(c)-1):
        if c[i] == c[i+1]:
            l +=1
        else:
            lengths.append(l+1)
            l=0
    lengths.append(l+1)
    return lengths[::-2], lengths[1::2]

lengths = np.array([int(x) for x in data[::-2]])
gaps = np.array([int(x) for x in data[1::2]])

for i, l in enumerate(lengths):
    
    loc = np.where(l<= gaps)[0]

    if loc.size == 0:
        continue
    
    print(l, s[2*i])

    
    

print(lengths, gaps)
print(get_lengths_gaps(c))