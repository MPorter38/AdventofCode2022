# input is a grid of numbers that represent tree heights 
# the output we want is the number of trees that can be seen from outside the grid. This is the number of tree heights
# that are taller than all of the tree either up/down/left/right from the tree to the edge of the grid

import numpy as np

f = "Day8Example.txt" 

with open(f,"r") as file:
    num_line = (sum(1 for line in file))

with open(f,"r") as file:
    line_length = len(list(file.readline().strip()))

grid = np.zeros((num_line, line_length)) 
 
with open(f,"r") as file:
    for i in range(0,num_line):
        grid[i,:] = list(file.readline().strip())

counter = (2 * num_line) + (2 * (line_length-2)) 

for j in range(1,num_line-1):
    for k in range(1,line_length-1):
        tree = grid[j,k]
        updown = grid[:,k]
        leftright = grid[j,:]
        if tree > max(updown[0:j]):
            counter += 1 
        elif tree > max(updown[j+1:num_line]):
            counter +=1 
        elif tree > max(leftright[0:k]):
            counter +=1 
        elif tree > max(leftright[k+1:line_length]):
            counter +=1 

print(counter)

# Part 2 
# We now want the output to be the max scenic score of the trees in the grid. 
# this score is the amount of trees that can be seen in each direction multiplied together

score = 0
grid = grid[1:num_line-1, 1:line_length-1]

for j in range(0,num_line-2):
    for k in range(0,line_length-2):
        tree = grid[j,k]
        updown = grid[:,k]
        leftright = grid[j,:]
        
        up=1
        if j!=0:
            x=j-1 
            while tree > updown[x] and x>-1:
                up+=1 
                x-=1 
        
        down=1 
        if j!=num_line-2:
            x=j+1
            while x<num_line-2 and tree > updown[x]:
                down+=1
                x+=1
        
        left=1 
        if k!=0:
            x=k-1
            while tree>leftright[x] and x>-1:
                left+=1
                x-=1
        
        right=1
        if k!=line_length-2:
            x=k+1
            while x<line_length-2 and tree>leftright[x]:
                right+=1
                x+=1
        
        if (up * down * left * right) > score:
            score = up * down * left * right
        
print(score)
