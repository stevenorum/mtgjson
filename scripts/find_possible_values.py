#!/usr/bin/env python

import json
import mtgfilters

input_file = "raw/AllCards-x.json"

with open(input_file, "r") as f:
    cards = mtgfilters.remove_unsets(json.load(f))

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
            value = card[field]
            if isinstance(value, basestring):
                field_sets[field].add(value)
            else:
                field_sets[field].update(value)

for field in field_sets:
    print("Field: {field}".format(field=field))
    for value in field_sets[field]:
        print("  {value}".format(value=value.encode('utf-8')))
#     print("")
