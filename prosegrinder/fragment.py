# -*- coding: utf-8 -*-

import re
from collections import Counter

import pointofview

from prosegrinder.dictionary import Dictionary
from prosegrinder.word import Word


class Fragment():

    def __init__(self, text, dictionary=Dictionary()):
        self._text = text
        self._dictionary = dictionary
        self._normalized_sentence = dictionary.normalize_text(text)
        self._words = [self._dictionary.get_word(word) for word in re.findall(
            Word.RE_WORD, self._normalized_sentence)]
        self._word_count = len(self._words)
        self._word_character_count = sum(
            [word.character_count for word in self._words])
        self._syllable_count = sum(
            [word.syllable_count for word in self._words])
        self._complex_word_count = sum(
            [word.is_complex_word for word in self._words])
        self._long_word_count = sum(
            [word.is_long_word for word in self._words])
        self._pov_word_count = sum([word.is_pov_word for word in self._words])
        self._first_person_word_count = sum(
            [word.is_first_person_word for word in self._words])
        self._second_person_word_count = sum(
            [word.is_second_person_word for word in self._words])
        self._third_person_word_count = sum(
            [word.is_third_person_word for word in self._words])
        self._word_frequency = dict(Counter(self._words))
        self._pov = pointofview.NONE
        if self._first_person_word_count > 0:
            self._pov = pointofview.FIRST
        elif self._second_person_word_count > 0:
            self._pov = pointofview.SECOND
        elif self._third_person_word_count > 0:
            self._pov = pointofview.THIRD

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self._text == other._text

    def __hash__(self):
        return hash(self._text)

    @property
    def dictionary(self):
        return self._dictionary

    @property
    def word_count(self):
        return self._word_count

    @property
    def word_character_count(self):
        return self._word_character_count

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
    def text(self):
        return self._text

    @property
    def frequency(self, word_string):
        return self._word_frequency[word_string]

    @property
    def first_person_word_count(self):
        return self._first_person_word_count

    @property
    def second_person_word_count(self):
        return self._second_person_word_count

    @property
    def third_person_word_count(self):
        return self._third_person_word_count

    @property
    def words(self):
        return self._words

    @property
    def pov(self):
        return self._pov
