cycle = 0
sum = 0
value = 1
img = [] 
for i in range(6):
  img.append(['']* 40)
print(img)

def runCycle():
  global cycle
  global sum
  cycle += 1
  if cycle % 40 == 20:
    sum += cycle * value
  
def p1():
  data = open('input.txt', 'r').read().strip().split('\n')
  global value
  for line in data:
    section = line.split(' ')
    if section[0] == 'noop':
      runCycle()
    elif section[0] == 'addx':
      for _ in range(2):
        runCycle()
      value += int(section[1])
  print(sum)
p1()
