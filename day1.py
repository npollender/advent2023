import re

with open('./in.txt', 'r') as file:
  puzzle = file.read()

#result is the sum of the first and last number of every string concatenated
def p1(lines):

  result = 0

  for line in lines.split('\n'):
    line = re.sub('\D', '', line)
    result += int(line[0] + line[-1])

  return result

#same as p1, but must also consider numbers written as words
#replace does not work here since we may encounter scenarios where numbers overlap - ie 'eighthree' or 'twone'
#instead, we collect each 'real' number and 'word' number (w/ regex), then follow the same logic as p1
def p2(lines):

  def to_digit(n):
    return n if n.isnumeric() else str(words.index(n))

  result = 0
  words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
  regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'

  for line in lines.split('\n'):
    num = re.findall(regex, line)
    result += int(to_digit(num[0]) + to_digit(num[-1]))

  return result

print('p1: ', p1(puzzle),
      '\np2: ', p2(puzzle))