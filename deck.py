import random

class Card:
    """
    A class representing a standard playing card with rank and suit.
    """
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♠", "♣", "♥", "♦"]

    def __init__(self, suit, rank):
        """
        Initialize a Card with a given suit and rank.

        :param suit: One of the four valid suits (♠, ♣, ♥, ♦)
        :param rank: One of the valid ranks (2–10, J, Q, K, A)
        :raises ValueError: if suit or rank is invalid
        """
        if rank not in self.RANKS:
            raise ValueError("Invalid Rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid Suit")
        self._suit = suit
        self._rank = rank

    def __eq__(self, other):
        """
        Compare two cards by rank for equality.

        :param other: another Card
        :return: True if ranks are equal
        """
        return self.rank == other.rank

    def __gt__(self, other):
        """
        Compare two cards by rank to determine greater-than.

        :param other: another Card
        :return: True if this card's rank is higher
        """
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

    def __str__(self):
        """
        Human-readable string representation of the Card.

        :return: Formatted string as "<rank><suit>"
        """
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        """
        Formal string representation of the Card.

        :return: Same as __str__
        """
        return self.__str__()

    @property
    def suit(self):
        """
        Suit getter method.

        :return: Suit of the card
        """
        return self._suit

    @property
    def rank(self):
        """
        Rank getter method.

        :return: Rank of the card
        """
        return self._rank


class Deck:
    """
    A class representing a full deck of 52 playing cards.
    """

    def __init__(self):
        """
        Initialize the Deck by creating one Card of each combination of suit and rank.
        """
        self._deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._deck.append(Card(suit, rank))

    def __str__(self):
        """
        String representation of the deck.

        :return: List of all cards as a string
        """
        return str(self._deck)

    def shuffle(self):
        """
        Shuffle the deck randomly in place.
        """
        random.shuffle(self._deck)

    def deal(self):
        """
        Deal (remove and return) the top card from the deck.

        :return: A Card object
        """
        return self._deck.pop(0)


if __name__ == "__main__":
    # Create and print a new unshuffled deck
    deck = Deck()
    print(deck)

    # Shuffle the deck and print again
    deck.shuffle()
    print(deck)

    # Deal (remove) the top card and print it
    print(deck.deal())
