# Author:    请喊我去编程
# Bilibili:  https://space.bilibili.com/73503664
# GitHub:    https://github.com/CallMeToProgram/Bad-Apple
# Mail:      2395795924@qq.com

# Created at 2019-06-17
# Updated at 2019-12-20

import pygame
import time
import curses
from pathlib import Path
import convert

# video and bgm path
VIDEO_PATH = "data/1.flv"
BGM_PATH = "data/bgm.mp3"

# frame rate of video
FRAME_RATE = 1 / 30


if Path("video_data.py").exists():
    from video_data import video_data
else:
    if not Path(VIDEO_PATH).exists():
        print("视频不存在: ", VIDEO_PATH)
    if not Path(BGM_PATH).exists():
        print("音乐不存在: ", BGM_PATH)
    video_data = convert.write(VIDEO_PATH)
    input("\n转换完成, 按任意键继续...")

count = 0

stdsrc = curses.initscr()
curses.start_color()
stdsrc.resize(30, 100)

pygame.mixer.init()
track = pygame.mixer.music.load(BGM_PATH)
pygame.mixer.music.play()
time.sleep(0.4)
now = time.time()

for frame_data in video_data:
    for i in range(len(frame_data)):
        stdsrc.addstr(i, 0, frame_data[i], curses.COLOR_WHITE)
    while time.time() - now < count * FRAME_RATE:
        time.sleep(count * FRAME_RATE - time.time() + now)
    stdsrc.refresh()
    count += 1

curses.endwin()
