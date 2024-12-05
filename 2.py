import numpy as np

#data = np.loadtxt('/home/matt/AOC/24/data/test')

#data = np.loadtxt('/home/matt/AOC/24/data/2')

filename = '/home/matt/AOC/24/data/2.txt'
#filename = '/home/matt/AOC/24/data/test'

with open(filename, 'r') as file:
    data = [list(map(float, line.split())) for line in file]

# First star
count = 0
for r in data:
    diff = np.diff(r)
    #print(diff)
    if all((diff<0) & (abs(diff) > 0) & (abs(diff) < 4)):
        count += 1
        #print('down')
    
    if all((diff>0) & (abs(diff) > 0) & (abs(diff) < 4)):
        count += 1
        #print('up')
    
print(count)

# Second star

checkMonotonicity = lambda x: (all(x<0)) or (all(x>0))
checkBounds = lambda x: (all(abs(x) > 0)) and (all(abs(x) < 4))
checkNumZeros = lambda x: len(np.where(x == 0)[0]) == 1
checkNumChanges = lambda x: (len(np.where(x <= 0)[0])==1) or (len(np.where(x >= 0)[0])==1)

#count = 0
#for r in data:
#    diff = np.diff(r)
#
#    if checkMonotonicity(diff):
#        if checkBounds(diff):
#            count += 1
#            print('vgood', r)
#        elif checkNumZeros(diff):
#            count += 1
#            print('good', r)
#    elif checkNumChanges(diff):
#        count += 1
#        print('reasonable', r, diff)
#

def isSafe(r):
    diff = np.diff(r)
    return (checkMonotonicity(diff)) and (checkBounds(diff))

count = 0

for r in data:
    if isSafe(r):
        count += 1
    else:
        for i in range(len(r)):
            r_tmp = r.copy()
            r_tmp.pop(i)
            if isSafe(r_tmp):
                count += 1
                break

print(count)