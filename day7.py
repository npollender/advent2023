from collections import Counter

with open('./in.txt', 'r') as file:
  puzzle = file.read()

def p1(lines):

  def hand_strength(hand):
    num_cards = sorted(Counter(hand).values(), reverse = True)
    if num_cards[0] == 5: #five of a kind
      return 6  
    elif num_cards[0] == 4: #four of a kind
      return 5
    elif num_cards[0] == 3 and num_cards[1] == 2: #full house
      return 4
    elif num_cards[0] == 3: #three of a kind
      return 3
    elif num_cards[0] == 2 and num_cards[1] == 2: #two pair
      return 2
    elif num_cards[0] == 2: #one pair
      return 1
    else: #high card
      return 0
  
  result = 0
  hands = []
  #ASCII notation - convert to alphabetical order based on card strength for easy sorting
  remap = {50: 97, 51: 98, 52: 99, 53: 100, 54: 101, 55: 102, 56: 103, 57: 104, 84: 105, 74: 106, 81: 107, 75: 108, 65: 109}

  for line in lines.split('\n'):
    hand = line.split(' ')[0].translate(remap)
    line = str(hand_strength(hand)) + ' ' + hand + ' ' + line.split(' ')[1]
    hands.append(line)

  hands.sort()

  for rank, hand in enumerate(hands, start = 1):
    result += int(hand.split(' ')[2]) * rank

  return result

def p2(lines):

  def hand_strength(hand):
    jokers = hand.count('a')
    hand = hand.replace('a', '')
    num_cards = sorted(Counter(hand).values(), reverse = True)
    if not num_cards or num_cards[0] + jokers == 5: #five of a kind
      return 6  
    elif num_cards[0] + jokers == 4: #four of a kind
      return 5
    elif num_cards[0] + jokers == 3 and num_cards[1] == 2: #full house
      return 4
    elif num_cards[0] + jokers == 3: #three of a kind
      return 3
    elif num_cards[0] == 2 and num_cards[1] == 2: #two pair
      return 2
    elif num_cards[0] + jokers == 2: #one pair
      return 1
    else: #high card
      return 0
    
  result = 0
  hands = []
  remap = {74: 97, 50: 98, 51: 99, 52: 100, 53: 101, 54: 102, 55: 103, 56: 104, 57: 105, 84: 106, 81: 107, 75: 108, 65: 109}

  for line in lines.split('\n'):
    hand = line.split(' ')[0].translate(remap)
    line = str(hand_strength(hand)) + ' ' + hand + ' ' + line.split(' ')[1]
    hands.append(line)

  hands.sort()

  for rank, hand in enumerate(hands, start = 1):
    result += int(hand.split(' ')[2]) * rank
    
  return result

print('p1: ', p1(puzzle),
      '\np2: ', p2(puzzle))