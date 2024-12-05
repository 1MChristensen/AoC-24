import numpy as np

data = np.loadtxt('/home/matt/AOC/24/data/1')
left = data[:, 0]
right = data[:, 1]

#left = np.array([3,4,2,1,3,3])
#right = np.array([4,3,5,3,9,3])

left_sort = np.sort(left)
right_sort = np.sort(right)

# First star
print(np.sum(np.abs(left_sort - right_sort)))

list = []
for i in left:
    n = len(np.where(right == i)[0])
    list.append(n*i)

print(np.sum(list))