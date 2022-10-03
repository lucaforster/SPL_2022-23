import random

def addnumbers():
    num1 = int(input())
    num2 = int(input())
    sum = num1 + num2
    return sum


def randomnumber():
    number = random.randint(100, 200)
    return number

array = ["Liverpool", "ManU", "Arsenal"]
def word():
    return array[random.randint()]

print(addnumbers(10, 13))
print(randomnumber())
print(word())