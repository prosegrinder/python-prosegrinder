# -*- coding: utf-8 -*-

import re
from collections import Counter

from bookworm.word import Word


class Sentence():

    RE_SENTENCE = re.compile("""
            # Match a sentence ending in punctuation or EOS.
            [^.!?…\\s]        # First char is non-punct, non-ws
            [^.!?…]*          # Greedily consume up to punctuation.
            (?:               # Group for unrolling the loop.
            [.!?…]            # (special) inner punctuation ok if
            (?!['\")]?\\s|$)  # not followed by ws or EOS.
            [^.!?…]*          # Greedily consume up to punctuation.
            )*                # Zero or more (special normal*)
            [.!?…]            # Ending punctuation.
            ['\")]?          # Optional closing quote.
            (?=\\s|$)
            """,
                                  flags=re.MULTILINE | re.VERBOSE)

    RE_SMART_QUOTES = re.compile("[“”]")

    def __init__(self, sentence, dictionary):
        self._sentence_string = sentence
        self._normalized_sentence = dictionary.normalize_text(sentence)
        self._dictionary = dictionary
        self._words = [self._dictionary.get_word(
            word) for word in re.findall(Word.RE_WORD, self._normalized_sentence)]
        self._word_count = len(self._words)
        self._character_count = sum(
            [word.character_count for word in self._words])
        self._syllable_count = sum(
            [word.syllable_count for word in self._words])
        self._complex_word_count = sum(
            [1 if word.is_complex_word else 0 for word in self._words])
        self._long_word_count = sum(
            [1 if word.is_long_word else 0 for word in self._words])
        self._pov_word_count = sum(
            [1 if word.is_pov_word else 0 for word in self._words])
        self._first_person_word_count = sum(
            [1 if word.is_first_person_word else 0 for word in self._words])
        self._second_person_word_count = sum(
            [1 if word.is_second_person_word else 0 for word in self._words])
        self._third_person_word_count = sum(
            [1 if word.is_third_person_word else 0 for word in self._words])
        self._word_frequency = Counter(self._words)

    @property
    def word_count(self):
        return self._word_count

    @property
    def character_count(self):
        return self._character_count

    @property
    def syllable_count(self):
        return self._syllable_count

    @property
    def complex_word_count(self):
        return self._complex_word_count

    @property
    def long_word_count(self):
        return self._long_word_count

    @property
    def unique_words(self):
        return self._word_frequency.keys()

    @property
    def word_frequency(self):
        return self._word_frequency

    @property
    def pov_word_count(self):
        return self._pov_word_count

    @property
    def sentence_string(self):
        return self._sentence_string

    @property
    def frequency(self, word):
        return self._word_frequency[word]
