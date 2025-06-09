from deck import Deck, Card

class PokerHand:
    """
    Represents a 5-card poker hand drawn from a deck.
    Provides properties to detect hand types like flush, straight, full house, etc.
    """

    def __init__(self, deck):
        """
        Draw 5 cards from the deck to form a hand.

        :param deck: Deck object to draw cards from
        """
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        """
        Returns the list of 5 Card objects in the hand.
        """
        return self._cards

    def __str__(self):
        """
        String representation of the PokerHand.

        :return: List of cards as a string
        """
        return str(self.cards)

    @property
    def is_flush(self):
        """
        Check if all cards have the same suit.

        :return: True if hand is a flush, False otherwise
        """
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def is_full_house(self):
        """
        Check if hand is a full house (3 of one rank and 2 of another).

        :return: True if full house, based on match count of 8
        """
        return self.number_matches == 8

    @property
    def number_matches(self):
        """
        Calculate the number of matching rank comparisons in the hand.

        :return: Total number of duplicate rank matches among cards
        """
        matches = 0
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        Check if hand contains exactly one pair.

        :return: True if one pair, False otherwise
        """
        return self.number_matches == 2

    @property
    def is_two_pair(self):
        """
        Check if hand contains exactly two pairs.

        :return: True if two pairs, False otherwise
        """
        return self.number_matches == 4

    @property
    def is_trips(self):
        """
        Check if hand contains exactly three of a kind.

        :return: True if three of a kind, False otherwise
        """
        return self.number_matches == 6

    @property
    def is_quads(self):
        """
        Check if hand contains four of a kind.

        :return: True if four of a kind, False otherwise
        """
        return self.number_matches == 12

    @property
    def is_straight(self):
        """
        Check if hand contains 5 cards in sequential rank order.

        :return: True if straight, False otherwise
        """
        self.cards.sort()
        distance = Card.RANKS.index(self.cards[4].rank) - \
                   Card.RANKS.index(self.cards[0].rank)
        return self.number_matches == 0 and distance == 4


# Simulation to estimate the probability of drawing a straight

count = 0       # total number of hands simulated
matches = 0     # number of hands that were straights

while matches < 100:
    deck = Deck()
    # deck._deck = deck._deck[:13]  # uncomment to limit deck (cheat)
    deck.shuffle()
    hand = PokerHand(deck)

    # Uncomment to debug hand details:
    # print("unsorted hand")
    # print(hand)
    # hand.cards.sort()
    # print("sorted hand")
    # print(hand)

    if hand.is_straight:
        matches += 1
        # print(hand)  # show matched hands

    count += 1

# Print estimated probability of getting a straight in poker
print(f"probability of  straight is {100 * matches / count}%")
