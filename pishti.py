# pishti.py
import itertools
from game import *

"""
=========================================
For my late grandfather, Turgut Erdemli,
who taught me this game when I was young.
=========================================
"""

def main():
    """
    Runs the game.
    """
    draw_deck = Game.deck_maker()
    num_players = Game.get_player_number()
    player_list: list[Player] = Game.create_players(num_players)
    final_empty_hands: int = 0
    temp_empty_hands: int = 0
    print(player_list)
    first_deal: list[Card] = Game.hidden_deal(draw_deck)
    stack_deck: list[Card] = first_deal[0]
    draw_deck: list[Card] = first_deal[1]
    for num in range(0, num_players):
        gen_deal = Game.deal(draw_deck)
        player_list[num].player_deck = gen_deal[0]
        draw_deck = gen_deal[1]
    for player in itertools.cycle(player_list):
        print("===================================")
        print("Stack deck is:")
        print(stack_deck)
        card = player.play()
        stack_deck.append(card)
        if (len(stack_deck) != 1):
            if (stack_deck[-2].compare(stack_deck[-1])):
                Game.collect(Game, player, stack_deck)
                last_collector = player
                stack_deck = []
        if (len(player.player_deck) == 0):
            temp_empty_hands += 1
        if (len(draw_deck) == 0):
            if (len(player.player_deck) == 0):
                final_empty_hands += 1
            if (final_empty_hands == num_players):
                if (len(stack_deck) != 0):
                    print("===================================")
                    print("Last collector is: " + last_collector.name)
                    Game.collect(Game, last_collector, stack_deck)
                break
            continue
        if (final_empty_hands != num_players):
            if (temp_empty_hands == num_players):
                temp_empty_hands = 0
                print("===================================")
                print("Redealing for everyone.")
                for num in range(0, num_players):
                    gen_deal = Game.deal(draw_deck)
                    player_list[num].player_deck = gen_deal[0]
                    draw_deck = gen_deal[1]
    for player in player_list:
        Game.scoring(player, num_players)
        print(player.name + "'s collected is: " + str(player.player_collect))
        print(player.name + "'s number of pishtis are: " + str(player.pishtis))
        print(player.name + "'s final score is: " + str(player.score))

if __name__ == "__main__":
    main()