import matplotlib.pyplot as plt
from PIL import Image
import re

def findStartAxis(x, y):
    return (x//65*65, y//65*65)

def findIndexByStartAxis(x,y):
    with open("./content.py", "r") as f:
        for line in f.readlines():
            #container.sprites.Add(Sprite("262f", set_emojis, 2665, 1300, 64, 64))
            pattern = r'"(\w+?)", set_emojis, {}, {},'.format(int(x), int(y))
            m = re.search(pattern, line)
            if m:
                return m.groups()[0]

def findCodeByIndex(index):
    with open("./index.txt", "r") as f:
        count = 0
        target = float('inf')
        for line in f.readlines():
            count += 1
            if line.startswith(index):
                target = count+2
            if count == target:
                return line

def mainLoop():
    plt.figure()
    fig = plt.gcf()
    fig.set_size_inches(60,60)
    im = Image.open("./emojione.sprites.png")
    while True:
        plt.imshow(im)
        pos = plt.ginput(1)
        startaxis = findStartAxis(*pos[0])
        emojiIndex = findIndexByStartAxis(*startaxis)
        emojiCode = findCodeByIndex(emojiIndex)
        #print(pos, startaxis, emojiIndex, emojiCode)
        print(emojiCode)

if __name__ == '__main__':
    mainLoop()
