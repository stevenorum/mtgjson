#!/usr/bin/env python

import json
import mtgfilters
import os
import sys

input_file = "raw/AllCards-x.json"
output_directory = "by_type"

with open(input_file, "r") as f:
    cards = mtgfilters.remove_unsets(json.load(f))

notype_count = 0
type_count = 0
types = {}
for cardname in cards:
    card = cards[cardname]
    if "types" in card:
        for type in card["types"]:
            by_type = types.get(type, [])
            by_type.append(card)
            types[type] = by_type
        type_count += 1
    else:
        print("Card {cardname} has no types.".format(cardname=cardname.encode('utf-8')))
        notype_count += 1

print("Type count: " + str(type_count))
print("No-Type count: " + str(notype_count))

for type in types:
    filename = os.path.join(output_directory, "{type}.json".format(type=type))
    with open(filename, "w") as f:
        json.dump(types[type], f, indent=2, sort_keys=True)
