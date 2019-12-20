# Author:    请喊我去编程
# Bilibili:  https://space.bilibili.com/73503664
# GitHub:    https://github.com/CallMeToProgram/Bad-Apple
# Mail:      2395795924@qq.com

# Created at 2019-06-17
# Updated at 2019-12-20

import matplotlib.pyplot as plt
import cv2
import pprint

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
char_len = len(ascii_char)
show_heigth = 30
show_width = 90


def convert(pic):
    pic_heigth, pic_width, _ = pic.shape
    gray = 0.2126 * pic[:, :, 2] + 0.7152 * pic[:, :, 1] + 0.0722 * pic[:, :, 0]
    res = []
    for i in range(show_heigth):
        y = int(i * pic_heigth / show_heigth)
        text = ""
        for j in range(show_width):
            x = int(j * pic_width / show_width)
            text += ascii_char[int(gray[y][x] / 256 * char_len)]
        res.append(text)
    return res


def write(VIDEO_PATH):
    print("转换视频中...")
    vc = cv2.VideoCapture(VIDEO_PATH)
    count = 0
    f, frame = vc.read()
    video_data = []
    while f:
        count += 1
        print("\r转换进度: %d" % count, end='')
        text = convert(frame)
        video_data.append(text)
        f, frame = vc.read()

    with open("video_data.py", "w") as f:
        f.write("video_data = " + pprint.pformat(video_data))

    return video_data


if __name__ == '__main__':
    print(convert(plt.imread("1.jpg")))
