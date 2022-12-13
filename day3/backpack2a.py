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
line = 0
while line < len(Lines):
  bp1 = Lines[line].strip()
  bp2 = Lines[line+1].strip()
  bp3 = Lines[line+2].strip()
  line += 3
  m = next(c for c in bp1 if c in bp2 and c in bp3 )
  total = total + priority(m)
print(total)


