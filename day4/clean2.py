def main():
  file1 = open('.\day4\input.txt', 'r')
  Lines = file1.readlines()
  total = 0
  for line in Lines:
    id1,id2 = [x for x in line.strip().split(',')]
    l1,u1 = [int(x) for x in id1.split('-')]
    l2,u2 = [int(x) for x in id2.split('-')]
    if u1 >=l2 and l1<=u2:
      total += 1
  print(total)

if __name__ == "__main__":
  main()


