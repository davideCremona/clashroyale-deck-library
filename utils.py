#!/usr/bin/python3

# ===================================================================
#    IMPORT SECTION
# ===================================================================
import os
import json
from datetime import datetime


# ===================================================================
#    FUNCTION DEFINITION
# ===================================================================

def get_timestamp():
    return datetime.now().strftime("%m/%d/%Y-%H:%M:%S")


def maybe_create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def get_cards_path():
    return "data/cards.json"


def get_decks_path():
    return "data/decks.json"


def get_cards_dict():
    cards_dict = {}
    if os.path.exists(get_cards_path()):
        cards_dict = json.load(open(get_cards_path(), 'r'))
    return cards_dict


def get_decks_dict():
    decks_dict = {}
    if os.path.exists(get_decks_path()):
        decks_dict = json.load(open(get_decks_path(), 'r'))
    return decks_dict


def update_all_cards(new_cards):
    maybe_create_dir("data")
    cards_dict = {'update_time': get_timestamp()}
    for card in new_cards:
        cards_dict[card['name']] = {
            'id': card['id'],
            'maxLevel': card['maxLevel'],
            'icon': card['iconUrls']['medium']
        }
    json.dump(cards_dict, open(os.path.join("data", "cards.json"), 'w'))


# ===================================================================
#    CLASS DEFINITION
# ===================================================================

# ===================================================================
#    START OF PROGRAM
# ===================================================================
if __name__ == '__main__':
    pass
