"""
Black Jack Game when you can play with your computer
"""
# Game, Player, Deck, Card, Hand?
from random import shuffle
from datetime import datetime


class WinExeption(Exception):
    pass


class LossExeption(Exception):
    pass


class DrawExeption(Exception):
    pass


class Cards:
    def __init__(self):
        self.card_received = None
        self.cards = self._generate_cards_tuple()
        self._shuffle_cards(self.cards)

    @staticmethod
    def _generate_cards_tuple():
        list_type = ["Trefl", "Pik", "Kier", "Karo"]
        list_colors = sum([[el for _ in range(12)] for el in list_type], [])
        list_figures_number = list(range(2, 10))
        list_figures_rest = ["Jopek", "Damka", "Król", "As"]
        list_figures = list_figures_number + list_figures_rest
        list_values_card = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
        list_cards = list(zip(list_figures * 4, list_colors, list_values_card * 4))
        return list_cards

    @staticmethod
    def _shuffle_cards(cards_list):
        return shuffle(cards_list)

    def __str__(self):
        return str(self.cards)

    def get_card(self):
        self.card_received = self.cards.pop(-1)


class Hand(Cards):
    def __init__(self):
        super().__init__()
        self.hand = []

    def __str__(self):
        return str(self.hand)


class Player(Hand):
    def __init__(self, name_player="Croupier"):
        super().__init__()
        self.name_player = name_player

    def get_card_on_hand(self):
        super().get_card()
        self.hand.append(self.card_received)
        self.check_if_win_or_lose(self.hand)

    def check_if_win_or_lose(self, player):
        # TODO TEST cards_values = [11,11]
        cards_values = [card[2] for card in player]
        if len(cards_values) == 2 and sum(cards_values) == 22:
            raise WinExeption(f"Wygrał: {self.name_player}")
        elif sum(cards_values) > 21:
            print(self.hand)
            raise LossExeption(f"Przegrana: {self.name_player}a")


class Game(Player):
    def __init__(self):
        # TODO add possibility to read data in csv/bd
        super().__init__()
        now = datetime.now()
        self.name_of_play = now.strftime("%Y_%m_%d_%H_%M_%S")
        self.player2 = Player()
        self.player1 = ''
        # self.pygame = pygame.init()
        # self.screen = pygame.display.set_mode((640, 400))

    def __del__(self):
        # TODO add possibility to store data in csv/bd
        # self.pygame.quit()
        pass

    def start_game(self):
        self.ask_user_his_name()
        self.draw_two_cards_for_each_player()
        print(self.player2.hand[:1])
        # os.system('read -s -n 1 -p "Press any key to continue..."')
        # pygame.init()
        # screen = pygame.display.set_mode((640, 400))
        print('Please told me if you want take one more card')
        print(f"{self.player1.name_player} have {self.count_sum_of_cards(self.player1.hand)} point\n"
              f"{self.player1.name_player} card is {self.player1.hand}")
        while True:
            pressed_key = input("Press Y to take a card N to pass or Q to quit: ")
            if pressed_key.lower() == 'q':
                print('You Pressed Q good by!')
                break
            elif pressed_key.lower() == 'y':
                self.player1.get_card_on_hand()
                self.count_sum_of_cards(self.player1.hand)
                print('You press Y')
                print(f"{self.player1.name_player} have {self.count_sum_of_cards(self.player1.hand)} point\n"
                      f"{self.player1.name_player} card is {self.player1.hand}")

            elif pressed_key.lower() == 'n':
                print('You press N')
                # print(f"{self.player2.name_player} have {self.count_sum_of_cards(self.player2.hand)} point\n"
                #       f"{self.player2.name_player} card is {self.player2.hand}")
                while self.count_sum_of_cards(self.player2.hand) < 21:
                    self.inform_players_about_score()
                    if self.count_sum_of_cards(self.player2.hand) > self.count_sum_of_cards(self.player1.hand):
                        raise LossExeption(f"Przegrana: {self.player2.name_player}a")
                    elif self.count_sum_of_cards(self.player2.hand) == self.count_sum_of_cards(self.player1.hand):
                        raise DrawExeption(
                            f"Remis: {self.player2.name_player} i {self.player1.name_player} zremisowali")
                    else:
                        self.player2.get_card_on_hand()
            else:
                print('you press N or Y or Q')

    def inform_players_about_score(self):
        print(f"{self.player2.name_player} have {self.count_sum_of_cards(self.player2.hand)} point\n"
              f"{self.player2.name_player} card is {self.player2.hand}")
        print(f"{self.player1.name_player} have {self.count_sum_of_cards(self.player1.hand)} point\n"
              f"{self.player1.name_player} card is {self.player1.hand}")

    @staticmethod
    def count_sum_of_cards(player):
        return sum([card[2] for card in player])

    def draw_two_cards_for_each_player(self):
        self.player2.get_card_on_hand()
        self.player1.get_card_on_hand()
        self.player2.get_card_on_hand()
        self.player1.get_card_on_hand()

    def ask_user_his_name(self):
        # TODO change to this
        # self.player1 = Player(input("Please provide name of player: "))
        self.player1 = Player("Max")


if __name__ == '__main__':
    game = Game()
    try:
        game.start_game()
    except WinExeption as e:
        print(e)
    except LossExeption as e:
        print(e)
    except DrawExeption as e:
        print(e)
