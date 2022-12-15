def main():
  file1 = open('.\day5\input.txt', 'r')
  Lines = file1.readlines()
  total = 0
  stacks = [[] for _ in range(9)]
  for line in Lines[7::-1]:
    row = [x for x in line[1:35:4]]
    i=0
    while i < 9:
      if 'A' <= row[i] <= 'Z': 
        stacks[i].append(row[i])
      i+=1
  print(stacks)

if __name__ == "__main__":
  main()


