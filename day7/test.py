def main():
  file1 = open('.\day7\input.txt', 'r')
  Lines = file1.readlines()
  total = 0
  for line in Lines[2:]:
    line_parts = line.strip().split(chr(32))
    if '0' <= line_parts[0][0] <= '9':
      total = total + int(line_parts[0])
  print(total)




if __name__ == "__main__":
  main()
