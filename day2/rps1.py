file1 = open('.\day2\input.txt', 'r')
Lines = file1.readlines()
map = {"A":1,"B":2,"C":3,"X":1,"Y":2,"Z":3}
result = [3,6,0]
total = 0
for line in Lines:
    p1, p2 = [map[x] for x in line.strip().split(" ")]
    total = total + p2 + result[(p2-p1) % 3]
print(total)