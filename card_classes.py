from random import shuffle


# Defines the single card, with a suit and rank and a given point value, as well as an alt value for ace
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = {
            "Ace": 11,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5,
            "Six": 6,
            "Seven": 7,
            "Eight": 8,
            "Nine": 9,
            "Ten": 10,
            "Jack": 2,
            "Queen": 3,
            "King": 4
        }

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value[self.rank]


# Defines a deck, at the base of which is a list of Card objects.
class DeckOfCards:
    def __init__(self):
        self.__suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
        self.__ranks = [
            "Ace",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Jack",
            "Queen",
            "King"
        ]
        self.cards = []
        self.discarded = []

        for suit in self.__suits:
            for rank in self.__ranks:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        self.cards += self.discarded
        self.discarded = []
        shuffle(self.cards)

    def draw_card(self):
        drawn_card = self.cards[0]
        self.cards.remove(drawn_card)
        self.discarded.append(drawn_card)
        return drawn_card

    def no_of_playable_cards(self):
        return len(self.cards)

    def no_of_discarded_cards(self):
        return len(self.discarded)


# List of cards currently in play by the player or the dealer
class CardsInPlay:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def get_value(self):
        total_value = 0
        for card in self.cards:
            total_value += card.get_value()
        return total_value

    def clear(self):
        self.cards.clear()

    def perskie_oko(self):
        number_of_aces = 0
        for card in self.cards:
            if card.rank == "Ace":
                number_of_aces += 1
        if number_of_aces >= 2:
            return True
        return False


deck = DeckOfCards()
deck.shuffle()

player_cards = CardsInPlay()
dealer_cards = CardsInPlay()
