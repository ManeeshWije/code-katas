data = open('input.txt', 'r')
lines = data.read().split('\n')
output = []

tempSum = 0
res = 0
for line in lines:
  if line == '':
    res = max(res, tempSum)
    output.append(tempSum)
    tempSum = 0
  else:
    tempSum += int(line)
output = sorted(output)
output = output[len(output) -3:]
print(sum(output))
