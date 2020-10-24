"""
Функции выставления игроков в разных расстановках.
Отсчет позиций всегда начинается слева/снизу в вправо/вверх

"""

set_timeouts = 1

def set_players_1523(role, joy_client):
    """
    Выставление игрока для 1523-схемы

    :return: ничего
    """
    if int(role) == 1:
        joy_client.press(key='a-button', timeout=set_timeouts)  # X
    elif int(role) == 2:
        joy_client.up_on_stick_ncount(count=1)
        joy_client.left_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.right_on_stick_ncount(count=1)
        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 3:
        joy_client.up_on_stick_ncount(count=1)
        joy_client.left_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.right_on_stick_ncount(count=1)
        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 4:
        joy_client.up_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 5:
        joy_client.up_on_stick_ncount(count=1)
        joy_client.right_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.left_on_stick_ncount(count=1)
        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 6:
        joy_client.up_on_stick_ncount(count=1)
        joy_client.right_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.left_on_stick_ncount(count=2)
        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 7:
        joy_client.up_on_stick(timeout=set_timeouts)
        joy_client.left_on_stick(timeout=set_timeouts)
        joy_client.up_on_stick(timeout=set_timeouts)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 8:
        joy_client.up_on_stick(timeout=set_timeouts)
        joy_client.left_on_stick(timeout=set_timeouts)
        joy_client.up_on_stick(timeout=set_timeouts)
        joy_client.right_on_stick(timeout=set_timeouts)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 9:
        joy_client.up_on_stick_ncount(count=2)
        joy_client.left_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.right_on_stick_ncount(count=1)
        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 10:
        joy_client.up_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 11:
        joy_client.up_on_stick_ncount(count=2)
        joy_client.right_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.left_on_stick_ncount(count=1)
        joy_client.down_on_stick_ncount(count=2)


def set_players_1442(role, joy_client):
    """
    Выставление игрока для 1442-схемы

    :return: ничего
    """

    if int(role) == 1:
        joy_client.press(key='a-button', timeout=set_timeouts)  # X
    elif int(role) == 2:
        joy_client.left_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 3:
        joy_client.left_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 4:
        joy_client.right_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 5:
        joy_client.right_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 6:
        joy_client.left_on_stick_ncount(count=1)
        joy_client.up_on_stick(timeout=set_timeouts)
        joy_client.left_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 7:
        joy_client.left_on_stick_ncount(count=1)
        joy_client.up_on_stick(timeout=set_timeouts)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 8:
        joy_client.right_on_stick(timeout=set_timeouts)
        joy_client.up_on_stick(timeout=set_timeouts)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 9:
        joy_client.right_on_stick(timeout=set_timeouts)
        joy_client.up_on_stick_ncount(count=2)
        joy_client.right_on_stick(timeout=set_timeouts)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 10:
        joy_client.left_on_stick(timeout=set_timeouts)
        joy_client.up_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=3)
    elif int(role) == 11:
        joy_client.right_on_stick(timeout=set_timeouts)
        joy_client.up_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=3)


def set_players_13412(role, joy_client):
    """
    Выставление игрока для 13412-схемы

    :return: ничего
    """

    if int(role) == 1:
        joy_client.press(key='a-button', timeout=set_timeouts)  # X
    elif int(role) == 2:
        joy_client.left_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 3:
        joy_client.up_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 4:
        joy_client.right_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 5:
        joy_client.left_on_stick_ncount(count=3)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 6:
        joy_client.left_on_stick(timeout=set_timeouts)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 7:
        joy_client.right_on_stick(timeout=set_timeouts)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 8:
        joy_client.right_on_stick_ncount(count=3)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 9:
        joy_client.up_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 10:
        joy_client.up_on_stick_ncount(count=3)
        joy_client.left_on_stick(timeout=set_timeouts)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=3)
    elif int(role) == 11:
        joy_client.up_on_stick_ncount(count=3)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=3)


def set_players_1433(role, joy_client):
    """
    Выставление игрока для 1433-схемы

    :return: ничего
    """

    if int(role) == 1:
        joy_client.press(key='a-button', timeout=set_timeouts)  # X
    elif int(role) == 2:
        joy_client.left_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 3:
        joy_client.left_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 4:
        joy_client.right_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 5:
        joy_client.right_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 6:
        joy_client.up_on_stick_ncount(count=1)
        joy_client.left_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 7:
        joy_client.up_on_stick(timeout=set_timeouts)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 8:
        joy_client.up_on_stick(timeout=set_timeouts)
        joy_client.right_on_stick(timeout=set_timeouts)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 9:
        joy_client.up_on_stick_ncount(count=2)
        joy_client.left_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=3)
    elif int(role) == 10:
        joy_client.up_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 11:
        joy_client.up_on_stick_ncount(count=2)
        joy_client.right_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.left_on_stick_ncount(count=1)
        joy_client.down_on_stick_ncount(count=2)


def set_players_14141_hybrid_leagues_R_D(role, joy_client):
    """
    Выставление игрока для 14141-схемы

    :return: ничего
    """

    if int(role) == 1:
        joy_client.press(key='a-button', timeout=set_timeouts)  # X
    elif int(role) == 2:
        joy_client.left_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 3:
        joy_client.left_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 4:
        joy_client.right_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 5:
        joy_client.right_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 6:
        joy_client.up_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 7:
        joy_client.up_on_stick(timeout=set_timeouts)
        joy_client.left_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 8:
        joy_client.up_on_stick(timeout=set_timeouts)
        joy_client.left_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 9:
        joy_client.up_on_stick(timeout=set_timeouts)
        joy_client.right_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 10:
        joy_client.up_on_stick_ncount(count=1)
        joy_client.right_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 11:
        joy_client.up_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)


def set_players_14222(role, joy_client):
    """
    Выставление игрока для 14222-схемы

    :return: ничего
    """

    if int(role) == 1:
        joy_client.press(key='a-button', timeout=set_timeouts)  # X
    elif int(role) == 2:
        joy_client.left_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 3:
        joy_client.left_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 4:
        joy_client.right_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 5:
        joy_client.right_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 6:
        joy_client.left_on_stick_ncount(count=1)
        joy_client.up_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 7:
        joy_client.left_on_stick_ncount(count=1)
        joy_client.up_on_stick(timeout=set_timeouts)
        joy_client.right_on_stick(timeout=set_timeouts)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 8:
        joy_client.up_on_stick_ncount(count=2)
        joy_client.left_on_stick(timeout=set_timeouts)
        joy_client.press(key='a-button', tset_timeoutsut=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 9:
        joy_client.right_on_stick_ncount(count=1)
        joy_client.up_on_stick(timeout=set_timeouts)
        joy_client.right_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 10:
        joy_client.up_on_stick_ncount(count=3)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=3)
    elif int(role) == 11:
        joy_client.up_on_stick_ncount(count=3)
        joy_client.right_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=3)


def set_players_1343(role, joy_client):
    """
    Выставление игрока для 1343-схемы

    :return: ничего
    """

    if int(role) == 1:
        joy_client.press(key='a-button', timeout=set_timeouts)  # X
    elif int(role) == 2:
        joy_client.left_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 3:
        joy_client.up_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 4:
        joy_client.right_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 5:
        joy_client.left_on_stick_ncount(count=3)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 6:
        joy_client.left_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 7:
        joy_client.right_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 8:
        joy_client.right_on_stick_ncount(count=3)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 9:
        joy_client.up_on_stick(timeout=set_timeouts)
        joy_client.left_on_stick_ncount(count=1)
        joy_client.up_on_stick(timeout=set_timeouts)
        joy_client.left_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 10:
        joy_client.up_on_stick_ncount(count=3)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=3)
    elif int(role) == 11:
        joy_client.up_on_stick_ncount(count=1)
        joy_client.right_on_stick_ncount(count=1)
        joy_client.up_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)


def set_players_14141_hybrid_leagues_L_U(role, joy_client):
    """
            Выставление игрока для 14141-схемы

            :return: ничего
            """

    if int(role) == 1:
        joy_client.press(key='a-button', timeout=set_timeouts)  # X
    elif int(role) == 2:
        joy_client.left_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 3:
        joy_client.left_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 4:
        joy_client.right_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 5:
        joy_client.right_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 6:
        joy_client.up_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 7:
        joy_client.up_on_stick(timeout=set_timeouts)
        joy_client.left_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 8:
        joy_client.up_on_stick(timeout=set_timeouts)
        joy_client.left_on_stick_ncount(count=1)
        joy_client.right_on_stick(timeout=set_timeouts)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 9:
        joy_client.up_on_stick(timeout=set_timeouts)
        joy_client.right_on_stick_ncount(count=1)
        joy_client.left_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 10:
        joy_client.up_on_stick_ncount(count=1)
        joy_client.right_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 11:
        joy_client.up_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)


def set_players_14222_leagues_and_nations_L_D(role, joy_client):
    """
        Выставление игрока для 14222-схемы из челленджа league and nation hybrid

        :return: ничего
        """

    if int(role) == 1:
        joy_client.press(key='a-button', timeout=set_timeouts)  # X
    elif int(role) == 2:
        joy_client.left_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 3:
        joy_client.left_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 4:
        joy_client.right_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 5:
        joy_client.right_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 6:
        joy_client.up_on_stick_ncount(count=1)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 7:
        joy_client.up_on_stick(timeout=set_timeouts)
        joy_client.right_on_stick(timeout=set_timeouts)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=1)
    elif int(role) == 8:
        joy_client.up_on_stick(timeout=set_timeouts)
        joy_client.left_on_stick(timeout=set_timeouts)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 9:
        joy_client.up_on_stick(timeout=set_timeouts)
        joy_client.right_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 10:
        joy_client.up_on_stick_ncount(count=2)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)
    elif int(role) == 11:
        joy_client.up_on_stick_ncount(count=2)
        joy_client.right_on_stick(timeout=set_timeouts)
        joy_client.press(key='a-button', timeout=set_timeouts)  # X

        joy_client.down_on_stick_ncount(count=2)