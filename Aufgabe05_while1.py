import random

sum = 0
number = 0

while True:
    number = random.randint(10, 30)
    if number == 15 or number == 25:
           break
    sum += number
print("Sumem = {sum}")
print("Nummer = {number}")