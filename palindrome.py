def is_palindrome(s: str) -> bool:
  if len(s) == 0:
    return True
  processed_string = ''
  for letter in s:
    processed_string = processed_string + letter if letter.isalpha() else processed_string
  processed_string = processed_string.lower()

  left, right = 0, len(processed_string) - 1
  while left < right:
    if processed_string[left] != processed_string[right]:
      return False
    left += 1
    right -= 1
  return True


def test_palindrome():
  assert is_palindrome('asdfdsa') == True
  assert is_palindrome('фывавфы') == False