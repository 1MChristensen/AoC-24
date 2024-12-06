import numpy as np
import re 

#filename = '/home/matt/AOC/24/data/test'
filename = '/home/matt/AOC/24/data/6.txt'

with open(filename, 'r') as file:
    data = file.read()

lines = re.split('\n', data)

array_data = np.array([list(line) for line in lines if line])
print(array_data)

bounds = array_data.shape[0] - 1
#print(bounds)
current_state = []


for d in ['>', 'v', '<', '^']:
    if np.where(array_data == d)[0].size > 0:
        current_state.append([np.where(array_data == d)[i][0] for i in range(2)])
        current_state.append(d)

save_state = current_state.copy()

#print(current_state)

history = [current_state[0]]

def is_In_Bounds(state):
    d = state[1]
    x = state[0][0]
    y = state[0][1]

    if d == '^':
        if x-1 < 0:
            return False

    if d == '>':
        if y+1 > bounds:
            return False
        
    if d == 'v':
        if x+1 > bounds:
            return False
        
    if d == '<':
        if y-1 < 0:
            return False
        
    return True
    
#print(is_In_Bounds([[0,1],'<']))

inDomain = True

while inDomain:

    noCollision = True
    
    while noCollision:
        x = current_state[0][0]
        y = current_state[0][1]

        if not is_In_Bounds(current_state):
            inDomain = False
            break


        if current_state[1] == '^':

            if array_data[x-1, y] == '#':
                noCollision = False
                break
            else:
                current_state[0] = [x-1, y]
                history.append(current_state[0])

        if current_state[1] == '>':

            if array_data[x, y+1] == '#':
                noCollision = False
                break
            else:
                current_state[0] = [x, y+1]
                history.append(current_state[0])
    
        if current_state[1] == 'v':

            if array_data[x+1, y] == '#':
                noCollision = False
                break
            else:
                current_state[0] = [x+1, y]
                history.append(current_state[0])

        if current_state[1] == '<':

            if array_data[x, y-1] == '#':
                noCollision = False
                break
            else:
                current_state[0] = [x, y-1]
                history.append(current_state[0])

    if current_state[1] == '>':
        current_state[1] = 'v'
        continue

    if current_state[1] == 'v':
        current_state[1] = '<'
        continue

    if current_state[1] == '<':
        current_state[1] = '^'
        continue

    if current_state[1] == '^':
        current_state[1] = '>'
        continue

history = [h for i,h in enumerate(history) if h not in history[:i]]

print(len(history))

################################################################

locations = [[x,y] for x in range(bounds+1) for y in range(bounds+1)]

save_map = array_data.copy()

#print(locations)

found_loops = 0

for O in locations:

    current_state = save_state.copy()
    array_data = save_map.copy()
    #print(array_data)
    #print(current_state)
    if O != current_state[0]:
        print('Obstruct placed at', O)
        array_data[O[0], O[1]] = '#'
        #print(array_data)

    history = []

    inDomain = True

    while inDomain:

        noCollision = True
        
        while noCollision:
            x = current_state[0][0]
            y = current_state[0][1]

            if not is_In_Bounds(current_state):
                inDomain = False
                break

            if current_state[1] == '^':

                if array_data[x-1, y] == '#':
                    noCollision = False
                    break
                else:
                    current_state[0] = [x-1, y]
                    if current_state in history:
                        inDomain = False
                        found_loops += 1
                        break
                        
                    history.append([current_state[0], current_state[1]])

            if current_state[1] == '>':

                if array_data[x, y+1] == '#':
                    noCollision = False
                    break
                else:
                    current_state[0] = [x, y+1]
                    if current_state in history:
                        inDomain = False
                        found_loops += 1
                        break

                    history.append([current_state[0], current_state[1]])
        
            if current_state[1] == 'v':

                if array_data[x+1, y] == '#':
                    noCollision = False
                    break
                else:
                    current_state[0] = [x+1, y]
                    if current_state in history:
                        inDomain = False
                        found_loops += 1
                        break

                    history.append([current_state[0], current_state[1]])

            if current_state[1] == '<':

                if array_data[x, y-1] == '#':
                    noCollision = False
                    break
                else:
                    current_state[0] = [x, y-1]
                    if current_state in history:
                        inDomain = False
                        found_loops += 1
                        break

                    history.append([current_state[0], current_state[1]])

        if current_state[1] == '>':
            current_state[1] = 'v'
            continue

        if current_state[1] == 'v':
            current_state[1] = '<'
            continue

        if current_state[1] == '<':
            current_state[1] = '^'
            continue

        if current_state[1] == '^':
            current_state[1] = '>'
            continue

    #print(history)

print('Found loops', found_loops)