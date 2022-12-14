# the input is a series of command. Either noop which means wait one cycle 
# or addx which take two cycles and then changes X by the number after it. Signal strength is given as cycle*X
# the output we the sum of the signal strength at cycle 20,60,100,140,180,220

import re
instruction = list()
values = list()
sign = list()
i=0

with open("Day10Input.txt","r") as file:
    while True:
        a_line = file.readline().strip()
        if not a_line:
            break
        
        instruction.append(list(a_line)[0])
        if list(a_line)[0]=="n":
            values.append('0')
            sign.append(" ")
        else:
            values.append(re.search('(\d+)',a_line).group(1))
            if list(a_line)[5]=="-":
                sign.append("-")
            else:
                sign.append("+")

cycle = list([0])

for i in range(0,len(instruction)):
    if instruction[i]=="n":
        cycle.append(cycle[i] + 1)
    else:
        cycle.append(cycle[i] + 2)

#print(len(cycle))

k=20
Total=0

for j in range(0,len(cycle)):
    X=1
    if cycle[j]<=k and cycle[j+1]>=k:
        for m in range(0,j):
            if sign[m]=="+":
                X+=int(values[m])
            elif sign[m]=="-":
                X-=int(values[m])
        Total += k*X
        k +=40
    if k>220:
        break

print(Total)   



