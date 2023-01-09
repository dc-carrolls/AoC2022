class Tree:
  def __init__(self,height,row,col):
    self.height = height
    self.row = row
    self.col = col
    self.n=0
    self.s=0
    self.w=0
    self.e=0
  #end constructor

  def get_scenic_score(self):
    return self.n * self.s * self.w * self.e 
  #end function
#end class

def calc_scenic_score(woods,row,col):
  #check west
  tree=woods[row][col]
  x=col-1
  stop = False
  while x>-1 and not stop:
    if woods[row][x].height >= tree.height:
      stop = True
    tree.w+=1
    x-=1
  #end while
  #check east
  x=col+1
  stop = False
  while x<99 and not stop:
    if woods[row][x].height >= tree.height:
      stop = True
    tree.e+=1
    x+=1
  #end while
  # #check north
  y=row-1
  stop = False
  while y>-1 and not stop:
    if woods[y][col].height >= tree.height:
      stop = True
    tree.n+=1
    y-=1
  #end while
  #check south
  y=row+1
  stop = False
  while y<99 and not stop:
    if woods[y][col].height >= tree.height:
      stop = True
    tree.s+=1
    y+=1
  #end while


    
def main():
  file1 = open('.\day8\input.txt', 'r')
  data = file1.readlines()
  rows = len(data)
  cols = len(data[0].strip())
  woods=[]
  for row in range(rows):
    row_str = data[row].strip()
    tree_row =[]
    for col in range(cols):
      tree = Tree(int(data[row][col]),row,col)
      tree_row.append(tree)
    #next tree
    woods.append(tree_row)
  #next row
  max = 0
  for row in range(rows):
    for col in range(cols):
      calc_scenic_score(woods,row,col)
      score = woods[row][col].get_scenic_score()
      if score > max: max = score
    #next tree
  #next row
  print(max)

if __name__ == "__main__":
  main()