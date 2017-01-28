#!/usr/bin/env python

import json

input_file = "raw/AllCards-x.json"

with open(input_file, "r") as f:
    cards = json.load(f)

fields = ["types","subtypes","supertypes","layout"]
field_sets = {}
for field in fields:
    field_sets[field] = set()

for cardname in cards:
    card = cards[cardname]
    if "Ever" in card.get("types",[]):
        print(cardname)
    for field in fields:
        if field in card:
            field_sets[field].update(card[field])

for field in field_sets:
    print("Field: {field}".format(field=field))
    for value in field_sets[field]:
        print("  {value}".format(value=value.encode('utf-8')))
#     print("")
