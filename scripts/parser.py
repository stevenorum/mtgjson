#!/usr/bin/env python

KEYWORDS={
"Flying":"FLYING",
"Trample":"TRAMPLE",
"Vigilance":"VIGILANCE"
}

def parse_creature_text(text):
    # Yes, this is hilariously basic and shitty and that's fine for testing the framework.
    if text in KEYWORDS:
        return KEYWORDS[text], ""
    return "", text
