def priority(c):
  a = ord(c)
  if 64 < a < 91: return a - 38
  if 96 < a < 123: return a - 96
  return -1

def main():
  file1 = open('.\day3\input.txt', 'r')
  Lines = file1.readlines()
  total = 0
  l = 0
  while l < len(Lines):
    m = next(c for c in Lines[l] if c in Lines[l+1] and c in Lines[l+2] )
    total = total + priority(m)
    l += 3
  print(total)
  file1.close()

if __name__ == "__main__":
  main()



