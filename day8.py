import re
import time

with open('./in.txt', 'r') as file:
  puzzle = file.read()

def p1(lines):

  result = 0
  regex = r'[a-zA-Z]+'

  instructions = lines.split('\n\n')[0]
  coords = re.findall(regex, lines.split('\n\n')[1])
  node = 'AAA'
  for c in range(0, len(coords), 3):
    if coords[c] == node:
      l = coords[c+1]
      r = coords[c+2]
      break

  while node != 'ZZZ':
    for i in instructions:
      for c in range(0, len(coords), 3):
        if (coords[c] == l and i == 'L') or (coords[c] == r and i == 'R'):
          node = coords[c]
          l = coords[c+1]
          r = coords[c+2]
          break
      result += 1
      if node == 'ZZZ':
        break
    
  return result

def p2(lines):

  def end_in_z(nodes):
    for n in nodes:
      if not n.endswith('Z'):
        return False
    return True  
  
  result = 0
  regex = r'[a-zA-Z]+'

  instructions = lines.split('\n\n')[0]
  coords = re.findall(regex, lines.split('\n\n')[1])
  nodes, lefts, rights = [], [], []
  for c in range(0, len(coords), 3):
    if coords[c].endswith('A'):
      nodes.append(coords[c])
      lefts.append(coords[c+1])
      rights.append(coords[c+2])

  while not end_in_z(nodes):
    for i in instructions:
      for n in range(0, len(nodes)):
        for c in range(0, len(coords), 3):
          if (coords[c] == lefts[n] and i == 'L') or (coords[c] == rights[n] and i == 'R'):
            nodes[n] = coords[c]
            lefts[n] = coords[c+1]
            rights[n] = coords[c+2]
            break
      result += 1   
      if end_in_z(nodes):
        break

  return result

tic = time.perf_counter()
print('p1: ', p1(puzzle),
      '\np2: ', p2(puzzle))
toc = time.perf_counter()
print('\nthat took ', (toc - tic) / 60, ' minutes') #ouchie