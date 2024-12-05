import re
import numpy as np
import itertools

filename = '/home/matt/AOC/24/data/test'
filename = '/home/matt/AOC/24/data/5.txt'

with open(filename, 'r') as file:
    data = file.read()

lines = re.split('\n', data)

#print(lines)

# find the '' point

updates = []
for i in range(len(lines)):
    
    if lines[-i-1] == '':
        break

    updates.append(lines[-i-1])

page_ordering = lines[:-i-1]    

page_ordering = [[int(re.split(r'\|', line)[0]), int(re.split(r'\|', line)[1])] for line in page_ordering]

updates = [[int(j) for j in re.split(r'\,', line)] for line in updates]

correct_updates = []
bad_updates = []
for update in updates:
    correct = True
    for i, x in enumerate(update):
        # Now seach all the instructions
        for order in page_ordering:
            if order[0] == x:
                # Need to check all numbers to the left
                if any(y == order[1] for y in update[:i]):
                    correct = False
                    #print(order,update[i:])
    if correct:
        correct_updates.append(update)
    if not correct:
        bad_updates.append(update)

#print(correct_updates)

# Now sum over middle parts
middle_sum = sum([update[int(len(update)/2)] for update in correct_updates])
print(middle_sum)

def check_correct(orders, List):
    for i, x in enumerate(List):
        for order in orders:
            if x == order[0]:
                if any(y == order[1] for y in List[:i]):
                    return False
                
    return True

print(check_correct(page_ordering, [75,97,47,61,53]))

new_correct_updates = []

for update in bad_updates:
    correct = False

    while(not correct):
        for i, x in enumerate(update):
            for order in page_ordering:
                if x == order[0]:
                    for j, y in enumerate(update[:i]):
                        if y == order[1]:
                            # We have found a bad placement to the left of the original check
                            # Now we need to swap these two points
                            #print(update)
                            tmp = update[i]
                            update[i] = update[j]
                            update[j] = tmp
                            #print(update)
        if check_correct(page_ordering, update):
            correct = True
            new_correct_updates.append(update)



middle_sum = sum([update[int(len(update)/2)] for update in new_correct_updates])
print(middle_sum)