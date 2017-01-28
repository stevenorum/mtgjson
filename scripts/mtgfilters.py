#!/usr/bin/env python

def unset_card(card):
    legalities = card.get("legalities",[])
    if not legalities:
        return False
    if legalities[0]["format"] == "Un-Sets" and legalities[0]["legality"] == "Legal":
        return True
    return False

def remove_unsets(cards):
     return { cardname:cards[cardname] for cardname in cards if not unset_card(cards[cardname])}
