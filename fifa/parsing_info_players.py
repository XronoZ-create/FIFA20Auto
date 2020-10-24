"""
Парсинг инфы об игроках на сайте

"""

import requests
from bs4 import BeautifulSoup
from fifa.exceptions import NO_FIND_PARSE

def parse_info(name):
    dict_price = {} # id:price
    dict_min_price = {} # id:price
    url1 = 'https://www.futbin.com/21/players?page=1&search=%s'%name
    url2 = 'https://www.futbin.com%s'
    url3 = 'https://www.futbin.com/21/playerPrices?player=%s'
    bs = BeautifulSoup(requests.get(url1).text)
    if bs.find_all('li', {'class':'page-item'}) != []:
        raise NO_FIND_PARSE
    for a in bs.find('table', {'id':'repTb'}).find('tbody').find_all('tr', recursive=False):
        data_url = a['data-url']
        id_player = BeautifulSoup(requests.get(url2%data_url).text).find('div', {"id":"page-info"})['data-player-resource']
        json_req = requests.get(url3%id_player).json()
        price_player = json_req[id_player]['prices']['ps']['LCPrice'].replace(',', '')
        min_price = json_req[id_player]['prices']['ps']['MinPrice'].replace(',', '')
        dict_price[id_player] = int(price_player)
        dict_min_price[id_player] = int(min_price)

    print(dict_price)
    print(dict_min_price)

    iter_price = 0
    for a, b in dict_price.items():
        if b > iter_price:
            iter_price = b
            iter_id = a

    print(iter_price, dict_min_price[iter_id])


    return iter_price, dict_min_price[iter_id]

