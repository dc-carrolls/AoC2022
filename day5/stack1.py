def move(stacks,num,frm,to):
  for n in range(num):
    stacks[to-1].append(stacks[frm-1].pop())


def main():
  file1 = open('.\day5\input.txt', 'r')
  Lines = file1.readlines()
  stacks = [[] for _ in range(9)]
  for line in Lines[7::-1]:
    row = [x for x in line[1:35:4]]
    i=0
    while i < 9:
      if 'A' <= row[i] <= 'Z': 
        stacks[i].append(row[i])
      i+=1
  for line in Lines[10:]:
    num,frm,to =[int(x) for x in line.strip().split(chr(32))[1::2]]
    move(stacks,num,frm,to)
  result = ""
  for stack in stacks:
    result = result + stack.pop()
  print(result)


if __name__ == "__main__":
  main()


