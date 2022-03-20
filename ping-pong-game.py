from pygame import*
from random import randint

win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))

back = (200, 255, 255)
window.fill(back)

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()