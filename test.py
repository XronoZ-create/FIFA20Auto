from SimulateJoy.device import DS4Device
from sikulilibrary.sikulilib import sikuliClient
import os
from PIL import Image, ImageOps, ImageFilter, ImageEnhance, ImageDraw
import numpy as np
import time
import copy



dir = os.path.dirname(os.path.realpath(__file__))
sikuli_client = sikuliClient(dir=dir)

test_dir = "/sikuli_screenshot/test/"

# data = copy.copy(sikuli_client.get_screen_offset(screen=test_dir + "keepitems.png", x_off=190, y_off=130, w_off=60, h_off=30))
img = Image.open('1.png').convert('RGB')
img = ImageOps.invert(img).filter(ImageFilter.MedianFilter)

t = sikuli_client.recognize_text(img, lang='eng')

print(t.split("\n"))

img.show()

