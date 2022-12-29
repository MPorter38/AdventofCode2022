import re 

with open("Day7Input.txt","r") as file:
    current_path = list()
    dir_dic = {}
    for line in file:
        if len(line)>5 and line[5] == ".":
            current_path.pop(0)
        elif line[2] == "c":
            current_path.insert(0,line[5:].strip())
            current_dir = list()
        if line[0] != "$":
            current_dir.append(line.strip())
            dir_dic[''.join(current_path)]= current_dir

def get_filesize(key,dic):
    file_size=0
    chunk = dic[key]
    for entry in chunk:
        if entry[0] != "d":
            file_size += int(re.search(r'\d+',entry).group())
        else:
            new_key = entry[4:] + key
            file_size+= get_filesize(new_key,dic)
    return file_size

ans = 0 

for key in dir_dic:
    dir_size = get_filesize(key,dir_dic)
    if dir_size <= 100000:
        ans += dir_size
print(f'Answer to Part 1 is {ans}')

to_remove=get_filesize('/',dir_dic)
space_needed = 30000000 - (70000000 - to_remove)

for key in dir_dic:
    dir_size = get_filesize(key,dir_dic)
    if dir_size >= space_needed :
        to_remove=min(dir_size,to_remove)

print(f'Answer to Part 2 is {to_remove}')
