with open('./in.txt', 'r') as file:
  puzzle = file.read()

#identify any number adjacent (+diagonal) to a special character (not '.')
#concatenate the corresponding numbers that are horizontally adjacent, then add to the result
def p1(lines):
#check left, right, up, down, and diagonals
  def check_adj(lines, row, col):
    return True if (col > 0                                          and lines[row][col-1]   in symbols or
                    col < len(lines[row])-1                          and lines[row][col+1]   in symbols or
                    row > 0                                          and lines[row-1][col]   in symbols or
                    row < len(lines)-1                               and lines[row+1][col]   in symbols or
                    (row > 0 and col > 0)                            and lines[row-1][col-1] in symbols or
                    (row > 0 and col < len(lines[row])-1)            and lines[row-1][col+1] in symbols or
                    (row < len(lines)-1 and col > 0)                 and lines[row+1][col-1] in symbols or
                    (row < len(lines)-1 and col < len(lines[row])-1) and lines[row+1][col+1] in symbols) else False
  
  def build_num(line, left, right, val):
    while left >= 0:
      if line[left].isnumeric():
        val = line[left] + val
        left -= 1
      else:
        break
    while right < len(line):
      if line[right].isnumeric():
        val = val + line[right]
        right += 1
      else:
        break
    return val, right

  result = 0
  symbols = '!@#$%^&*()-+?_=,<>/'

  lines = lines.split('\n')

  for row, line in enumerate(lines, start = 0):
    col = 0
    while col < len(line):
      val = line[col]
      if val.isnumeric() and check_adj(lines, row, col):
        val, col = build_num(line, col-1, col+1, val)
        result += int(val)
      else:
        col += 1

  return result

#identify * symbol... if it is adjacent to EXACTLY two numbers, multiply numbers and add to result
#quite literally the most impracticle solution I could of thought of to be honest
def p2(lines):
  #based on input, we know a gear doesn't appear on the min/max indecies. No need to add this to clauses
  def check_gear(lines, row, col):
    result, adj = 1, 0
    if lines[row][col-1].isnumeric() and adj < 2:
      tmp, val = col-1, ''
      adj += 1
      while tmp >= 0 and lines[row][tmp].isnumeric() and adj <= 2:
        val = lines[row][tmp] + val
        tmp -= 1
      result *= int(val) if adj <= 2 else 0
    if lines[row][col+1].isnumeric() and adj < 2:
      tmp, val = col+1, ''
      adj += 1
      while tmp < len(lines[row]) and lines[row][tmp].isnumeric() and adj <= 2:
        val = val + lines[row][tmp]
        tmp += 1
      result *= int(val) if adj <= 2 else 0
    result, adj = check_corners(lines, row, col, adj, result, -1) if adj <= 2 else 0
    result, adj = check_corners(lines, row, col, adj, result, 1) if adj <= 2 else 0

    return result if adj == 2 else 0
  #lr = -1 check up, lr = 1 check down
  def check_corners(lines, row, col, adj, result, lr):
    corner_flag = False
    if lines[row+lr][col].isnumeric() and adj < 2:
      tmp_l, tmp_r, val = col, col, lines[row+lr][col]
      adj += 1
      if (tmp_l >= 0 or tmp_r < len(lines[row])) and adj <= 2:
        while lines[row+lr][tmp_l-1].isnumeric():
          val = lines[row+lr][tmp_l-1] + val
          tmp_l -= 1
        while lines[row+lr][tmp_r+1].isnumeric():
          val = val + lines[row+lr][tmp_r+1]
          tmp_r += 1
      result *= int(val) if adj <= 2 else 0
    else:
      corner_flag = True
    if lines[row+lr][col-1].isnumeric() and adj < 2 and corner_flag:
      tmp, val = col-1, ''
      adj += 1
      while tmp >= 0 and lines[row+lr][tmp].isnumeric() and adj <= 2:
        val = lines[row+lr][tmp] + val
        tmp -= 1
      result *= int(val) if adj <= 2 else 0
    if lines[row+lr][col+1].isnumeric() and adj < 2 and corner_flag:
      tmp, val = col+1, ''
      adj += 1
      while tmp < len(lines[row]) and lines[row+lr][tmp].isnumeric() and adj <= 2:
        val = val + lines[row+lr][tmp]
        tmp += 1
      result *= int(val) if adj <= 2 else 0
    return result if adj <= 2 else 0, adj

  result = 0
  lines = lines.split('\n')

  for row, line in enumerate(lines, start = 0):
    col = 0
    while col < len(line):
      val = line[col]
      if val == '*':
        result += check_gear(lines, row, col)
      col += 1

  return result

print('p1 :', p1(puzzle),
      '\np2 :', p2(puzzle))