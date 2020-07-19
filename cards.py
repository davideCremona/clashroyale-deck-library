#!/usr/bin/python3

# ===================================================================
#    IMPORT SECTION
# ===================================================================
import utils
import copy


# ===================================================================
#    FUNCTION DEFINITION
# ===================================================================

def get_card_by_name(card_name):
    return cards_db[card_name]


def get_deck_by_id(deck_id):
    deck = copy.deepcopy(decks_db['decks'][deck_id])
    deck['cards'] = [get_card_by_name(c) for c in deck['cards']]
    return deck


# ===================================================================
#    CLASS DEFINITION
# ===================================================================

cards_db = utils.get_cards_dict()
decks_db = utils.get_decks_dict()

# ===================================================================
#    START OF PROGRAM
# ===================================================================
if __name__ == '__main__':
    pass
