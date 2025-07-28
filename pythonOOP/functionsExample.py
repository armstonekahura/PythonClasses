import random

from sty import fg

def randomRGBColour():
    red = random.randint(0, 256)
    green = random.randint(0, 256)
    blue = random.randint(0, 256)

    return red, green, blue


def generateColour(red, green, blue):
    return fg(red, green, blue)


red, green, blue = randomRGBColour()
colour = generateColour(red, green, blue)

print(colour, "I randomly change my colour")

