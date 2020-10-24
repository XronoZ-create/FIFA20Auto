"""
Главный класс, который наследуют все другие челленджи
"""

from sikulilibrary.sikulilib import sikuliClient
import time
from SimulateJoy.device import DS4Device
from fifa.exceptions import ERROR_CONNECT_PS4
from fifa.find_exceptions import find_error_connect
import os
from fifa.tepmplate_keyboard import template_keyboard
from fifa.players import players
from PIL import Image, ImageOps, ImageFilter, ImageDraw
from fifa.parsing_info_players import parse_info
from fifa.set_players import set_players_1523, set_players_1343, set_players_1433, set_players_1442,\
    set_players_13412, set_players_14141_hybrid_leagues_L_U, set_players_14141_hybrid_leagues_R_D,\
    set_players_14222, set_players_14222_leagues_and_nations_L_D

class FifaClass():
    def __init__(self, dir):
        self.joy_client = DS4Device('Windows', 'localhost')
        self.dir = dir
        self.sikuli_client = sikuliClient(dir=self.dir)

    def run_ps4remote(self):
        """
        Функция для запуска ярлыка в папке. И ожидание окончания запуска.

        :return: ничего
        """

        self.ps4remote_dir = self.dir+"/Дистанционное воспроизведение PS.lnk"
        os.startfile (self.ps4remote_dir)
        self.run_dir = "/sikuli_screenshot/auth/"

        self.sikuli_client.click_to_screen(screen=self.run_dir + "zapusk.png")
        self.sikuli_client.wait_vanish_screen(screen=self.run_dir + "big_computer.png", time_wait=260)

    def run_fifa(self):
        """
        Запуск фифы

        :return: ничего
        """

        self.joy_client.press(key='main-button')
        self.joy_client.press(key='a-button')# X

    def skip_start(self):
        """
        Выбор языка и скип всех всплывающих менющек

        :return: ничего
        """

        self.runfifa_dir = "/sikuli_screenshot/runfifa/"
        self.sikuli_client.wait_until_screen(screen=self.runfifa_dir + "russia.png", time_wait=260)
        self.joy_client.press_ncount(key='left-button', count=2)
        self.joy_client.press(key='a-button')  # X
        self.sikuli_client.wait_until_screen(screen=self.runfifa_dir + "fifa21logo.png", time_wait=260)
        self.joy_client.press(key='a-button')  # X
        self.sikuli_client.wait_until_screen(screen=self.runfifa_dir + "fifamenulogo.png", time_wait=260)
        self.joy_client.press(key='a-button')  # X

        print('FIFA2020 была успешно запущена')

    def skip_news(self):
        """
        Запуск Ultimate и скип всех всплювающих менюшек

        :return: ничего
        """

        self.joy_client.press(key='a-button')  # X
        self.runultimate_dir = "/sikuli_screenshot/runultimate/"
        while True:
            try:
                self.sikuli_client.wait_until_screen(screen=self.runultimate_dir + "store.png", time_wait=5)
                break
            except:
                self.joy_client.press(key='a-button')  # X

    def select_challenges_found(self):
        """
        Переход в меню челленджей

        :return: ничего
        """

        self.select_dir = '/sikuli_screenshot/selectchallengefound/'
        self.joy_client.right_on_stick_ncount(count=2)
        self.joy_client.press(key='a-button', timeout=0.5)
        self.sikuli_client.wait_until_screen(screen=self.select_dir + "selectandback.png", time_wait=20)
        self.joy_client.right_on_stick_ncount(count=3)
        self.joy_client.press(key='a-button', timeout=0.5)
        self.sikuli_client.wait_until_screen(screen=self.select_dir + "menutab.png", time_wait=20)
        self.joy_client.press_ncount(key='right-bumper', count=2, timeout=1)

    def select_challenges(self, num_chall=4):
        """
        Выбор нужного челленджа

        :param num_chall:
        :return: ничего
        """

        self.joy_client.right_on_stick_ncount(count=num_chall)
        self.joy_client.press(key='a-button', timeout=1)

    def select_half_challenges(self, list_act=['right', 'down']):
        """
        Выбор 1/4 части челленджа.

        :param list_act: список действий для перемещения до нужного челленджа
        :return: ничего
        """

        self.select_half_timeout = 0.5
        self.select_challengeone = '/sikuli_screenshot/selectchallengeone/'
        time.sleep(2)
        for self.a in list_act:
            if self.a == 'right':
                self.joy_client.right_on_stick(timeout=self.select_half_timeout)
            elif self.a == 'down':
                self.joy_client.down_on_stick(timeout=self.select_half_timeout)
            elif self.a == 'left':
                self.joy_client.left_on_stick(timeout=self.select_half_timeout)
            elif self.a == 'up':
                self.joy_client.up_on_stick(timeout=self.select_half_timeout)
        self.joy_client.press(key='a-button', timeout=self.select_half_timeout)
        try:
            self.sikuli_client.wait_until_screen(screen=self.select_challengeone + "startfromscratch.png", time_wait=5)
            self.joy_client.press(key='a-button', timeout=self.select_half_timeout)
        except:
            pass
        time.sleep(5)

    def buy_people_to_role(self, role, name, price, set_type):
        """
        Покупка нужного игрока.

        :param role: роль в расстановке. int
        :param name: имя для поиска. str
        :param price: цена для старта поиска для покупки. int
        :param set_type: определение 1/4 части выполнения челленджа. Расстановка игроков. От этого значения зависит,
         то какая функция будет вызвана для выставления нужного игрока на нужную позицию. int
         1523
         1442
         13412
         1433

            14141
            1343
            14222
            1451

        :return: ничего
        """

        self.buy_timeout = 0.5
        self.set_type = set_type
        self.select_challengeone = '/sikuli_screenshot/selectchallengeone/'
        self.sikuli_client.wait_until_screen(screen=self.select_challengeone + "playercard.png", time_wait=20)
        self.joy_client.press(key='left-bumper', timeout=self.buy_timeout)
        self.sikuli_client.wait_until_screen(screen=self.select_challengeone + "quality.png", time_wait=20)
        self.role = role
        self.name = name
        self.price = price

        self.joy_client.press(key='a-button', timeout=self.buy_timeout)  # X
        self.y = self.type_text_fifa(text=self.name)
        self.joy_client.down_on_stick_ncount(count=(2-self.y))
        self.joy_client.press(key='a-button', timeout=self.buy_timeout)  # X
        self.joy_client.down_on_stick(timeout=self.buy_timeout)
        self.joy_client.press(key='a-button', timeout=self.buy_timeout)  # X
        self.joy_client.press('left-trigger', timeout=self.buy_timeout) # сброс min price
        self.joy_client.right_on_stick(timeout=self.buy_timeout)
        self.joy_client.up_on_stick(timeout=self.buy_timeout)
        self.joy_client.press(key='left-trigger', timeout=self.buy_timeout) # сброс max buy now
        self.joy_client.right_on_stick(timeout=self.buy_timeout)
        if self.price < 1000:
            self.joy_client.right_on_stick_ncount(count=((self.price-200)/50), timeout=0.2)
        else:
            self.joy_client.right_on_stick_ncount(count=16, timeout=0.2)
            self.joy_client.right_on_stick_ncount(count=((self.price - 1000) / 100), timeout=0.2)
        self.joy_client.press(key='y-button')
        self.sikuli_client.wait_vanish_screen(screen=self.select_challengeone + "quality.png", time_wait=20)
        while True:
            try:
                self.sikuli_client.wait_until_screen(screen=self.select_challengeone + "noitems.png", time_wait=5)
                print('Нет таких ордеров на продаже')
                self.joy_client.press(key='y-button', timeout=self.buy_timeout) # Y
                self.joy_client.press(key='a-button', timeout=self.buy_timeout)
                self.joy_client.right_on_stick(timeout=self.buy_timeout)
                self.joy_client.press(key='y-button', timeout=self.buy_timeout)
            except:
                print('Что то изменилось...')
                self.joy_client.press(key='a-button', timeout=self.buy_timeout)
                self.joy_client.up_on_stick(timeout=self.buy_timeout)
                self.joy_client.press(key='a-button', timeout=self.buy_timeout)
                try:
                    self.sikuli_client.wait_until_screen(screen=self.select_challengeone + "succesbuy.png", time_wait=5)
                    print('Покупка удалась')
                    self.joy_client.stick_to_onehourse()
                    time.sleep(1)
                    self.joy_client.press(key='right-bumper')
                    time.sleep(1)
                    self.sikuli_client.wait_until_screen(screen=self.select_challengeone + "playercard.png",
                                                         time_wait=20)
                    if self.set_type == 1523:
                        set_players_1523(role=self.role, joy_client=self.joy_client)
                    elif self.set_type == 1442:
                        set_players_1442(role=self.role, joy_client=self.joy_client)
                    elif self.set_type == 13412:
                        set_players_13412(role=self.role, joy_client=self.joy_client)
                    elif self.set_type == 1433:
                        set_players_1433(role=self.role, joy_client=self.joy_client)
                    elif self.set_type == "14141_hybrid_leagues_R_D":
                        set_players_14141_hybrid_leagues_R_D(role=self.role, joy_client=self.joy_client)
                    elif self.set_type == 14222:
                        set_players_14222(role=self.role, joy_client=self.joy_client)
                    elif self.set_type == 1343:
                        set_players_1343(role=self.role, joy_client=self.joy_client)
                    elif self.set_type == "14141_hybrid_leagues_L_U":
                        set_players_14141_hybrid_leagues_L_U(role=self.role, joy_client=self.joy_client)
                    elif self.set_type == "14222_leagues_and_nations_L_D":
                        set_players_14222_leagues_and_nations_L_D(role=self.role, joy_client=self.joy_client)
                    break
                except:
                    print('Уже купили')
                    self.joy_client.press(key='a-button', timeout=self.buy_timeout)
                    self.joy_client.press(key='y-button', timeout=self.buy_timeout)
                    self.joy_client.press(key='a-button', timeout=self.buy_timeout)
                    self.joy_client.right_on_stick(timeout=self.buy_timeout)
                    self.joy_client.press(key='y-button', timeout=self.buy_timeout)

    def confirm_trafei(self):
        """
        Подтверждение полученного трафея

        :return: ничего
        """

        self.confirm_timeout = 0.5
        self.dir_confirm_trafei = '/sikuli_screenshot/confirmtrafei/'

        self.joy_client.press(key='start-button') # options
        time.sleep(2)
        self.joy_client.right_on_stick(timeout=self.confirm_timeout)
        self.joy_client.press(key='a-button', timeout=self.confirm_timeout)  # X
        time.sleep(2)
        while True:
            try:
                self.sikuli_client.wait_until_screen(screen=self.dir_confirm_trafei + "flag.png", time_wait=5)
                break
            except:
                try:
                    self.sikuli_client.wait_until_screen(screen=self.dir_confirm_trafei + "donechallange.png", time_wait=5) # если закончился челлендж
                    self.joy_client.press(key='a-button', timeout=2)  # X
                    break
                except:
                    self.joy_client.press(key='a-button', timeout=self.confirm_timeout)  # X

    def from_challenge_to_ultimate(self):
        """
        Возвращение из меню челленджа в главное меню ультимейт

        :return: ничего
        """
        self.fromch_to_ult_timeout = 2
        self.joy_client.press(key='b-button', timeout=self.fromch_to_ult_timeout) # O
        self.joy_client.press(key='b-button', timeout=self.fromch_to_ult_timeout)  # O
        self.joy_client.press(key='b-button', timeout=self.fromch_to_ult_timeout)  # O

    def open_store(self, default_offset):
        """
        Открытие торговой площадки

        :param default_offset: смещение, относительно начала. int
        :return: ничего
        """

        self.dir_open_store = '/sikuli_screenshot/openstore/'

        self.joy_client.right_on_stick_ncount(count=(4-default_offset))
        self.joy_client.press(key='a-button')  # X
        self.sikuli_client.wait_until_screen(screen=self.dir_open_store + "tabmenu.png", time_wait=20)

    def open_pack(self):
        """
        Открытие пака

        :return: ничего
        """

        self.dir_open_pack = '/sikuli_screenshot/openpack/'
        self.joy_client.press(key='a-button')  # X
        while True:
            try:
                self.sikuli_client.wait_until_screen(screen=self.dir_open_pack + "sendtotransferlist.png", time_wait=5)
                break
            except Exception as err:
                print(err)
                self.joy_client.press(key='a-button', timeout=0.5)  # X

    def check_price(self, name):
        """
        Получение цены для продажы

        :param name:
        :return: int
        """

        self.price_card, self.min_price_card = parse_info(name=name)

        return self.price_card, self.min_price_card

    def check_new_pack(self):
        """
        Проверка доступных паков

        :return: True or False. boolean
        """

        self.dir_new_pack = '/sikuli_screenshot/newpack/'
        try:
            self.sikuli_client.wait_until_screen(screen=self.dir_new_pack + "defmenu.png", time_wait=5)
            return False
        except:
            return True

    def recognition_count_card_inpack(self):
        """
        Распознование числа карт в паке.

        :return: число карт в паке. int
        """

        self.dir_open_pack = '/sikuli_screenshot/openpack/'
        self.img = Image.fromarray(
            self.sikuli_client.get_screen_offset(
                screen=self.dir_open_pack + "sendtotransferlist.png",
                x_off=725,
                y_off=75,
                w_off=85,
                h_off=25
            )
        )
        self.img = ImageOps.invert(self.img).filter(ImageFilter.CONTOUR)
        # self.img.show()
        self.count_card = int(self.sikuli_client.
                              recognize_text(self.img, lang='eng').
                              replace(' \n', '').replace('\n', '').replace('\x0c', '').split(' ')[0])
        print(self.count_card)

        return self.count_card

    def recognition_info_card(self):
        """
        Распознование информации о карте: имя

        :return: string
        """

        self.recogn_info_card_timeout = 0.5
        self.rec_dir = "/sikuli_screenshot/recognitioncard/"

        try:
            self.sikuli_client.wait_until_screen(screen=self.rec_dir + "playerdetails.png", time_wait=1)
            self.joy_client.press(key='right-stick-press', timeout=self.recogn_info_card_timeout)
            self.img = Image.fromarray(
                self.sikuli_client.get_screen_offset(
                    screen=self.rec_dir + "playerbio.png",
                    x_off=220,
                    y_off=80,
                    w_off=75,
                    h_off=15
                )
            )
            ImageOps.invert(self.img).filter(ImageFilter.SHARPEN).filter(ImageFilter.SHARPEN)
            self.rec_text = self.sikuli_client.recognize_text(ImageOps.invert(self.img).filter(ImageFilter.SHARPEN).
                                                              filter(ImageFilter.SHARPEN)).split('\n')[0].\
                replace(':','').replace('.','').replace(',','').replace('!','').replace('?','')
            print(self.rec_text)
            self.joy_client.press(key='right-stick-press', timeout=self.recogn_info_card_timeout)
            return self.rec_text
        except Exception as err:
            print('Не игрок:', err)

            try:
                self.sikuli_client.wait_until_screen(screen=self.rec_dir + "duplicates.png", time_wait=1)
                return 'BLUE'
            except Exception as err:
                print('Не дубликат:', err)
                try:
                    self.sikuli_client.wait_until_screen(screen=self.rec_dir + "duplicates.png", time_wait=1) # ВРЕМЕННО!!!
                    return 'GREEN'
                except Exception as err:
                    print('Не зеленый:', err)
                    return 'TRASH'

    def sell_card(self, price, min_price):
        """
        Продажа карты.

        :param price:
        :return: ничего
        """

        self.sell_timeout = 0.5
        self.dir_sell_card = '/sikuli_screenshot/sellcard/'
        self.joy_client.press(key='x-button', timeout=self.sell_timeout)  # квадратик
        self.joy_client.press('left-trigger', timeout=self.sell_timeout)  # сброс
        self.joy_client.down_on_stick(timeout=self.sell_timeout)
        self.joy_client.press('left-trigger', timeout=self.sell_timeout)  # сброс

        # цена выставляется на шаг ниже
        if price <= 1000:
            self.joy_client.right_on_stick_ncount(count=((price-min_price)/50)-2)
        elif price > 1000 and min_price <= 1000:
            self.joy_client.right_on_stick_ncount(count=int((1000-min_price)/50)-2)
            self.joy_client.right_on_stick_ncount(count=int((price-1000)/100))
        elif price > 1000 and min_price > 1000:
            self.joy_client.right_on_stick_ncount(count=int((price - min_price) / 100)-2)
        self.joy_client.down_on_stick_ncount(count=3)
        self.joy_client.press(key='a-button', timeout=self.sell_timeout)  # X
        self.sikuli_client.wait_until_screen(screen=self.dir_sell_card + "5com.png", time_wait=10)
        self.joy_client.press(key='a-button', timeout=self.sell_timeout)  # X

    def cart_to_trash(self):
        """
        Скип мусора

        :return: ничего
        """

        self.joy_client.right_stick_down()

    def cart_to_auction(self):
        """
        Выставляем карту на аукцион. Если не получилось узнать цену

        :return:
        """
        self.cart_to_auction_timeout = 0.5
        self.dir_sell_card = '/sikuli_screenshot/sellcard/'
        self.joy_client.press(key='x-button', timeout=1)  # квадратик

        self.joy_client.down_on_stick_ncount(count=4)
        self.joy_client.press(key='a-button')  # X
        self.sikuli_client.wait_until_screen(screen=self.dir_sell_card + "5com.png", time_wait=10)
        self.joy_client.press(key='a-button', timeout=self.cart_to_auction_timeout)  # X

    def action_cards_inpack(self):
        """
        Разбираемся с картами в доступном паке

        :return: ничего
        """

        self.action_cards_inpack_timeout = 0.5
        self.count_card_inpack = self.recognition_count_card_inpack()
        for self.e in range(0, self.count_card_inpack-2):
            self.name_player = self.recognition_info_card()[0:14]
            if self.name_player == 'BLUE' or self.name_player == 'TRASH':
                self.cart_to_trash()
            elif self.name_player == 'GREEN':
                self.joy_client.press(key='a-button', timeout=3)  # X
                self.joy_client.press(key='a-button', timeout=self.action_cards_inpack_timeout)  # X
            else:
                try:
                    self.price_player, self.min_price_player = self.check_price(name=self.name_player) # если цену получилось узнать
                    self.sell_card(price=self.price_player, min_price=self.min_price_player)
                except:
                    self.cart_to_auction()

        self.cart_to_trash()
        try:
            self.sikuli_client.wait_until_screen(screen=self.rec_dir + "duplicates.png", time_wait=1)
        except Exception as err:
            print('Последний итем не дубликат. Пробуем активировать:', err)
            self.joy_client.press(key='a-button', timeout=1)  # X
        self.cart_to_trash()
        self.joy_client.press(key='right-trigger', timeout=self.action_cards_inpack_timeout)
        self.joy_client.press(key='a-button', timeout=self.action_cards_inpack_timeout)  # X

    def test(self):
        self.action_cards_inpack()

    def type_text_fifa(self, text):
        """
        Печать текста виртуальной клавиатурой fifa

        :param text: string
        :return: смещенеи по оси y
        """

        print(text)
        self.type_timeout = 0.1
        self.x = 0
        self.y = 0
        for self.a in text:
            if self.a != " ":
                self.x_dif = template_keyboard[self.a][0] - self.x
                self.y_dif = template_keyboard[self.a][1] - self.y
                self.x = template_keyboard[self.a][0]
                self.y = template_keyboard[self.a][1]
                if self.x_dif < 0:
                    self.joy_client.left_on_stick_ncount(count=abs(self.x_dif), timeout=self.type_timeout)
                elif self.x_dif > 0:
                    self.joy_client.right_on_stick_ncount(count=self.x_dif, timeout=self.type_timeout)
                elif self.x_dif == 0:
                    pass

                if self.y_dif < 0:
                    self.joy_client.up_on_stick_ncount(count=abs(self.y_dif), timeout=self.type_timeout)
                elif self.y_dif > 0:
                    self.joy_client.down_on_stick_ncount(count=self.y_dif, timeout=self.type_timeout)
                elif self.y_dif == 0:
                    pass

                self.joy_client.press(key='a-button', timeout=0.5)
            else:
                self.joy_client.press(key="right-trigger", timeout=0.5)
        return self.y

    def auth(self, login='anduinny@bk.ru', password='Vddvsttcson1'):
        self.auth_dir = "/sikuli_screenshot/auth/"
        self.sikuli_client.type_to_screen(screen=self.auth_dir+"playlogo.png", dx=-71, dy=226, text=login) #log
        self.sikuli_client.type_to_screen(screen=self.auth_dir + "playlogo.png", dx=-71, dy=277, text=password) #pass
        self.sikuli_client.click_to_screen(screen=self.auth_dir + "btn_login.png")

    def open_fifa(self):
        try:
            pass
        except Exception as err:
            if find_error_connect:
                raise ERROR_CONNECT_PS4(err)

