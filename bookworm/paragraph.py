# -*- coding: utf-8 -*-

import re
from collections import Counter

from bookworm.sentence import Sentence


class Paragraph():

    RE_PARAGRAPH = re.compile(".*(?=\\n|$)")

    def __init__(self, paragraph_string, dictionary):
        self._paragraph_string = paragraph_string
        self._dictionary = dictionary
        self._sentences = [sentence for sentence in re.findall(
            Sentence.RE_SENTENCE, self._paragraph_string)]
        self._word_count = sum([sentence.word_count()
                                for sentence in self._sentences])
        self._character_count = sum(
            [sentence.character_count() for sentence in self._sentences])
        self._syllable_count = sum(
            [sentence.syllable_count() for sentence in self._sentences])
        self._complex_word_count = sum(
            [sentence.complex_word_count() for sentence in self._sentences])
        self._long_word_count = sum(
            [sentence.long_word_count() for sentence in self._sentences])
        self._pov_word_count = sum(
            [sentence.pov_word_count() for sentence in self._sentences])
        self._first_person_word_count = sum(
            [sentence.first_person_word_count() for sentence in self._sentences])
        self._second_person_word_count = sum(
            [sentence.second_person_word_count() for sentence in self._sentences])
        self._third_person_word_count = sum(
            [sentence.third_person_word_count() for sentence in self._sentences])
        self._word_frequency = sum(
            [sentence.word_frequency() for sentence in self._sentences])

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self._paragraph_string == other._paragraph_string

    def __hash__(self):
        return hash(self._paragraph_string)

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
    def paragraph_string(self):
        return self._paragraph_string

    @property
    def frequency(self, word_string):
        return self._word_frequency[word_string]
