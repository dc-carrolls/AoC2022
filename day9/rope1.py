class Knot:
  def __init__(self):
    self.x = 0
    self.y = 0
  #end constructor
#end class

class Head(Knot):
  def __init__(self,tail):
    super().__init__()
    self.x_dir = 0
    self.y_dir = 0
    self.move=None
    self.distance=None
    self.tail = tail
    self.tail_set = {(self.tail.x,self.tail.y)}
  #end constructor

  def set_move(self,move,distance):
    self.distance = distance
    self.move = move

  def move_tail(self):
    delta_x = abs(self.tail.x - self.x)
    delta_y = abs(self.tail.y - self.y)
    if delta_x > 1:
      self.tail.x += self.x_dir
      if delta_y > 0: 
        self.tail.y += self.y_dir
    if delta_y > 1: 
      self.tail.y += self.y_dir
      if delta_x > 0:
        self.tail.x += self.x_dir
    self.tail_set.add((self.tail.x,self.tail.y))

  def update(self):
    while self.distance > 0:
      if self.move == 'U': 
        self.y_dir = 1
        self.y += self.y_dir  
      elif self.move == 'D': 
        self.y_dir = -1
        self.y += self.y_dir   
      elif self.move == 'L': 
        self.x_dir = -1
        self.x += self.x_dir  
      elif self.move == 'R':
        self.x_dir = 1   
        self.x += self.x_dir 
      #end if
      self.distance += -1
      self.move_tail()
    #end while      
  #end method
#end class

def main():
  file1 = open('.\day9\input.txt', 'r')
  data = file1.readlines()
  my_tail = Knot()
  my_head = Head(my_tail)
  for row in data:
    move,dist = row.strip().split()
    my_head.set_move(move,int(dist))
    my_head.update()
  print('Tail length:',len(my_head.tail_set))
    
if __name__ == "__main__":
  main()