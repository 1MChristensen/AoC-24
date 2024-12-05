import numpy as np
import re

filename = '/home/matt/AOC/24/data/test'
filename = '/home/matt/AOC/24/data/3.txt'

with open(filename, 'r') as file:
    data = file.read().replace('\n', '')


# First star
brackets = re.findall(r'mul\([0-9]+,{1}[0-9]+\)', data)
brackets = [re.sub(r'mul', '', x) for x in brackets]
#print(brackets)
left = []
right = []
for t in brackets:
    #print(t)
    left.append(re.split(r'\,', t)[0])
    right.append(re.split(r'\,', t)[1])

left = np.array([int(re.sub(r'\(', '', x)) for x in left])
right = np.array([int(re.sub(r'\)', '', x)) for x in right])

print(left@right)

# Second star

# precondition the string first

split = re.split(r"do\(\)", data)
split = [re.split(r"don't\(\)", x)[0] for x in split]

string = ''
for s in split:
    string += s


brackets = re.findall(r'mul\([0-9]+,{1}[0-9]+\)', string)
brackets = [re.sub(r'mul', '', x) for x in brackets]
#print(brackets)
left = []
right = []
for t in brackets:
    #print(t)
    left.append(re.split(r'\,', t)[0])
    right.append(re.split(r'\,', t)[1])

left = np.array([int(re.sub(r'\(', '', x)) for x in left])
right = np.array([int(re.sub(r'\)', '', x)) for x in right])

print(left@right)

print(string)