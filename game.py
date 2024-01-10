#game.py
import random
from card import *
from player import *
from constants import *

class Game():
    """
    Currently, the Game is just a collection of functions utilized in Pishti.
    Future versions, which might implement the "round mechanic" might create
    instances of this class.
    """
    def deck_maker() -> list[Card]:
        """
        Uses the list of legal cards to create each card as an
        instance of the card class.
        Returns:
            list[Card]:
                All the legal cards as instances of the card class.
        """
        draw_deck = []
        for name, info in RANKS_AND_SUITS.items():
            draw_deck.append(Card(name, info[0], info[1], False))
        random.shuffle(draw_deck)
        return draw_deck
    
    def deal ( draw_deck: list[Card] ) -> tuple[list[Card], list[Card]]:
        """
        Deals 4 cards to a player after everyone's hands have
        been emptied.
        Parameters:
            draw_deck ( list[Card] ):
                The deck the cards are drawn from.
        Returns:
            tuple[list[Card], list[Card]]]:
            The first list contains the cards dealt to each player.
            The second list contains the cards left on the draw pile.
        """
        dealed = draw_deck[-4:]
        draw_deck = draw_deck[:-4]
        return (dealed, draw_deck)
    
    def hidden_deal ( draw_deck: list[Card] ) -> tuple[list[Card], list[Card]]:
        """
        Deals 4 cards to the middle stack at the start of the game.
        Parameters:
            draw_deck ( list[Card] ):
                The deck the cards are drawn from.
        Returns:
            tuple[list[Card], list[Card]]]:
            The first list contains the cards dealt to the middle stack. The
            first three cards are hidden to give the collector strategic advantage.
            The second list contains the cards left on the draw pile.
        """
        dealed = list(reversed(draw_deck[-4:]))
        draw_deck = draw_deck[:-4]
        dealed[0].hide()
        dealed[1].hide()
        dealed[2].hide()
        return (dealed, draw_deck)
    
    def collect ( self, player: Player, stack_deck: list[Card] ) -> None:
        """
        Empties the middle stack and adds it to the personal collection of a player.
        Parameters:
            player ( Player ):
                The player who collects the pile.
            stack_deck ( list[Card] ):
                The middle stack the player collects.
        """
        if (self.pishti_checker(stack_deck)):
            print("PISHTI!")
            player.pishtis += 1
        for card in stack_deck:
            card.reveal()
            player.player_collect.append(card)
        stack_deck = []
        return None

    def pishti_checker ( stack_deck: list[Card] ) -> bool:
        """
        Checks whether the collected pile counts towards a Pishti.
        (The pile has a single card and collecting card is not a Jack.)
        Parameters:
            stack_deck ( list[Card] ):
                The middle stack deck that is being collected.
        """
        if len(stack_deck) == 2:
            if stack_deck[-1].value != 11:
                return True
            else:
                return False
        else:
            return False

    def get_player_number () -> int:
        """
        Collects the number of players.
        Returns:
            int:
                The number of players in the game.
        """
        while True:
            while True:
                try:
                    num_players = int(input("How many players will play this game? (2 - 4)\n"))
                    break
                except ValueError:
                    print("Please enter a number.")
            if (num_players > 1 and num_players < 5):
                break
            else:
                print("Please submit an appropriate number.")
        return num_players
    
    def create_players ( players: int ) -> list[Player]:
        """
        Creates the instances of players for the range of 2 to 4.
        Parameters:
            players ( int ): Number of players
        Returns:
            list[Player]:
                A list containing all the player instances.
        """
        player_list: list[Player] = []
        for i in range(0, players):
            name = str(input("Player " + str(i + 1) + " please enter your name.\n"))
            player_list.append(Player(name))
        return player_list
    
    def scoring ( player: Player, num_players: int ) -> None:
        """
        Scores each players' collected deck.
        Parameters:
            player ( Player ):
                A player.
            num_players ( int ):
                The number of players in the game.
        """
        player.score += player.pishtis * 10
        if len(player.player_collect) > (52/num_players):
            player.score += 3
        for card in player.player_collect:
            if (card.value == 10) & (card.suit == "DIAMONDS"):
                player.score += 3
            if (card.value == 2) & (card.suit == "CLUBS"):
                player.score += 2
            if (card.value == 11) | (card.value == 1):
                player.score += 1
        return None