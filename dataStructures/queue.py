class myqueue:

  def __init__(self) -> None:
    self.data = []

  def length(self):
    return len(self.data)

  def enque(self, element):
    if len(self.data) < 5:
      return self.data.append(element)
    else:
      return "overflow"

  def deque(self):
    if len(self.data) == 0:
      return 'underflow'
    else:
      self.data.pop(0)

b = myqueue()
b.enque(2) # put the element into the queue
b.enque(3)
b.enque(4)
b.enque(5)
print(b.data)
b.deque()# # remove the first element that we have put in the queue
print(b.data)