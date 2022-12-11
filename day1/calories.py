file1 = open('.\day1\input.txt', 'r')
Lines = file1.readlines()

top3 = [0,0,0,0]
max = 0  
total = 0
# Strips the newline character
for line in Lines:
    if line.strip() == "":
        if total > max:
            max = total
        total = 0
    else:
        total = total + int(line.strip())
        top3[0]=total
        top3.sort()

print(top3[3]+top3[2]+top3[1])

mylist = [[0,1],[2,3]]

for list in mylist:
    for n in list:
        if n==2:
            
