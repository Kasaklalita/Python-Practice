def anagram(s: str, t: str) -> bool:
  if len(s) != len(t):
    return False
  
  letters = {}
  for letter in s:
    letters[letter] = letters.get(letter, 0) + 1
    
  for letter in t:
    if letter in letters:
      if letters[letter] == t.count(letter):
        pass
      else:
        return False
    else:
      return False

  return True


def test_anagram():
  assert anagram('ana', 'aan') == True
  assert anagram('ab', 'aa') == False
  assert anagram('asdf', 'asd') == False
  assert anagram('', '') == True
