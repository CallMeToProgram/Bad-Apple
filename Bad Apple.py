import pygame
import time
import curses
from flv_data import flv_data

count = 0
frame_rate = 0.0333667

stdsrc = curses.initscr()
curses.start_color()
stdsrc.resize(30, 100)

pygame.mixer.init()
track = pygame.mixer.music.load("data/bgm.mp3")
pygame.mixer.music.play()
time.sleep(0.4)
now = time.time()

for frame_data in flv_data:
    for i in range(len(frame_data)):
        stdsrc.addstr(i, 0, frame_data[i], curses.COLOR_WHITE)
    while time.time() - now < count * frame_rate:
        pass
    stdsrc.refresh()
    count += 1

curses.endwin()
