# The input is games of rock paper scissor where the first letter (A-Rock, B-Paper, C-Scissor) plays against the second letter 
# (X-Rock, Y-Paper, Z-Scissor) and we are the second letter. 
# The output we want is the total score. We calculate this in two parts:
# 6 for a win, 3 for a draw and 0 for a lose 
# 1 for using rock (X), 2 for paper (Y) and 3 for scissor (Z) 

file_name = 'Day2Example.txt'

score1 = 0 

def add_hand_score(hand):
    score = 3 
    if hand == 'X':
        score =  1 
    elif hand == 'Y':
        score =  2
    return score

def add_comparison_score(hand1, hand2):
    score = 0
    if hand1 == 'A':
        if hand2 == 'X':
            score += 3
        elif hand2 == 'Y':
            score += 6 
    elif hand1 == 'B':
        if hand2 == 'Z':
            score += 6
        elif hand2 == 'Y':
            score += 3 
    else:
        if hand2 == 'X':
            score += 6
        elif hand2 == 'Z':
            score += 3 
    return score

with open(file_name,'r') as file:
    for line in file:
        first_hand = line.split()[0]
        second_hand = line.split()[1]

        score1 += add_hand_score(second_hand)
        score1 += add_comparison_score(first_hand,second_hand)

print(f'Part 1 is {score1}')

# part 2
# the second column says how the round needs to end: 
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.

score2 = 0  

def add_score(hand1, hand2):
    score = 0
    if hand2 == 'Y':
        score += 3 
        if hand1 == 'A':
            score += 1
        elif hand1 == 'B':
            score += 2
        else:
            score += 3

    elif hand2 == 'Z':
        score += 6
        if hand1 == 'A':
            score += 2
        elif hand1 == 'B':
            score += 3
        else:
            score += 1 
            
    else:
        if hand1 == 'A':
            score += 3
        elif hand1 == 'B':
            score += 1
        else:
            score += 2
    return score

with open(file_name,'r') as file:
    for line in file:
        first_hand = line.split()[0]
        second_hand = line.split()[1]
        score2 += add_score(first_hand,second_hand)
        
print(f'Part 2 is {score2}')