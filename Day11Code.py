# input is information about a series of monekys and items. 
# There is starting items which are the items that each monkey starts with where the number represents worry level]
# Operation shows how the worry level changes after the monkey has inspected the item. 
# the test uses worry level to determine what to do with the tiem 
# also after the monkey inspects an item, the worry level decreases by a third (to nearest whole no.)
# the order of actions is that the first monkey inspects their first item, the operations happens,
# the test is applied and actioned. Then the same monkey does this for any other items it has 
# after that the next monkey does the same. when all monkeys have gone the round ends
# the output we want the total number of items that each monkey inspects over 20 rounds so we can give the product 
# of the two most active monkeys number of items inspected

import re

items = {}
ops = list()
test = list()
monkeys=8

with open("Day11Example.txt","r") as file: 
    for i in range(0,monkeys):
        k=0
        while True:
            a_line = file.readline().strip()
            if not a_line:
                break
            k+=1 
            if k == 2:
                items[i]= re.findall('(\d+)',a_line)
            elif k == 3:
                ops.append(a_line.split()[4:6])
            elif k == 4:
                test.append([a_line.split()[3]])
            elif k == 5:
                test[i].append(a_line.split()[5])
            elif k==6:
                test[i].append(a_line.split()[5])

# print(items)
# print(ops)
# print(test)
inspect_count = {}
for m in range(0,monkeys):
    inspect_count[m]=0 

def go_round(items_dt, ops_ls, test_ls,monkeys, divisor):
    for m in range(0,monkeys):
        n=0
        while len(items_dt[m]) > 0:
            #print(items_dt,m)
            worry_it = int(items_dt[m][n])
            if ops_ls[m][0] == "+":
                worry_it += int(ops_ls[m][1])
            else:
                if ops[m][1] == "old":
                    worry_it = worry_it ** 2
                else:
                    worry_it = worry_it * int(ops[m][1])
            inspect_count[m] +=1
            worry_it = worry_it // divisor
            if worry_it % int(test_ls[m][0]) ==0:
                items_dt[int(test_ls[m][1])].append(worry_it)
            else:
                items_dt[int(test_ls[m][2])].append(worry_it)
            items_dt[m].pop(n)
    return(inspect_count)

#for round in range(0,10000):
    output = go_round(items,ops,test,monkeys,1)
     
output = go_round(items,ops,test,monkeys,1)
print(output)

# print(244 * 230)

