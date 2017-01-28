#!/usr/bin/env python

import json

input_file = "raw/AllSets.json"

with open(input_file, "r") as f:
    cards = json.load(f)
keys = [k for k in cards]
keys.sort()
for key in keys:
    print(key)
