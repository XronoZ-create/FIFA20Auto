from fifa.fifa import FifaClass
from fifa.nationhybrid import LeagueAndNationHybrid
from fifa.hybridleague import HybridLeague
import os
import time
from fifa.players import players

dir = os.path.dirname(os.path.realpath(__file__))


f = HybridLeague(dir=dir)
time.sleep(3)

a = 'fabian'

c = f.action_cards_inpack()


