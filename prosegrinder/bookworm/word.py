# -*- coding: utf-8 -*-

import re

class Word:
    """A Word, the base unit for measuring fiction prose."""

    MIN_SYLLABLES_COMPLEX_WORD = 3
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

    def __init__(self, word_string, syllable_count, is_dictionary_word, is_numeric):
        self.initial_word = word_string
        self.syllable_count = syllable_count
        self.is_dictionary_word = is_dictionary_word
        self.is_numeric = is_numeric
        self.normalized_word = word_string.strip().lower()
        self.character_count = len(self.normalized_word)

    def is_complex_word(self):
        return self.syllable_count >= self.MIN_SYLLABLES_COMPLEX_WORD

    def is_long_word(self):
        return self.character_count >= self.MIN_CHARS_LONG_WORD

    def is_first_person_word(self):
        return self.normalized_word in self.POV_FIRST

    def is_second_person_word(self):
        return self.normalized_word in self.POV_SECOND

    def is_third_person_word(self):
        return self.normalized_word in self.POV_THIRD

    def is_pov_word(self):
        return (self.is_first_person_word or
                self.is_second_person_word or
                self.is_third_person_word)
