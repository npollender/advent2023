import re

with open('./in.txt', 'r') as file:
  puzzle = file.read()

#similar to day1, we collect individual values for number of cubes and color of cubes (w/ regex)
#we compare these values to our maxmimum values defined in 'bag', and skip iteration if it exceed the max
def p1(lines):

  result = 0
  bag = {'red' : 12, 'green' : 13, 'blue' : 14}
  regex = r'(\d+) (red|green|blue)'

  for game, line in enumerate(lines.split('\n'), start = 1):
    for num, rgb in re.findall(regex, line):
      if int(num) > bag[rgb]:
        break
    else:
      result += game

  return result

#like p1, collect nums and colors
#keep track of maximum value for each color ... more simple than p1 tbh
def p2(lines):

  result = 0
  regex = r'(\d+) (red|green|blue)'

  for line in lines.split('\n'):
    bag = {'red' : 0, 'green' : 0, 'blue' : 0}
    for num, rgb in re.findall(regex, line):
      if int(num) > bag[rgb]:
        bag[rgb] = int(num)
    result += bag['red'] * bag['green'] * bag['blue']

  return result

print('p1: ', p1(puzzle),
      '\np2: ', p2(puzzle))