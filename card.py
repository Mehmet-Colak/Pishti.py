#card.py
class Card():
    """
    The Card is the custom class used in Pishti.
    Collecting cards is the goal of the game.
    """

    def __init__( self, name: str, suit : str, value : int, hidden : bool):
        """
        Creating an instance of a card.
        Parameters:
            name ( str ):
                The name that will appear as a string.
            suit ( str ):
                The suit of the card.
            value ( int ):
                The number of the card. Jack is 11, Queen is 12, King is 13.
            hidden ( bool ):
                Whether or not the name of the card is visible as a string.
        """
        self.name: str = name
        self.suit: str = suit
        self.value: int = value
        self.hidden: bool = hidden

    def hide ( self ) -> None:
        "Makes the card's string into '----.'"
        self.hidden = True
    
    def reveal ( self ) -> None:
        "Turns the card's string back to its original name."
        self.hidden = False

    def compare ( self, other: "Card" ) -> bool:
        """
        Compares the two cards to see whether the player collects.
        A card is only collected if the top card is the same value
        as the card below or if the card on top is a Jack.
        Parameters:
            other ( Card ):
                The card on top, whose value is checked.
        Returns:
            bool:
                Whether or not the card is collected.
        """
        if other.value == 11:
            return True
        if self.value == other.value:
            return True
        else:
            return False

    def __str__( self ) -> str:
        "toStringmethod of the card."
        if self.hidden:
            return("----")
        else:
            return self.name    

    def __repr__( self ) -> str:
        "toStringmethod of the card in a given list."
        if self.hidden:
            return("----")
        else:
            return self.__str__()