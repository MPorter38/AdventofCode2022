# the input is a series of movements for the head of the rope. The rope also has a tail that is always within touching distant of the head
# this can be vertically, horizontally or diagonally. The tail moves to follow the head around the area
# the output we want a count of the number of squares in the area that the tail occupies

import re

f = "Day9Example.txt" 

with open(f,"r") as file:
    num_line = (sum(1 for line in file))

direction = list()
distance = list()

with open(f,"r") as file:
    for line in file:
        a_line = line.strip()
        direction.append(list(a_line)[0])
        distance.append(int(re.search('(\d+)',a_line).group(1)))

# positions relative to start of (0,0)

T_pos_all = set()
T_pos_all.add((0,0))
T_pos = [0,0]
H_pos = [0,0]
pos_dif = [0,0]
abs_pos_dif = [0,0]

for j in range(0,num_line):
    for k in range(0,distance[j]):
        if direction[j] == "U":
            H_pos[1] += 1
        elif direction[j] == "D":
            H_pos[1] -= 1
        elif direction[j] == "L":
            H_pos[0] -= 1
        else:
            H_pos[0] += 1
        
        pos_dif[0] = (H_pos[0] - T_pos[0])
        pos_dif[1] = (H_pos[1] - T_pos[1])

        abs_pos_dif[0] = abs(H_pos[0] - T_pos[0])
        abs_pos_dif[1] = abs(H_pos[1] - T_pos[1])
        
        if (abs_pos_dif[0]>1 and abs_pos_dif[1]==1):
            T_pos[0] += pos_dif[0]/abs_pos_dif[0]  
            T_pos[1] += pos_dif[1]/abs_pos_dif[1]  
        elif (abs_pos_dif[1]>1 and abs_pos_dif[0]==1):
            T_pos[0]+= pos_dif[0]/abs_pos_dif[0]
            T_pos[1] += pos_dif[1]/abs_pos_dif[1]   
        elif abs_pos_dif[0]>1 and abs_pos_dif[1]==0:
            T_pos[0] += pos_dif[0]/abs_pos_dif[0] 
        elif abs_pos_dif[1]>1 and abs_pos_dif[0]==0:
            T_pos[1] += pos_dif[1]/abs_pos_dif[1]  

        T_pos_all.add(tuple(T_pos))

print(len(T_pos_all))
    