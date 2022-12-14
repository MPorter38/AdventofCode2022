input = list()
with open("Day13Input.txt","r") as file:
    for line in file:
        a_line = line.strip()
        if len(a_line)>1:
            input.append(eval(a_line))

def compare(left,right):
    for i in range(max(len(left),len(right))):
        if i == len(left):
            return True 
        if i == len(right):
            return False
        if type(left[i]) is int and type(right[i]) is int:
            if left[i] is not right[i]:
                return left[i]<right[i]
        else:
            result = compare(left[i] if type(left[i]) is list else [left[i]],right[i] if type(right[i]) is list else [right[i]])
            if result is not None:
                return result

#print(compare(input[1],input[1+1]))
total = 0 
k=0
for i in range(0,len(input),2):
    result = compare(input[i],input[i+1])
    k+=1
    if result:
        total += k

print(total)

# part 2

decoder1 = [[2]]
decoder2 = [[6]]

total1 = 1 
total2 = 2
for i in range(0,len(input)):
    result = compare(input[i],decoder1)
    if result:
        total1 += 1
    result = compare(input[i],decoder2)
    if result:
        total2+=1

print(total1 * total2)