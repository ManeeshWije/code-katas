data = open('input.txt', 'r')
lines = data.read().strip().split('\n')
output = []
arr = []
step = 3
i = 0
for line in lines:
  arr.append(line)
  i += 1
  if i >= 3:
    for c in line:
      if c in arr[0] and c in arr[1]:
        output.append(c)
        break
    i = 0
    arr = []
sum = 0
print(output)
for c in output:
  if c.isupper():
    sum += ord(c) - 38
  else:
    sum += ord(c) - 96
print(sum)
