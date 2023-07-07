class Node:
  def __init__(self,name,tail) -> None:
    self.name = name
    self.tail = tail
  
  def print_tail(self):
    print(self.name)
    if self.tail != None:
      self.tail.print_tail()

#end class


tail2 = Node('tail2',None)
tail1 = Node('tail1',tail2)
head = Node('Head',tail1)

head.print_tail()
    

