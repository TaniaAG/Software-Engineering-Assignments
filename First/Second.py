sum = 0
first = 1
second = 1
aux = 0
while second < 4000000:
    aux = first
    first = second
    second = second + aux
    if second % 2 == 0:
        sum += second

print ("The sum is equal to", sum)
