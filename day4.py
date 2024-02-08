import re
from collections import defaultdict

with open('./in.txt', 'r') as file:
  puzzle = file.read()

#identify matching values from winning numbers and your numbers
#if there is a match, += 1, any subsequent match is *= 2
def p1(lines):

  result = 0
  regex = r'(\d+)'

  for line in lines.split('\n'):
    card_value = 0
    line = line.split('|')
    winning_nums, your_nums = line[0].split(':')[1], line[1]
    for num in re.findall(regex, your_nums):
      if num in re.findall(regex, winning_nums):
        if card_value == 0:
          card_value += 1
        else:
          card_value *= 2
    result += card_value

  return result

#when there is a match, make a duplicate card of (current card + 1), incrementing the card for each additional match
#tally all cards (originals & duplicates)
def p2(lines):

  result = 0
  card_dict = defaultdict(int)
  regex = r'(\d+)'

  for card, line in enumerate(lines.split('\n'), start=1):
    matches = 0
    card_dict[card] += 1
    line = line.split('|')
    winning_nums, your_nums = line[0].split(':')[1], line[1]
    for num in re.findall(regex, your_nums):
      if num in re.findall(regex, winning_nums):
        matches += 1
    for match in range(matches):
      card_dict[card+match+1] += card_dict[card]
    result += card_dict[card]

  return result
    

print('p1: ', p1(puzzle),
      '\np2: ', p2(puzzle))