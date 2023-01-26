xyz = []

with open("Day18Example.txt","r") as file:
    for line in file:
        line = line.split(",")
        xyz.append((int(line[0]),int(line[1]),int(line[2])))

def face_generator(x, y, z):
    yield(x,y,z,x-1,y-1,z)
    yield(x,y,z-1,x-1,y-1,z-1)
    yield(x,y,z,x,y-1,z-1)
    yield(x-1,y,z,x-1,y-1,z-1)
    yield(x,y-1,z,x-1,y-1,z-1)
    yield(x,y,z,x-1,y,z-1)

def find_unique_faces(input):
    faces = {}
    for i in range(0,len(input)):
        for face in face_generator(*xyz[i]):
            if face in faces.keys():
                faces[face] +=  1
            else:
                faces[face] = 1 
    return set(face for face in faces if faces[face]==1)

print(len(find_unique_faces(xyz)))

#part 2 floodfill
