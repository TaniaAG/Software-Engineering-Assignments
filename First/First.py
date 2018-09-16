sum = 0
for index in range(0, 1000):
    if index % 3 == 0 or index % 5 == 0:
        sum += index

print("The sum of multiples of 3 and 5 in the range 0 to 1000 is equal to", sum)