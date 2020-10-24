"""
Класс-клиент сикули

"""

from lackey import *
from lackey import Region
import pytesseract
class sikuliClient():
    def __init__(self, dir):
        self.dir = dir
        Settings.MinSimilarity = 0.9

    def type_to_screen(self, screen, text, dx=0, dy=0):
        # Pattern("1602541046838.png").targetOffset(-71, 226)
        self.screen = self.dir+screen
        self.wait_until_screen(screen)
        type(Pattern(self.screen).targetOffset(dx,dy), text)

    def wait_until_screen(self, screen, time_wait=30):
        self.wait_img = wait(self.dir+screen, time_wait)
        return self.wait_img

    def wait_vanish_screen(self, screen, time_wait=30):
        waitVanish(self.dir+screen, time_wait)

    def click_to_screen(self, screen, dx=0, dy=0):
        self.screen = self.dir + screen
        self.wait_until_screen(screen)
        click(Pattern(self.screen).targetOffset(dx, dy))

    def get_screen_offset(self, screen, x_off, y_off, w_off, h_off):
        self.match_image = self.wait_until_screen(screen)
        self.offset_reg = Region(
            int(self.match_image.getX())+x_off,
            int(self.match_image.getY())+y_off,
            w_off,
            h_off
        )
        # self.offset_reg.setH(h_off)
        # self.offset_reg.setW(w_off)
        # self.offset_reg.setX(int(self.match_image.getX())+x_off)
        # self.offset_reg.setY(int(self.match_image.getY())+y_off)

        self.offset_image = capture(self.offset_reg)
        return self.offset_image

    def recognize_text(self, image, lang='spa'):
        self.req_text = pytesseract.image_to_string(image, lang=lang)
        print(self.req_text)

        return self.req_text
