index = 2
number = 600851475143
while index < number:
    if number % index == 0:
        number = number / index
    index += 1

print("The largest prime factor of the given number is",index)
