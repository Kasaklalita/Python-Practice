# def outer_function(msg):
#   def inner_function():
#     print(msg)
#   return inner_function

def decorator_function(original_function):
  def wrapper_function(*args, **kwargs):
    print('wrapper executed this before {}'.format(original_function.__name__))
    original_function(*args, **kwargs)
  return wrapper_function

class decorator_class(object):
  def __init__(self, original_function):
    self.original_function = original_function
  
  def __call__(self, *args, **kwargs):
    print('call method executed this before {}'.format(self.original_function.__name__))
    self.original_function(*args, **kwargs)

@decorator_class
def display():
  print('display function ran')

@decorator_class
def display_info(name, age):
  print('display_info ran with arguments ({} {})'.format(name, age))

display()
display_info('John', 25)