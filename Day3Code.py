# Input is a string of letters
# For the output we need to split the string in half and find the letter that is common to both halves
# This is then converted to a score (a=1, b=2,...,z=26,A=27,...,Z=52) and the output is the sum

file_name = 'Day3Input.txt'

with open(file_name,'r') as file:
    num_lines = (sum(1 for line in file))

# total = 0 

# with open(file_name,'r') as file:
#     for i in range(1,num_lines + 1):
#         a_line = file.readline()
#         midpoint = (len(a_line)-1)/2
#         first_set = list(a_line)[0:int(midpoint)]
#         second_set = list(a_line)[int(midpoint):len(a_line)-1]
#         common_letter = list(set(first_set) & set(second_set))[0]
#         common_letter = int(ord(common_letter))
#         if common_letter < 91:
#             common_letter = common_letter - 38
#         else:
#             common_letter = common_letter - 96 
        
#         total = total + common_letter

# file.close()

# print(total)

# Part 2
# Find the common letter between three consecutive rows and sum up as before 

total = 0 
common_letter = 0 

with open(file_name,'r') as file:
    for i in range(1,int(num_lines/3)+1):
        line1 = file.readline()
        line2 = file.readline()
        line3 = file.readline()
        set1 = set(line1)
        set1.remove('\n')
        set2 = set(line2)
        set2.remove('\n')
        set3 = set(line3)
        if i < (int(num_lines/3)):
            set3.remove('\n')
        common_letter = list(set1 & set2 & set3)[0]
        common_letter = int(ord(common_letter))
        
        if common_letter < 91:
            common_letter = common_letter - 38
        else:
            common_letter = common_letter - 96
        total += common_letter

file.close()

print(total)