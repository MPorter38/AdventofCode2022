# Input is two ranges of numbers 
# The output we want is how many the ranges are completely within the other range of numbers
# Given a to b and x to y, we want to know if x>=a and y=<b or if a>=x and b=<y 

score =0 

with open("Day4Example.txt","r") as file:
    for line in file:
        a_line = line.strip()
        first_section = a_line.split(",")[0]
        second_section = a_line.split(",")[1]
        a = int(first_section.split("-")[0])
        b = int(first_section.split("-")[1])
        x = int(second_section.split("-")[0])
        y = int(second_section.split("-")[1])
        if x>=a and y<=b:
            score += 1 
        elif a>=x and b<=y:
            score += 1

print(score)

# part 2 - do they have any overlap at all?
# so given a-b and x-y, is a<=x<=b, a<=y<=b, x<=a<=y, x<=b<=y

score =0 

with open("Day4Example.txt","r") as file:
    for line in file:
        a_line = line.strip()
        first_section = a_line.split(",")[0]
        second_section = a_line.split(",")[1]
        a = int(first_section.split("-")[0])
        b = int(first_section.split("-")[1])
        x = int(second_section.split("-")[0])
        y = int(second_section.split("-")[1])
        if a<=x<=b or a<=y<=b:
            score += 1 
        elif x<=a<=y or x<=b<=y:
            score += 1

print(score)