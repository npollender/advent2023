import re

with open('./in.txt', 'r') as file:
  puzzle = file.read()

def p1(lines):
  
  result = 1
  regex = r'(\d+)'

  time = re.findall(regex, lines.split('\n')[0])
  dist = re.findall(regex, lines.split('\n')[1])

  for d in range(len(dist)):
    records = 0
    flag = False
    for t in range(1, int(time[d]) + 1):
      if ((int(dist[d]) / t) + t <= int(time[d]) and
          (int(time[d]) - t) * t >= int(dist[d])):
        flag = True
        records += 1
      #solution can only exist in an internal range so once we get a new invalid result we can break
      elif flag:
        break

    result *= records

  return result

def p2(lines):

  result = 0
  flag = False

  time = re.sub('\D', '', lines.split('\n')[0])
  dist = re.sub('\D', '', lines.split('\n')[1])
  
  #even though this is O(n), still takes a while on my slow ass laptop. It can surely be improved
  for t in range(1, int(time) + 1):
    if ((int(dist) / t) + t <= int(time) and
        (int(time) - t) * t >= int(dist)):
      flag = True
      result += 1
    elif flag:
      break

  return result

print('p1: ', p1(puzzle),
      '\np2: ', p2(puzzle))