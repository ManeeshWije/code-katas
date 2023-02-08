""" 
P1
1. [D N Z]  [C M]  [P]
2. [] [C M] [Z N D P]
3. [M C] [] [Z N D P]
4. [C] [M] [Z N D P]
return CMZ 

P2
Multiple crates keeps order
"""

stacks = [
  ['W', 'L', 'S'], ['Q', 'N', 'T', 'J'], ['J', 'F', 'H', 'C', 'S'], ['B', 'G', 'N', 'W', 'M', 'R', 'T'], 
  ['B', 'Q', 'H', 'D', 'S', 'L', 'R', 'T'], ['L', 'R', 'H', 'F', 'V', 'B', 'J', 'M'], ['M', 'J', 'N', 'R', 'W', 'D'],
  ['J', 'D', 'N', 'H', 'F', 'T', 'Z', 'B'], ['T', 'F', 'B', 'N', 'Q', 'L', 'H']
]
# stacks = [
#   ['N', 'Z'], ['D', 'C', 'M'], ['P']
# ]
def p1():
  output = ""
  moves = []
  tempList = []
  lines = open('input.txt', 'r').read().strip().split('\n')
  for line in lines:
    line = line.replace('move', '').replace('from', '').replace('to', '').strip()
    sublist = line.split(' ')
    tempList.append(sublist)

  for i in tempList:
      temp = list(filter(None, i))
      moves.append(temp)

  for move in moves:
    j = 0
    quantityMove = int(move[0])
    fromStack = int(move[1])
    toStack = int(move[2])
    while j < quantityMove:
      temp = stacks[fromStack - 1].pop(0)
      stacks[toStack - 1].insert(0, temp)
      j += 1
  for arr in stacks:
    output += arr[0]
  print(output)
# p1()

def p2():
  output = ""
  moves = []
  tempList = []
  lines = open('input.txt', 'r').read().strip().split('\n')
  for line in lines:
    line = line.replace('move', '').replace('from', '').replace('to', '').strip()
    sublist = line.split(' ')
    tempList.append(sublist)

  for i in tempList:
      temp = list(filter(None, i))
      moves.append(temp)

  for move in moves:
    j = 0
    tempArr = []
    quantityMove = int(move[0])
    fromStack = int(move[1])
    toStack = int(move[2])
    while j < quantityMove:
      temp = stacks[fromStack - 1].pop(0)
      if quantityMove == 1:
        stacks[toStack - 1].insert(0, temp)
      else:
        tempArr.append(temp)
      j += 1
    for i in reversed(tempArr):
      stacks[toStack - 1].insert(0, i)
  for arr in stacks:
    output += arr[0]
  print(output)
p2()
