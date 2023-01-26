
conversions = {
    "2" : 2,
    "1" : 1,
    "0" : 0,
    "-" :-1,
    "=":-2
}

def Convert(SNAFU:str):
    SNAFU=list(SNAFU)
    total = 0
    for i in range(0,len(SNAFU)):
        digit = conversions[SNAFU[i]]
        j = len(SNAFU) - i - 1
        decimal = digit *  (5 ** j)
        total += decimal
    return total 

converted = 0 

with open("Day25Example.txt","r") as file:
    for line in file:
        converted += Convert(line.strip()) 

print(converted)

encodings = {
    2 : "2",
    1 : "1",
    0 : "0",
    3 : ["1","="],
    4 : ["1","-"],
    5 : "0"
}

def Encode(Decimal:int):
    output = list()
    while True:
        output.insert(0,encodings[Decimal % 5])
        Decimal = Decimal // 5
        if Decimal == 0:
            break

    for i in range(len(output)-1,0,-1):
        if len(output[i])>1:
            element = output[i]
            output[i] = element[1]
            if len(output[i-1])==1:
                output[i-1] = encodings[int(output[i-1])+1]
                if output[i-1] in ["-","="]:
                    output[i-1] = list('1',output[i-1])
            else:
                
                if output[i-1][1]=="=":
                    output.pop(i-1)
                    output.insert(i-1,[1,"-"])
                else:
                    output.pop(i-1)
                    output.insert(i-1,[1,"0"])

    print(output)

Encode(converted)

