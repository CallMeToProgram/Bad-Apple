import cv2
from convert import convert
import pprint


vc = cv2.VideoCapture("data/1.flv")
f, frame = vc.read()
flv_data = []
while f:
    text = convert(frame)
    flv_data.append(text)
    f, frame = vc.read()

with open("flv_data.py", "w") as f:
    f.write("flv_data = " + pprint.pformat(flv_data))



