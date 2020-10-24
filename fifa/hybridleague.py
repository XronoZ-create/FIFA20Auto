"""
Класс челленджа Hybrid League

"""
from fifa.fifa import FifaClass
import time
from fifa.players import players
from PIL import Image, ImageOps, ImageFilter, ImageDraw
from difflib import SequenceMatcher

class HybridLeague(FifaClass):

    def similar(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

    def unic_hybrid_league(self):
        self.joy_client.up_on_stick(timeout=0.5)
        self.joy_client.right_on_stick_ncount(count=2)
        self.joy_client.press(key='x-button', timeout=0.5)  # квадратик
        self.joy_client.down_on_stick_and_x()
        time.sleep(2)
        self.joy_client.press(key='a-button', timeout=4)  # X
        self.joy_client.press(key='b-button')  # O


    def confirm_trafei_uniq(self):
        """
        Подтверждение полученного трафея

        :return: ничего
        """

        self.confirm_timeout = 0.5

        self.joy_client.press(key='start-button') # options
        time.sleep(3)
        self.joy_client.right_on_stick(timeout=self.confirm_timeout)
        self.joy_client.press(key='a-button', timeout=self.confirm_timeout)  # X
        time.sleep(2)
        self.joy_client.up_on_stick(timeout=0.5)
        self.joy_client.press(key='a-button', timeout=0.5)  # X
        self.joy_client.press(key='b-button', timeout=self.confirm_timeout)  # O
        time.sleep(3)

    def passing_HybridLeague(self):
        #Уникальная механика для прохождения челленджа только для этой лиги
        self.task_half_challenges = [
            ["14141_hybrid_leagues_R_D", ['right', 'down']],
        ]
        for self.act in self.task_half_challenges:
            self.select_challenges_found()
            self.select_challenges(num_chall=3)
            self.select_half_challenges(list_act=self.act[1])
            self.select_challengeone = '/sikuli_screenshot/selectchallengeone/'
            self.sikuli_client.wait_until_screen(screen=self.select_challengeone + "playercard.png", time_wait=20)
            self.league = self.set_st_role()
            for self.playerrole, self.playerdata in players[self.act[0]][self.league].items():
                self.buy_people_to_role(role=self.playerrole,
                                        name=self.playerdata['name'],
                                        price=self.playerdata['price'],
                                        set_type=self.act[0])
            self.unic_hybrid_league()
            self.confirm_trafei_uniq()
            self.from_challenge_to_ultimate()
            self.open_store(default_offset=2)
            while self.check_new_pack() == True:
                self.open_pack()
                time.sleep(2)
                self.action_cards_inpack()
            self.joy_client.press(key='b-button')  # O
            time.sleep(2)
            self.joy_client.left_on_stick_ncount(count=4)
        #Обычная механика для оставшихся челленджей
        self.task_half_challenges = [
            [14222, ['down']],
            ["14141_hybrid_leagues_L_U", [""]],
            [1343, ["right"]]
        ]

        for self.act in self.task_half_challenges:
            self.select_challenges_found()
            self.select_challenges(num_chall=3)
            self.select_half_challenges(list_act=self.act[1])
            for self.playerrole, self.playerdata in players[self.act[0]].items():
                self.buy_people_to_role(role=self.playerrole,
                                        name=self.playerdata['name'],
                                        price=self.playerdata['price'],
                                        set_type=self.act[0])
            self.confirm_trafei()
            self.from_challenge_to_ultimate()
            self.open_store(default_offset=2)
            while self.check_new_pack() == True:
                self.open_pack()
                time.sleep(2)
                self.action_cards_inpack()
            self.joy_client.press(key='b-button')  # O
            time.sleep(2)
            self.joy_client.left_on_stick_ncount(count=4)

    def set_st_role(self):
        self.set_st_dir = "/sikuli_screenshot/setstrole/"
        self.set_st_role_timeout = 0.5
        self.joy_client.up_on_stick_ncount(count=2)
        time.sleep(self.set_st_role_timeout)
        self.joy_client.press(key='a-button', timeout=self.set_st_role_timeout)  # X
        self.joy_client.press(key='right-bumper', timeout=self.set_st_role_timeout) # R1
        time.sleep(3)
        self.joy_client.press(key='a-button', timeout=self.set_st_role_timeout)  # X
        time.sleep(3)
        self.league = self.recognize_league()
        self.joy_client.down_on_stick_ncount(count=2)

        return self.league

    def recognize_league(self):
        self.rec_dir = "/sikuli_screenshot/recognitionleague/"
        self.recognize_league_timeout = 0.5
        self.joy_client.press(key='right-stick-press', timeout=self.recognize_league_timeout)
        self.joy_client.press(key='right-bumper', timeout=self.recognize_league_timeout)  # R1
        self.img = Image.fromarray(
            self.sikuli_client.get_screen_offset(
                screen=self.rec_dir + "playerbio.png",
                x_off=205,
                y_off=220,
                w_off=150,
                h_off=15
            )
        )
        # ImageOps.invert(self.img).filter(ImageFilter.SHARPEN).filter(ImageFilter.SHARPEN)
        # self.img.show()
        self.rec_text = self.sikuli_client.recognize_text(ImageOps.invert(self.img).filter(ImageFilter.SHARPEN).
                                                          filter(ImageFilter.SHARPEN), lang='eng').split('\n')[0]. \
            replace(':', '').replace('.', '').replace(',', '').replace('!', '').replace('?', '')
        for self.league_comp in players['14141_hybrid_leagues_R_D'].keys():
            if self.similar(a = self.rec_text, b = self.league_comp) >= 0.8:
                self.rec_text = self.league_comp
                break
        print(self.rec_text)
        self.joy_client.press(key='left-bumper', timeout=self.recognize_league_timeout)  # L1
        self.joy_client.press(key='right-stick-press', timeout=self.recognize_league_timeout)
        time.sleep(3)
        return self.rec_text

