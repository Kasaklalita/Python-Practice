class Node:
  def __init__(self, letter) -> None:
    self.childleft = None
    self.childright = None
    self.nodedata = letter

def in_order(root):
  if root:
    in_order(root.childleft)
    print(root.nodedata)
    in_order(root.childright)

# create the nodes for the tree
root = Node('A')
root.childleft = Node('B')
root.childright = Node('C')
root.childleft.childleft = Node('D')
root.childleft.childright = Node('E')

in_order(root)