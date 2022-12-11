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
counter = 0
for bp in Lines:
  if counter % 3 == 0: 
    bp1 = bp.strip()
    counter += 1
  elif counter % 3 == 1: 
    bp2 = bp.strip()
    counter += 1
  else:
    counter = 0
    bp3 = bp.strip()
    m = next(c for c in bp1 if c in bp2 and c in bp3 )
    total = total + priority(m)
print(total)


