def main():
  curr_dir = "/"
  dirs = {curr_dir:0} 
  file1 = open('.\day7\input.txt', 'r')
  Lines = file1.readlines()
  for line in Lines[2:]:
    line_parts = line.strip().split(chr(32))
    if line_parts[0] == 'dir':
      dirs[curr_dir+":"+line_parts[1]]=0    
    elif '0' <= line_parts[0][0] <= '9':
      path_list = curr_dir.split(":")
      for n in range(1,len(path_list)+1):
        dirs[":".join(path_list[0:n])] += int(line_parts[0])
    elif line_parts[0] == '$' and line_parts[1] == "cd":
      if line_parts[2] == '..':
        path_list = curr_dir.split(":")
        path_list.pop()
        curr_dir = ":".join(path_list)
      else:
        curr_dir = curr_dir+":"+line_parts[2]  
      #end if
    #end if
  #next line
  print(dirs['/'])
  FS_TOTAL = 70000000
  SPACE_REQ = 30000000
  dir_size = SPACE_REQ - (FS_TOTAL-dirs['/'])
  dir_list = []
  total = 0
  for dir in dirs:
    value = dirs[dir]
    if value <= 100000: total += value
    if value >= dir_size: dir_list.append(value)
  #next dir
  print(total)
  dir_list.sort()
  print(dir_list[0])

if __name__ == "__main__":
  main()
