monkeys = {}

with open("Day23Input.txt","r") as file:
    for i,line in enumerate(file):
        for j,item in enumerate(line):
            if item == "#":
                monkeys[i,j] = [(i,j)]

def move_monkeys(location_dict : dict, rule_order : str):
    proposed_moves = {}
    for i,j in location_dict:
        proposed_moves[i,j] = [(i,j)]
        surroundings = {}
        for direction in ["N","NE","E","SE","S","SW","W","NW"]:
            up = i + (1 if "S" in direction else -1 if "N" in direction else 0)
            across = j + (1 if "E" in direction else -1 if "W" in direction else 0)
            surroundings[direction] = location_dict.get((up,across), False), (up,across)
        if any([surroundings[k][0] for k in surroundings]):
            for direction in rule_order:
                if not any([surroundings[k][0] for k in surroundings if direction in k]):
                    proposed_moves[surroundings[direction][1]] = proposed_moves.get(surroundings[direction][1],[]) + [(i,j)]
                    del proposed_moves[(i,j)]
                    break 
    
    for k,v in [(a,b) for (a,b) in proposed_moves.items()]:
        if len(v) > 1:
            for i in v:
                proposed_moves[i] = [i]
            del proposed_moves[k]
    return proposed_moves

locations = monkeys.copy()
rule_order = "NSWE"
for i in range(10):
    locations = move_monkeys(locations,rule_order)
    rule_order = rule_order[1:] + rule_order[0]
    
h = max([k[0] for k in locations]) - min([k[0] for k in locations]) + 1
w = max([k[1] for k in locations]) - min([k[1] for k in locations]) + 1

ans = h * w -len(locations)
print(f'Part 1 answer is {ans}')

k=0
rule_order = "NSWE"
locations = monkeys.copy()
while True:
    if move_monkeys(locations,rule_order) == locations:
        break 
    else:
        locations = move_monkeys(locations,rule_order)
        rule_order = rule_order[1:] + rule_order[0]
        k+=1

print(f'Part 2 answer is {k}')