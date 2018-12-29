from itertools import chain
with open("claims.txt") as f:
    ids = f.readlines()
ids = [x.strip('\n').split() for x in ids]
claims = []
size = 1000;
Matrix = [['~' for x in range(size)] for y in range(size)]


for line in ids:
    c = [x.strip(':') for x in line[2].split(',')]
    d = [x.strip('') for x in line[3].split('x')]
    claims.append(line[0])
    x = int(c[0])
    y = int(c[1])

    w = int(d[0])
    h = int(d[1])
    for i in range(0, w):
        for j in range(0, h):
            if Matrix[x+i][y+j] == "X" or Matrix[x+i][y+j] == "C":
                Matrix[x+i][y+j] = "C"
            else:
                Matrix[x+i][y+j] = "X"

unclaimed = 0
claimed = 0
for x in range(size):
    for y in range(size):
        if(Matrix[x][y] == "X"):
            unclaimed += 1
        elif(Matrix[x][y] == "C"):
            claimed += 1

# for line in Matrix:
#     print(line)

print('unclaimed sq inches', unclaimed)
print('claimed sq inches', claimed)

for line in ids:
    c = [x.strip(':') for x in line[2].split(',')]
    d = [x.strip('') for x in line[3].split('x')]
    x = int(c[0])
    y = int(c[1])

    w = int(d[0])
    h = int(d[1])
    conflict = False
    for i in range(0, w):
        for j in range(0, h):
            if Matrix[x+i][y+j] == "C":
                conflict = True
                break
            else:
                continue
    if not conflict:
        print('only id unclaimed', line[0])

f.close()