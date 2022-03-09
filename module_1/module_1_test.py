from collections import Counter
from random import randint

from module_1 import Cards, Hand, Player

def test_generate_cards_tuple():
    # given
    point_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]

    # when
    cards = Cards()
    figures_counter = Counter(elem[1] for elem in cards.cards)
    number_color = len(list(figures_counter.values()))
    counter_number_per_colour = list(figures_counter.values())
    value_counter = Counter(elem[2] for elem in cards.cards)
    total_poin_sum = sum([k*v for k, v in value_counter.items()])

    # then

    assert len(cards.cards) == 48
    assert number_color == 4
    assert len(set(counter_number_per_colour)) == 1
    assert len(list(value_counter.values())) == len(set(point_list))
    assert total_poin_sum == sum(point_list)*4


def test_cards_is_shuffled():
    # given
    first_card = (2, 'Trefl', 2)
    last_card = ('As', 'Karo', 11)

    # when
    cards = Cards()

    # then
    assert (cards.cards[0] != first_card) or (cards.cards[-1] != last_card)

def test_get_card():
    # given
    counter = 0
    # when
    cards = Cards()
    for i in range(randint(1, 48)):
        cards.get_card()
        counter += 1

    # then
    assert len(cards.cards) == 48 - counter
    assert cards.card_received is not None
    assert len(cards.card_received) == 3


def test_on_hand():
    hand = Hand()
    hand.get_card_on_hand()

    hand2 = Hand()
    hand2.get_card_on_hand()
    hand2.get_card_on_hand()

    assert len(hand.hand) == 1
    assert len(hand2.hand) == 2

def test_player_name():
    # given
    player_1_name = 'Max'
    player_2_name = 'Croupier'
    # when
    player2 = Player()
    player2.get_card_on_hand()
    player1 = Player(player_1_name)

    assert player1.name_player == player_1_name
    assert player2.name_player == player_2_name




