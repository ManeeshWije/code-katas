def p1():
  lines = open('input.txt', 'r').read().strip().split('\n')
  sum = 0
  for i, line in enumerate(lines):
    section = lines[i].split(' ')
    if section[1].startswith('cd') and not section[2].startswith('..'):
      k = 1
      j = i + 1
      curr = 0
      while j < len(lines):
        next = lines[j].split(' ')
        if next[1] == 'cd':
          if next[2] == '..':
            k -= 1
          else:
            k += 1
          if k == 0:
            break
        if next[0].isdigit():
          curr += int(next[0])
        j += 1
      if curr <= 100000:
        sum += curr
  print(sum)
# p1()

def p2():
  lines = open('input.txt', 'r').read().strip().split('\n')
  sum = 0
  dirSizes = []
  for i, line in enumerate(lines):
    section = lines[i].split(' ')
    if section[1].startswith('cd') and not section[2].startswith('..'):
      k = 1
      j = i + 1
      curr = 0
      while j < len(lines):
        next = lines[j].split(' ')
        if next[1] == 'cd':
          if next[2] == '..':
            k -= 1
          else:
            k += 1
          if k == 0:
            break
        if next[0].isdigit():
          curr += int(next[0])
        j += 1
      dirSizes.append(curr)
  dirSizes.sort()
  totalSize = dirSizes[-1]
  unusedSize = 70000000 - totalSize
  required = 30000000 - unusedSize
  res = float('inf')
  for size in dirSizes:
    if size >= required:
      res = min(res, size)
  print(res)
p2()
