# Input is a string of characters 
# the output we want is the location of the first block of fourth unique letters in the string 
# we want the index of the first character where the itself and the three characters before it are unique

# letter_bank = list()
# counter = 0 

# with open("Day6Input.txt","r") as file:
#     a_str = file.readline()
#     num_char = len(a_str)
#     for i in range(3,num_char):
#         letter = a_str[i]
#         block = list(a_str[i-3:i+1])
#         # print("Block", block)
#         if len(block) <= len(set(block)):
#             print(i+1)
#             break

#Part 2 - now look for the first unique block of 14 numbers

letter_bank = list()
counter = 0 

with open("Day6Input.txt","r") as file:
    a_str = file.readline()
    num_char = len(a_str)
    for i in range(13,num_char):
        letter = a_str[i]
        block = list(a_str[i-13:i+1])
        # print("Block", block)
        if len(block) <= len(set(block)):
            print(i+1)
            break