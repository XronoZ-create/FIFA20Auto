"""
Класс челленджа hybrid nation

"""

from fifa.fifa import FifaClass
import time
from fifa.players import players

class HybridNations(FifaClass):

    def passing_HybridNations(self):
        self.task_half_challenges = [
            [1523, ['right', 'down']],
            [1433, ['down']],
            [13412, ['']],
            [1442, ['right']]
        ]
        for self.act in self.task_half_challenges:
            self.select_challenges_found()
            self.select_challenges(num_chall=4)
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