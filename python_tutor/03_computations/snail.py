from math import ceil


def pole_snail(pole_height, up_speed, down_speed):
    """
    Source https://pythontutor.ru/lessons/int_and_float/problems/ulitka/
    Condition
    The snail creeps along a vertical pole with a height of h meters, rising a meters/day,
    and descending b meters by night.
    On what day does the snail crawl to the top of the pole?
    The program receives input natural numbers h, a, b.
    The program should print one natural number. It is guaranteed that a> b.
    """
    if pole_height < 0 or up_speed < 0 or down_speed < 0:
        raise Exception('Invalid arguments, all arguments should be >= 0')
    if down_speed > up_speed:
        raise Exception('Snail is too slow to raise above {}m'.format(up_speed))

    if pole_height == 0:
        print('Pole is not long enough')
        return 0
    if pole_height <= up_speed:
        print('Looks like it will take less than a day')
        return 1
    if down_speed > up_speed:
        raise Exception('Snail is too slow to raise above {}m'.format(up_speed))

    adjusted_speed = up_speed - down_speed
    count_days = pole_height / adjusted_speed
    print('The journey lasted looong {} days'.format(ceil(count_days)))


pole_snail(740, 3, 2.5)
