def p1():
  data = open('input.txt', 'r').read().strip().split('\n')
  visibleCount = 0
  arr = []
  for i in range(len(data)):
    temparr = []
    for j in range(len(data[i])):
      temparr.append(int(data[i][j]))
    arr.append(temparr)
  cols = len(arr[0])
  rows = len(arr)

  def up(arr, row, col):
    for i in range(row - 1, -1, -1):
      if arr[i][col] >= arr[row][col]:
        return False
    return True
    
  def down(arr, row, col):
    for i in range(row + 1, cols):
      if arr[i][col] >= arr[row][col]:
        return False
    return True

  def left(arr, row, col):
    for i in range(col - 1, -1, -1):
      if arr[row][i] >= arr[row][col]:
        return False
    return True

  def right(arr, row, col):
    for i in range(col + 1, rows):
      if arr[row][i] >= arr[row][col]:
        return False
    return True

  for i in range(cols):
    for j in range(rows):
      if up(arr, i, j) or down(arr, i, j) or left(arr, i, j) or right(arr, i, j):
        visibleCount += 1
  print(visibleCount)
p1()

def p2():
  data = open('input.txt', 'r').read().strip().split('\n')
  arr = []
  for i in range(len(data)):
    temparr = []
    for j in range(len(data[i])):
      temparr.append(int(data[i][j]))
    arr.append(temparr)
  cols = len(arr[0])
  rows = len(arr)

  def up(arr, row, col):
    depthCanSee = 0
    for i in range(row - 1, -1, -1):
      depthCanSee += 1
      if arr[i][col] >= arr[row][col]:
        return depthCanSee
    return depthCanSee
    
  def down(arr, row, col):
    depthCanSee = 0
    for i in range(row + 1, cols):
      depthCanSee += 1
      if arr[i][col] >= arr[row][col]:
        return depthCanSee
    return depthCanSee

  def left(arr, row, col):
    depthCanSee = 0
    for i in range(col - 1, -1, -1):
      depthCanSee += 1
      if arr[row][i] >= arr[row][col]:
        return depthCanSee
    return depthCanSee

  def right(arr, row, col):
    depthCanSee = 0
    for i in range(col + 1, rows):
      depthCanSee += 1
      if arr[row][i] >= arr[row][col]:
        return depthCanSee
    return depthCanSee

  res = float('-inf')
  for i in range(cols):
    for j in range(rows):
      u = up(arr, i, j)
      d = down(arr, i, j)
      l = left(arr, i, j)
      r = right(arr, i, j)
      score = u * d * l * r
      res = max(res, score)
  print(res)
p2()
