# use bfs algorithm to find the shortest path from S to E 
# the letters relate to heights where we can go up one level at most (e.g. a->b) and down as many as we like

map = list()

with open("Day12Example.txt","r") as file:
    while True:
        a_line = file.readline()
        if not a_line:
            break
        map.append(list(a_line.strip()))

for i in range(0,len(map)):
    if "E" in map[i]:
        node2 = i*len(map[0]) + map[i].index("E")
        map[i][map[i].index("E")] = "z"
        
graph ={}
for i in range(0,len(map)):
    for j in range(0,len(map[0])):
        sq_height = map[i][j]
        adj = list()
        if sq_height == "S":
            sq_height = "a"
            node1 = i*len(map[0]) + j    
        if i != 0:
            up = map[i-1][j]
            if ord(sq_height)+1 >= ord(up):
                adj.append((i-1)*len(map[0])+j)
        if i != len(map)-1:
            down = map[i+1][j]
            if ord(sq_height)+1 >= ord(down):
                adj.append((i+1)*len(map[0])+j)
        if j != 0:
            left = map[i][j-1]
            if ord(sq_height)+1 >= ord(left):
                adj.append((i)*len(map[0])+(j-1))
        if j !=len(map[0])-1:
            right = map[i][j+1]
            if ord(sq_height)+1 >= ord(right):
                adj.append((i)*len(map[0])+(j+1))
        graph[i*len(map[0])+j] = adj

def short_path(graph,start,end):
    path_list = [[start]]
    path_index =0 
    visited = {start}
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        if end in next_nodes:
            current_path.append(end)
            return current_path
        for next_node in next_nodes:
            if not next_node in visited:
                new_path=current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                visited.add(next_node)
        path_index +=1
    return[]

#Part 1 
# print(short_path(graph,node1,node2))

# print(len(short_path(graph,node1,node2)))

# Part 2 

path_len =[]
for k in range(0,len(map)):
    a_locs= list(i for i,x in enumerate(map[k]) if x=="a")
    for a in a_locs:
        length = len(short_path(graph,a+k*len(map[0]),node2))
        if length != 0:
            path_len.append(length)

print(min(path_len))