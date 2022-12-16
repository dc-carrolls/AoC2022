class Dir:
  def __init__(self,name,parent):
    self.parent = parent
    self.name = name
    self.child_dir = {}
    self.size = 0
  #end constructor
#end class

def traverse(root,dir_list):
  dir_list.append(root)
  if len(root.child_dir) == 0:
    return root.size
  else:
    for node in root.child_dir:
      root.size = root.size + traverse(root.child_dir[node],dir_list) 
    #next node
  #end if
  return root.size
#end function

def main():
  root = Dir("/",None)
  curr_dir = root
  file1 = open('.\day7\input.txt', 'r')
  Lines = file1.readlines()
  for line in Lines[2:]:
    line_parts = line.strip().split(chr(32))
    if line_parts[0] == 'dir':
      curr_dir.child_dir[line_parts[1]]=Dir(line_parts[1],curr_dir)
    elif '0' <= line_parts[0][0] <= '9':
      curr_dir.size = curr_dir.size + int(line_parts[0])
    elif line_parts[0] == '$' and line_parts[1] == "cd":
      if line_parts[2] == '..':
        curr_dir = curr_dir.parent
      else:
        curr_dir = curr_dir.child_dir[line_parts[2]]
      #end if
    #end if
  #next line
  dir_list=[]
  print(traverse(root,dir_list))
  dir_list.sort(key = lambda x: x.size, reverse=True)
  FS_TOTAL = 70000000
  SPACE_REQ = 30000000
  dir_size = SPACE_REQ - (FS_TOTAL-root.size)
  i=0
  while i < len(dir_list):
    node = dir_list[i]
    if node.size > dir_size:
      print(node.name,node.size)
    #end if
    i+=1
  #end while
#end main

  

if __name__ == "__main__":
  main()
#end if


