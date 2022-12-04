# The input is games of rock paper scissor where the first letter (A-Rock, B-Paper, C-Scissor) plays against the second letter 
# (X-Rock, Y-Paper, Z-Scissor) and we are the second letter. 
# The output we want is the total score. We calculate this in two parts:
# 6 for a win, 3 for a draw and 0 for a lose 
# 1 for using rock (X), 2 for paper (Y) and 3 for scissor (Z) 

file_name = 'Day2Input.txt'

with open(file_name,'r') as file:
    num_lines = (sum(1 for line in file))

# score1 = 0 
# score2 = 0 

# with open(file_name,'r') as file:
#     for i in range(0, num_lines):
#         a_line = file.readline()
#         first_hand = a_line.split()[0]
#         second_hand = a_line.split()[1]

#         if second_hand == 'X':
#             score1 = score1 + 1 
#         elif second_hand == 'Y':
#             score1 = score1 + 2
#         else:
#             score1 = score1 + 3

#         if first_hand == 'A':
#             if second_hand == 'X':
#                 score2 = score2 + 3
#             elif second_hand == 'Y':
#                 score2 = score2 + 6 
#         elif first_hand == 'B':
#             if second_hand == 'Z':
#                 score2 = score2 + 6
#             elif second_hand == 'Y':
#                 score2 = score2 + 3 
#         else:
#             if second_hand == 'X':
#                 score2 = score2 + 6
#             elif second_hand == 'Z':
#                 score2 = score2 + 3 

# print(score2 + score1)

# part 2
# the second column says how the round needs to end: 
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.

score3 = 0 
score4 = 0 

with open(file_name,'r') as file:
    for i in range(0, num_lines):
        a_line = file.readline()
        first_hand = a_line.split()[0]
        second_hand = a_line.split()[1]
        
        if second_hand == 'Y':
            score3 = score3 + 3 
            if first_hand == 'A':
                score4 = score4 + 1
            elif first_hand == 'B':
                score4 = score4 + 2
            else:
                score4 = score4 +3

        elif second_hand == 'Z':
            score3 = score3 + 6
            if first_hand == 'A':
                score4 = score4 + 2
            elif first_hand == 'B':
                score4 = score4 + 3
            else:
                score4 = score4 + 1 
                
        else:
            if first_hand == 'A':
                score4 = score4 + 3
            elif first_hand == 'B':
                score4 = score4 + 1
            else:
                score4 = score4 + 2
        


print(score3 + score4)