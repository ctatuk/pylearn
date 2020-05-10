'''
    Source: http://pythontutor.ru/lessons/for_loop/problems/lost_card/
    For a board game, cards with numbers from 1 to N are used.
    One card was lost. Find her, knowing the numbers of the remaining cards.
    Given the number N, then N - 1 number of the remaining cards (various numbers from 1 to N).
    The program should display the number of the lost card.
    For the smartest: arrays and similar data structures cannot be used.
'''
def table_game(n, card_list):

    num_list = range(1, n + 1)
    missing_card = sum(num_list) - sum(card_list)
    print(missing_card)


table_game(6, [1, 3, 4, 5, 6])