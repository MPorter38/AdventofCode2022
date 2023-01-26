
monkeys = {}
with open("Day21Example.txt","r") as file:
    for line in file:
        monkeys[line.split(":")[0]] = line.strip().split(": ")[1]

def resolve_value(value,dict):
    string = dict[value]
    if string.isdigit():
        return int(string)
    else:
        string = string.split(" ")
        value1 = resolve_value(string[0],dict)
        value2 = resolve_value(string[2],dict)
        return eval("".join([str(value1),string[1],str(value2)]))

print(f' Part 1 is {resolve_value("root",monkeys)}')

root_str = monkeys["root"].split(" ")
monkeys["root"] = f'{root_str[0]} - {root_str[2]}'
prev_error = abs(resolve_value("root",monkeys))
prev_ansatz = int(monkeys["humn"])
ansatz = 0 
monkeys["humn"] = str(ansatz)
rate = 0.1 
error = abs(resolve_value("root",monkeys))

while error > 0.1:
    try:
        grad = (ansatz - prev_ansatz) // (error - prev_error)
    except ZeroDivisionError:
        grad = 1 if error < prev_error else -1
    
    prev_ansatz = ansatz
    prev_error = error 

    ansatz -= rate * error * grad
    monkeys["humn"] = str(round(ansatz))
    error = abs(resolve_value("root",monkeys))

print(f'Part 2 {round(ansatz)}')

