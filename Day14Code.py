import re 

y_max = 0 
x_left = 500
rock_coords = list()
with open("Day14Example.txt","r") as file:
    for line in file:
        line = line.split("->")
        coord_list = list()
        for coord in line:
            end_coord = (int(re.search("\d+",coord).group()), int(re.search(",\d+",coord).group()[1:]))
            y_max = max(y_max,end_coord[1])
            x_left = min(x_left,end_coord[0])
            rock_coords.append(end_coord)
            coord_list.append(end_coord)
            if len(coord_list)>1:
                start_coord = coord_list[0]
                if start_coord[0] == end_coord[0]:
                    miny = min(start_coord[1],end_coord[1])
                    maxy = max(start_coord[1],end_coord[1])
                    for i in range(miny+1,maxy):
                        rock_coords.append((start_coord[0],i))
                if start_coord[1] == end_coord[1]:
                    minx = min(start_coord[0],end_coord[0])
                    maxx = max(start_coord[0],end_coord[0])
                    for i in range(minx+1,maxx):
                        rock_coords.append((i,start_coord[1]))
                coord_list.pop(0)

def drop_sand(rocks:list, ymax:int, xleft:int):
    sand_coords=[500,0]
    while True:
        if sand_coords[1]>=ymax or sand_coords[0]<=xleft:
            return False  
        elif (sand_coords[0],sand_coords[1]+1) not in rocks:
            sand_coords[1] += 1 
        elif(sand_coords[0]-1,sand_coords[1]+1) not in rocks:
            sand_coords[0] -= 1
            sand_coords[1] += 1 
        elif (sand_coords[0]+1,sand_coords[1]+1) not in rocks:
            sand_coords[0] += 1
            sand_coords[1] += 1    
        else:
            rocks.append((sand_coords[0],sand_coords[1]))
            break 
    return True

original_coords = rock_coords.copy()
# grains=0
# while True:
#     x=drop_sand(rock_coords,y_max,x_left)
#     if x:
#         grains+=1 
#         # to see progress while code is running - 
#         #print(grains)
#     else:
#         break

# print(f'Part 1 answer is {grains}')

def drop_sand_with_floor(rocks:list, ymax:int):
    sand_coords=[500,0]
    while sand_coords[1]<ymax-1:
        if (sand_coords[0],sand_coords[1]+1) not in rocks:
            sand_coords[1] += 1 
        elif(sand_coords[0]-1,sand_coords[1]+1) not in rocks:
            sand_coords[0] -= 1
            sand_coords[1] += 1 
        elif (sand_coords[0]+1,sand_coords[1]+1) not in rocks:
            sand_coords[0] += 1
            sand_coords[1] += 1    
        else:
            rocks.append((sand_coords[0],sand_coords[1]))
            break
    rocks.append((sand_coords[0],sand_coords[1]))

rock_coords=original_coords.copy()
grains=0
while True:
    drop_sand_with_floor(rock_coords,y_max+2)
    grains+=1 
    # to see progress while code is running - 
    print(grains,rock_coords[-1])
    if (500,0) in rock_coords:
            break

print(f'Part 2 answer is {grains}')