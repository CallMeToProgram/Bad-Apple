import matplotlib.pyplot as plt

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


if __name__ == '__main__':
    print(convert(plt.imread("miku.jpg")))
