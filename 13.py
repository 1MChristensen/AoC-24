import numpy as np
from numpy.linalg import solve
import re

filename = '/home/matt/AOC/24/data/test'
filename = '/home/matt/AOC/24/data/13.txt'

with open(filename, 'r') as file:
    data = file.read()

#data = np.array([[s for s in string] for string in data])
#print(data)
nums = [int(i) for i in re.findall(r'\d+', data)]
games = [[n for n in nums[6*i: 6*(i+1)]] for i in range(len(nums)//6)]

for i in range(len(games)):
    games[i][-2] += 10000000000000
    games[i][-1] += 10000000000000

print(games)

#print(games)

cost = 0
for game in games:
    A = np.array([[game[0], game[2]], [game[1], game[3]]])

    b = np.array([game[4], game[5]])
    
    sol = solve(A, b)

    print(sol[0], np.isclose(sol[0], round(sol[0]), rtol=1e-15))

    if (np.isclose(sol[0], round(sol[0]), rtol=1e-15)) and (np.isclose(sol[1], round(sol[1]), rtol=1e-15)):
        cost += sol[0]*3
        cost += sol[1]

print(cost)