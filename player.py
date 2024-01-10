#player.py
from card import *

class Player():
    """
    The Players are the users of the program.
    This program enables the use of 2 to 4 players.
    """
    def __init__( self, name: str ):
        """
        Creating instance of a player.
        Parameters:
            name ( str ):
                The unique name chosen by the player.
        """
        self.name: str = name
        self.player_collect: list[Card] = []
        self.player_deck: list[Card] = []
        self.pishtis: int = 0
        self.score: int = 0
    
    def play ( self ) -> Card:
        """
        Letting the player choose a card from their deck.
        Return:
            Card:
                The card played by the player.
        """
        print(self.name + ", your cards are:")
        print(self.player_deck)
        num_of_cards = len(self.player_deck)
        while True:
            while True:
                try:
                    card_index = int(input("Which index will you play? (1 - " + str(num_of_cards) + ")\n"))
                    break
                except ValueError:
                    print("Please enter a number.")
            if (card_index > 0 and card_index < (num_of_cards + 1)):
                break
            else:
                print("Invalid index, please try again.")
        removed_card = self.player_deck.pop(card_index - 1)
        return removed_card

    def __str__( self ) -> str:
        "toString method of the player."
        return self.name    

    def __repr__( self ) -> str:
        "toString method of the player in a given list."
        return self.__str__()