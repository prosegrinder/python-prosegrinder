# -*- coding: utf-8 -*-

import re

class Word:
    """A Word, the base unit for measuring fiction prose."""

    MIN_CHARS_LONG_WORD = 7
    POV_FIRST = ["i", "i'm", "i'll", "i'd", "i've", "me", "mine", "myself",
                 "we", "we're", "we'll", "we'd", "we've", "us", "ours", "ourselves"]
    POV_SECOND = ["you", "you're", "you'll", "you'd", "you've", "your", "yours",
                  "yourself", "yourselves"]
    POV_THIRD = ["he", "he's", "he'll", "he'd", "him", "his", "himself", "she", "she's",
                 "she'll", "she'd", "her", "hers", "herself", "it", "it's", "it'll", "it'd",
                 "itself", "they", "they're", "they'll", "they'd", "they've", "them",
                 "theirs", "themselves"]
    WORD_PATTERN = re.compile("[\\w’']+")

    def __init__(self, wordString, syllableCount, inDictionary, isNumeric):
        self.wordString = wordString
        self.syllableCount = syllableCount
        self.inDictionary = inDictionary
        self.isNumeric = isNumeric
