class Knot:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.x_dir = 0
    self.y_dir = 0
    self.tail_set = {(self.x,self.y)}
  #end constructor
#end class

class Tail(Knot):
  def __init__(self):
    super().__init__()
    self.tail_set = {(self.x,self.y)}
  #end constructor

  def move_tail(self):
    self.tail_set.add((self.x,self.y))



class Head(Knot):
  def __init__(self,tail):
    super().__init__()
    self.move=None
    self.distance=None
    self.tail = tail
  #end constructor

  def set_move(self,move,distance):
    self.distance = distance
    self.move = move

  def move_tail(self):
    delta_x = abs(self.tail.x - self.x)
    delta_y = abs(self.tail.y - self.y)
    if delta_x > 1:
      self.tail.x_dir = self.x_dir
      self.tail.x += self.x_dir
      if delta_y > 0: 
        self.tail.y_dir = self.y_dir
        self.tail.y += self.y_dir
    if delta_y > 1: 
      self.tail.y_dir = self.y_dir
      self.tail.y += self.y_dir
      if delta_x > 0:
        self.tail.x_dir = self.x_dir
        self.tail.x += self.x_dir
   #self.tail_set.add((self.tail.x,self.tail.y))
    # if type(self.tail) is Head:
    #   print('Tail',self.tail.x,self.tail.y)
    self.tail.move_tail()
    print('Tail',self.tail.x,self.tail.y)

    # else:
      
    #   self.tail.tail_set.add((self.tail.x,self.tail.y))


      
    

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
  file1 = open('.\day9\input2.txt', 'r')
  data = file1.readlines()
  my_tail9 = Tail()
  my_tail8 = Head(my_tail9)
  my_tail7 = Head(my_tail8)
  my_tail6 = Head(my_tail7)
  my_tail5 = Head(my_tail6)
  my_tail4 = Head(my_tail5)
  my_tail3 = Head(my_tail4)
  my_tail2 = Head(my_tail3)
  my_tail1 = Head(my_tail2)
  my_head = Head(my_tail1)
  for row in data:
    move,dist = row.strip().split()
    my_head.set_move(move,int(dist))
    my_head.update()
  print('Tail length:',len(my_tail9.tail_set))
    
if __name__ == "__main__":
  main()