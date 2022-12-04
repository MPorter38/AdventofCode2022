# The input is a list of the calories in each item that is being caried, where the blank rows seperate what each elf is carrying. 
# The output required is how many total calories is the elf that is carrying the most calories carrying?
# ie which block of numbers add up to the highest total 

file_name = 'Day1Input.txt'

with open(file_name,'r') as file:
    num_lines = (sum(1 for line in file)) + 1

cal_counts = [0] #calorie count for each elf
elf_count = 0 #count number of elves

with open(file_name,'r') as file:
    for i in range(1,num_lines,1):
        a_line = file.readline()
        if a_line == "\n":
            elf_count = elf_count + 1 
            cal_counts.append(0)
        else:
            cal_counts[elf_count] = cal_counts[elf_count] + int(a_line)

print("The max is ", (max(cal_counts)))

# Extra Part - Find the sum of the top three

print("The sum of the top three is", sum(sorted(cal_counts, reverse=True)[:3]))


