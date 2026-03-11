tomb =  []

sor = 4
oszlop = 3
num = 1

for i in range(sor):
    sor_tomb = []
    for j in range(oszlop):
        sor_tomb.append(num)
        num += 1
    tomb.append(sor_tomb)
print(tomb)