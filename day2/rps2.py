file1 = open('.\day2\input.txt', 'r')
Lines = file1.readlines()
map = {"A":1,"B":2,"C":3,"X":2,"Y":1,"Z":3}
res_map = [3,0,6]
total = 0
for line in Lines:
    p1, res = [map[x] for x in line.strip().split(" ")]
    total = total + res_map[res-1] + ((p1 - res) % 3) + 1
print(total)