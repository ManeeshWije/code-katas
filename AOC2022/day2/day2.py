data = open('input.txt', 'r')
lines = data.read().strip().split('\n')
res = 0
for line in lines:
  move = line.split(" ")
  score = 0
  if move[1] == 'X': # need to lose
    if move[0] == 'A':
      score += 3
      score += 0
    elif move[0] == 'B':
      score += 1
      score += 0
    elif move[0] == 'C':
      score += 2
      score += 0
      
  elif move[1] == 'Y': # need to draw
    if move[0] == 'A':
      score += 1
      score += 3
    elif move[0] == 'B':
      score += 2
      score += 3
    elif move[0] == 'C':
      score += 3
      score += 3

  elif move[1] == 'Z': # need to win
    if move[0] == 'A':
      score += 2
      score += 6
    elif move[0] == 'B':
      score += 3
      score += 6
    elif move[0] == 'C':
      score += 1
      score += 6
  res += score
print(res)
