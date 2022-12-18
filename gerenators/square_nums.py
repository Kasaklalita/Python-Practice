def square_numbers(nums):
  for i in nums:
    yield (i*i)

# list comprehension
# my_nums = (x*x for x in [1, 2, 3, 4, 5])

my_nums = square_numbers = square_numbers([1, 2, 3, 4, 5])
for num in my_nums:
  print(num)