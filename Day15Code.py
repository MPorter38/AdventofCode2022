import re
Sx=list()
Sy=list()
Bx=list()
By=list()
Y = 2000000
with open("Day15Input.txt","r") as file:
    while True:
        a_line = file.readline().strip()
        if not a_line:
            break
        b_line = a_line.split(":")[0]
        c_line = a_line.split(":")[1]

        Sx.append(int(re.search('x=(-?\d+)',b_line).group(1)))
        Sy.append(int(re.search('y=(-?\d+)',b_line).group(1)))
        Bx.append(int(re.search('x=(-?\d+)',c_line).group(1)))
        By.append(int(re.search('y=(-?\d+)',c_line).group(1)))

DistSB = list()
focus_row = set()
for i in range(0,len(Sx)):
    DistSB.append(abs(Sx[i]-Bx[i]) + abs(Sy[i]-By[i]))

    if abs(Sy[i] - Y) <= DistSB[i] :    
        spread = DistSB[i] - abs(Y-Sy[i])  
        focus_row.add(Sx[i])
        #print(Sx[i],Sy[i],Bx[i], By[i],DistSB[i], spread)
        for j in range(1,int(spread)+1):
            #print(Sx[i]+j, Sx[i]-j)
            focus_row.add(Sx[i]-j)
            focus_row.add(Sx[i]+j)

for i in range(0,len(Sx)):       
    if By[i] == Y and Bx[i] in focus_row:
        focus_row.remove(Bx[i])

print(len(focus_row))