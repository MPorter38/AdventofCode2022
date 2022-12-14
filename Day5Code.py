# the input is an arrangements of crates and a set of movement instructions 
# the output we want is the top crate of each stake after the instructions have been applied 

import numpy as np 
import re 

def parse_txt(f,depth,moves,nstacks):
# f is file, depth is how many items are in each crate to begin with, moves is the number of lineof instruction
# nstacks is the number of stacks
    ins = np.zeros((moves,3))
    stack = np.empty((depth,nstacks),dtype="str")

    with open(f,'r') as file:
        for i in range(0,depth):
            a_line = file.readline()
            for k in range(0,nstacks):
                stack[i,k] = a_line[k*4 + 1]
                    
        for j in range(depth+2,moves+depth+2):
            b_line = file.readline()
            if b_line[0] == "m":
                ins[j-depth-2,0] = re.search('move (\d+)',b_line).group(1)
                ins[j-depth-2,1] = re.search('from (\d+)',b_line).group(1)
                ins[j-depth-2,2] = re.search('to (\d+)',b_line).group(1)
                
    return(stack, ins)

# no_stacks = 9
# stack_depth = 8
# no_moves = 505
no_stacks = 3
stack_depth = 3
no_moves = 4

(stack, moves)=parse_txt('Day5Example.txt',stack_depth, no_moves, no_stacks)

stack_list = list()
for k in range(0,no_stacks):
    x= list(stack[:,k])
    x[:] = (value for value in x if value!=' ')
    stack_list.append(x)

# for m in range(0,no_moves):
#     a_move = moves[m,:].astype(int)
#     for l in range(0,a_move[0]):
#         crate = stack_list[a_move[1]-1][0]
#         stack_list[a_move[2]-1].insert(0,crate)
#         stack_list[a_move[1]-1].pop(0)

# print(stack_list)

# Part 2 
# When multiple crates are moved they now stay in the same order rather than moving one by one 
print(moves)
for m in range(0,no_moves):
    a_move = moves[m,:].astype(int)
    print(a_move)
    for l in range(0,a_move[0]):
        crates = stack_list[a_move[1]-1][0:a_move[0]+1]
        stack_list[a_move[2]-1].insert(0,crates)
        for i in range(0,a_move[0]-1):
            stack_list[a_move[1]-1].pop(i)

print(stack_list)