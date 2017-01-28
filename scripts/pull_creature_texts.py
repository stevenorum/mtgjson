#!/usr/bin/env python

import json
import mtgfilters
import os
import sys

input_file = "by_type/Creature.json"
output_directory = "random"

with open(input_file, "r") as f:
    cards = json.load(f)

texts = {}

for card in cards:
    texts[card["name"]] = card.get("text", "")

filename = os.path.join(output_directory, "creature_texts.json")
with open(filename, "w") as f:
        json.dump(texts, f, indent=2, sort_keys=True)
