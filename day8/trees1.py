class Tree:
  def __init__(self,height):
    self.height = height
    self.n=True
    self.s=True
    self.w=True
    self.e=True
  #end constructor

  def get_visible(self):
    return self.n or self.s or self.w or self.e 
  #end function
#end class
    
def main():
  file1 = open('.\day8\input.txt', 'r')
  rows = file1.readlines()
  woods=[]
  for row in rows:
    row = row.strip()
    max=-1
    tree_row =[]
    for tree_height in row:
      tree = Tree(int(tree_height))
      tree_row.append(tree)
      if tree.height > max:
        max = tree.height
      else:
        tree.w=False
      #end if 
    #next tree
    woods.append(tree_row)
  #next row

  for row in woods:
    max = -1
    for tree in row[::-1]:
      if tree.height > max:
        max = tree.height
      else:
        tree.e=False
      #end if 
    #next tree
  #next row

  for col in range(len(woods[0])):
    max = -1
    for row in range(len(woods)):
      tree = woods[row][col]
      if tree.height > max:
        max = tree.height
      else:
        tree.n=False
      #end if 
    #next row
  #next col

  for col in range(len(woods[0])):
    max = -1
    for row in range(len(woods)-1,-1,-1):
      tree = woods[row][col]
      if tree.height > max:
        max = tree.height
      else:
        tree.s=False
      #end if 
    #next row
  #next col
  total = 0
  for row in woods:
    for tree in row:
      if tree.get_visible():
        total += 1
      #end if
    #next tree
  #next row
  print(total)

if __name__ == "__main__":
  main()