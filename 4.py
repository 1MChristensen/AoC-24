import numpy as np
import re

filename = '/home/matt/AOC/24/data/test'
filename = '/home/matt/AOC/24/data/4.txt'

with open(filename, 'r') as file:
    data = file.read()

lines = re.split('\n', data)

array_data = np.array([list(line) for line in lines if line])
print(array_data)

# First star
count = 0

for line in array_data:
    line = ''.join(line)
    # Search forwards
    count += len(re.findall(r'XMAS', line))

    # Search backwards
    count += len(re.findall(r'SAMX', line))
    
#print(count)

# Now flip the array
columns = array_data.transpose()

for line in columns:
    line = ''.join(line)
    # Search forwards
    count += len(re.findall(r'XMAS', line))

    # Search backwards
    count += len(re.findall(r'SAMX', line))


# Now get the forwards diagonals

diags = [''.join(array_data.diagonal(offset=int(-array_data.shape[0]+i))) for i in range(2*array_data.shape[0])]

for line in diags:
    line = ''.join(line)
    # Search forwards
    count += len(re.findall(r'XMAS', line))

    # Search backwards
    count += len(re.findall(r'SAMX', line))


# Now get backwards diagonals

back_array_data = np.fliplr(array_data)
diags = [''.join(back_array_data.diagonal(offset=int(-array_data.shape[0]+i))) for i in range(2*array_data.shape[0])]

for line in diags:
    line = ''.join(line)
    # Search forwards
    count += len(re.findall(r'XMAS', line))

    # Search backwards
    count += len(re.findall(r'SAMX', line))


print(count)

# Second star

# Split matrix into 3x3 sub array
dim = array_data.shape[0]
print(dim)

sub_matrices = [array_data[i:i+3,j:j+3] for i in range(dim-2) for j in range(dim-2)]

# Now search the sub matrices for the structure
count = 0

for matrix in sub_matrices:

    if ((matrix[0,0] == 'M') & (matrix[0,2] == 'M') & (matrix[2,0] == 'S') & (matrix[2,2] == 'S') & (matrix[1,1] == 'A')):
        #print(matrix)
        count +=1

    if ((matrix[0,0] == 'M') & (matrix[2,0] == 'M') & (matrix[0,2] == 'S') & (matrix[2,2] == 'S') & (matrix[1,1] == 'A')):
        #print(matrix)
        count +=1

    if ((matrix[2,0] == 'M') & (matrix[2,2] == 'M') & (matrix[0,0] == 'S') & (matrix[0,2] == 'S') & (matrix[1,1] == 'A')):
        #print(matrix)
        count +=1

    if ((matrix[0,2] == 'M') & (matrix[2,2] == 'M') & (matrix[0,0] == 'S') & (matrix[2,0] == 'S') & (matrix[1,1] == 'A')):
        #print(matrix)
        count +=1

print(count)