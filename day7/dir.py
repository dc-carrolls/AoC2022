class Dir:
  def __init__(self,name,parent):
    self.parent = parent
    self.name = name
    self.child_dir = {}
    self.size = 0
  #end constructor
#end class

def traverse(root):
  if len(root.child_dir) == 0:
    return root.size
  else:
    for node in root.child_dir:
      root.size = root.size + traverse(root.child_dir[node]) 
    #next node
  #end if
  return root.size
#end function
  
def find_total(root,limit):
  if root.size <= limit:
    total = root.size
  else:
    total = 0
  #end if
  if len(root.child_dir) == 0:
    return total  
  else:
    for node in root.child_dir:
      total = total + find_total(root.child_dir[node],limit)
    #next node
  #end if
  return total  
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
  print(traverse(root))
  print(root.size)
  print(find_total(root,100000))

if __name__ == "__main__":
  main()


