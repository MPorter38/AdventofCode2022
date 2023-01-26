from collections import deque
encrypted = deque()
with open("Day20Example.txt","r") as file:
    for line in file:
        encrypted.append(int(line.strip()))

enumerated = deque(enumerate(encrypted.copy()))

for original_index in range(len(encrypted)):
    while enumerated[0][0] != original_index:
        enumerated.rotate(-1)
    value_pair = enumerated.popleft()
    enumerated.rotate(-(value_pair[1] % len(enumerated)))
    enumerated.append(value_pair)

def value_in_position(values,position):
    adjusted_pos = (values.index(0) + position) % len(values)
    return values[adjusted_pos]

coords = 0 
for n in (1000,2000,3000):
    coords += value_in_position([v[1] for v in enumerated],n)

print(f'Part 1 is {coords}')

decryption = deque()
for i,value in enumerate(encrypted):
    decryption.append((i,811589153 * value))

for i in range(10):
    for original_index in range(len(encrypted)):
        while decryption[0][0] != original_index:
            decryption.rotate(-1)
        value_pair = decryption.popleft()
        decryption.rotate(-(value_pair[1] % len(decryption)))
        decryption.append(value_pair)

coords = 0 
for n in (1000,2000,3000):
    coords += value_in_position([v[1] for v in decryption],n)

print(f'Part 2 is {coords}')