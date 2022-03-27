import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"

for i in range(7000):
    first = "".join((random.choice(chars) for i in range(24)))
    second = "".join((random.choice(chars) for i in range(6)))
    third = "".join((random.choice(chars) for i in range(27)))

    result = first + "." + second + "." + third

    output = open("OutputTokens.txt", "a")
    output.write(result + "\n \n")
    print('TOKENS GENERATED')