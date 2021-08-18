# -*- coding: utf-8 -*-

import re
from collections import Counter

import pointofview

from prosegrinder.dictionary import Dictionary
from prosegrinder.word import Word


class Fragment(object):

    def __init__(self, text, dictionary=Dictionary()):
        self.text = text
        self.dictionary = dictionary
        self.normalized_sentence = dictionary.normalize_text(text)
        self.words = [self.dictionary.get_word(word) for word in re.findall(
            Word.RE_WORD, self.normalized_sentence)]
        self.word_count = len(self.words)
        self.word_character_count = sum(
            [word.character_count for word in self.words])
        pf = Counter()
        pc = 0
        for word in self.words:
            pf.update(word.phone_frequency)
            pc += word.phone_count
        self.phone_frequency = pf
        self.phone_count = pc
        self.syllable_count = sum(
            [word.syllable_count for word in self.words])
        self.complex_word_count = sum(
            [word.is_complex_word for word in self.words])
        self.long_word_count = sum(
            [word.is_long_word for word in self.words])
        self.pov_word_count = sum([word.is_pov_word for word in self.words])
        self.first_person_word_count = sum(
            [word.is_first_person_word for word in self.words])
        self.second_person_word_count = sum(
            [word.is_second_person_word for word in self.words])
        self.third_person_word_count = sum(
            [word.is_third_person_word for word in self.words])
        self.word_frequency = dict(Counter(self.words))
        self.unique_words = self.word_frequency.keys()
        self.unique_word_count = len(self.unique_words)
        self.pov = pointofview.NONE
        if self.first_person_word_count > 0:
            self.pov = pointofview.FIRST
        elif self.second_person_word_count > 0:
            self.pov = pointofview.SECOND
        elif self.third_person_word_count > 0:
            self.pov = pointofview.THIRD

    def __eq__(self, other):
        return self.text == other.text

    def __hash__(self):
        return hash(self.text)

    # @property
    # def dictionary(self):
    #     return self.dictionary

    # @property
    # def word_count(self):
    #     return self.word_count

    # @property
    # def word_character_count(self):
    #     return self.word_character_count

    # @property
    # def phone_frequency(self):
    #     return self.phone_fequency

    # @property
    # def phone_count(self):
    #     return self.phone_count

    # @property
    # def syllable_count(self):
    #     return self.syllable_count

    # @property
    # def complex_word_count(self):
    #     return self.complex_word_count

    # @property
    # def long_word_count(self):
    #     return self.long_word_count

    # @property
    # def unique_words(self):
    #     return self.word_frequency.keys()

    # @property
    # def word_frequency(self):
    #     return self.word_frequency

    # @property
    # def pov_word_count(self):
    #     return self.pov_word_count

    # @property
    # def text(self):
    #     return self.text

    def frequency(self, word_string):
        return self.word_frequency[word_string]

    # @property
    # def first_person_word_count(self):
    #     return self.first_person_word_count

    # @property
    # def second_person_word_count(self):
    #     return self.second_person_word_count

    # @property
    # def third_person_word_count(self):
    #     return self.third_person_word_count

    # @property
    # def words(self):
    #     return self.words

    # @property
    # def pov(self):
    #     return self.pov
