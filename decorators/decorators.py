# def outer_function(msg):
#   def inner_function():
#     print(msg)
#   return inner_function

def decorator_function(original_function):
  def wrapper_function():
    print('wrapper executed this before {}'.format(original_function.__name__))
    original_function()
  return wrapper_function

@decorator_function
def display():
  print('display function ran')

display()