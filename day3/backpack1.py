def priority(c):
  a = ord(c)
  if 64 < a < 91:
    return a - 38
  elif 96 < a < 123:
    return a - 96
  else:
    return -1

file1 = open('.\day3\input.txt', 'r')
Lines = file1.readlines()
total = 0
for line in Lines:
    mid = len(line)//2
    c1 = line.strip()[:mid]
    c2 = line.strip()[mid:]
    m = next(c for c in c1 if c in c2)
    total = total + priority(m)
print(total)


