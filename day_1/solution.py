lines = open("input.txt").read().splitlines()

caloriesCounter = 0
sumList = []

for line in lines:
    if (line != ''):
        caloriesCounter += int(line)
    else:
        sumList.append(int(caloriesCounter))
        caloriesCounter = 0

sumList.append(int(caloriesCounter))

# result of part 1
print('Result of part 1:', max(sumList))

# result of part 2
sumList.sort(reverse=True)
print('Result of part 2:', sum(sumList[0:3]))