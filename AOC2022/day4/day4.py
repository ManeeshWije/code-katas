def p1():
  data = open('input.txt', 'r')
  lines = data.read().strip().split('\n')
  count = 0
  for line in lines:
    interval = line.split(',')
    first = interval[0]
    second = interval[1]
    num = first.split('-')
    num2 = second.split('-')
    if ((int(num[0]) >= int(num2[0]) and int(num[1]) <= int(num2[1]))) or (int(num2[0]) >= int(num[0]) and int(num2[1]) <= int(num[1])):
      print(num[0], num[1], num2[0], num2[1])
      count += 1
  print(count)
p1()

def p2():
  data = open('input.txt', 'r')
  lines = data.read().strip().split('\n')
  count = 0
  for line in lines:
    interval = line.split(',')
    first = interval[0]
    second = interval[1]
    num = first.split('-')
    num2 = second.split('-')
    if int(num[0]) <= int(num2[1]) and int(num[1]) >= int(num2[0]):
      print(num[0], num[1], num2[0], num2[1])
      count += 1
  print(count)
p2()
