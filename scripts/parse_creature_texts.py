#!/usr/bin/env python

import json
import mtgfilters
import os
import parser
import sys

input_file = "by_type/Creature.json"
output_directory = "random"

with open(input_file, "r") as f:
    cards = json.load(f)

texts = {}

successful = 0

for card in cards:
    text = card.get("text", "")
    parsed, remainder = parser.parse_creature_text(text)
    successful += 0 if remainder else 1
    texts[card["name"]] = {"raw":text, "parsed":parsed, "remainder":remainder}

filename = os.path.join(output_directory, "parsed_creature_texts.json")
with open(filename, "w") as f:
        json.dump(texts, f, indent=2, sort_keys=True)
print(successful)
