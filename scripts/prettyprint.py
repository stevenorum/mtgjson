#!/usr/bin/env python

import json
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r") as f:
    content = json.load(f)
with open(output_file, "w") as f:
    json.dump(content, f, indent=2, sort_keys=True)
