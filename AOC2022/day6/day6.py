"""
nppdvjthqldpwncqszvftbrmjlhg
- check every 4 letter consectutive sequence
- if dupe in sequence, check next 4 letter sequence
- else return the len of original string up to last index of 4 letter sequence
"""
def p1():
  lines = open('input.txt', 'r').readline().strip('\n')
  count = 0
  curr = ""
  found = False
  i = 0
  while i < len(lines) and not found:
    j = i
    count = 0
    while count < 4:
      curr += lines[j]
      if len(set(curr)) == len(curr) and len(curr) == 4:
        found = True
        break
      else:
        count += 1
      if len(curr) == 4:
        curr = ''
      j += 1
    i += 1
  print(lines.find(curr) + 4)
# p1()

def p2():
  lines = open('input.txt', 'r').readline().strip('\n')
  count = 0
  curr = ""
  found = False
  i = 0
  while i < len(lines) and not found:
    j = i
    count = 0
    while count < 14:
      curr += lines[j]
      if len(set(curr)) == len(curr) and len(curr) == 14:
        found = True
        break
      else:
        count += 1
      if len(curr) == 14:
        curr = ''
      j += 1
    i += 1
  print(lines.find(curr) + 14)
p2()
