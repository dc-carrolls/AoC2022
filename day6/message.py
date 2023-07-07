def main():
  file = open('.\day6\input.txt', 'r')
  line = file.readline()
  c = 14
  marker = line[c-14:c]
  while c < len(line) and (len(set(marker)) != len(marker)):
    c+=1
    marker = line[c-14:c]
  print(c)

if __name__ == "__main__":
  main()


