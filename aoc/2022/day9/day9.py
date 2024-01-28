def p1():
  data = open('input.txt', 'r').read().strip().split('\n')
  w = 30
  h = 30
  grid = [[0 for x in range(w)] for y in range(h)] 
  rows = len(grid)
  cols = len(grid[0])
  count = 1
  pos = 0
  for line in data:
    if line[0] == 'R':
      quantity = int(line[2])
      for i in range(rows):
        for j in range(cols):
      # print(line)
      # count += int(quantity) - 1
    # if line[0] == 'L':
    #   quantity = int(line[2])
    #   for i in range(quantity):
    #     grid[-1][i] = 1
    #   count += int(quantity) - 1
    # if line[0] == 'U':
    #   quantity = int(line[2])
    #   for i in range(quantity):
    #     grid[pos][i] = 1
      # count += int(quantity) - 1
    # if line[0] == 'D':
    #   quantity = line[2]
    #   count += int(quantity) - 1
  
  for i in range(rows):
    for j in range(cols):
       print(grid[i][j], end='')
    print("")
p1()

def p2():
  data = open('input.txt', 'r').read().strip().split('\n')
# p2()
