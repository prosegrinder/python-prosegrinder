# -*- coding: utf-8 -*-

from collections import Counter

import pointofview

from prosegrinder.dictionary import Dictionary


class FragmentContainer():

    def __init__(self, fragments, dictionary=Dictionary()):
        self._dictionary = dictionary
        self._fragments = fragments or []
        self._word_count = sum(
            [fragment.word_count for fragment in self._fragments])
        self._word_character_count = sum(
            [fragment.word_character_count for fragment in self._fragments])
        self._syllable_count = sum(
            [fragment.syllable_count for fragment in self._fragments])
        self._complex_word_count = sum(
            [fragment.complex_word_count for fragment in self._fragments])
        self._long_word_count = sum(
            [fragment.long_word_count for fragment in self._fragments])
        self._pov_word_count = sum(
            [fragment.pov_word_count for fragment in self._fragments])
        self._first_person_word_count = sum(
            [fragment.first_person_word_count for fragment in self._fragments])
        self._second_person_word_count = sum(
            [fragment.second_person_word_count for fragment in self._fragments])
        self._third_person_word_count = sum(
            [fragment.third_person_word_count for fragment in self._fragments])
        wf = Counter()
        for fragment in self._fragments:
            wf.update(fragment.words)
        self._word_frequency = dict(wf)
        self._pov = pointofview.NONE
        if (self._first_person_word_count > 0):
            self._pov = pointofview.FIRST
        elif (self._second_person_word_count > 0):
            self._pov = pointofview.SECOND
        elif (self._third_person_word_count > 0):
            self._pov = pointofview.THIRD

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self._fragments == other._fragments

    def __hash__(self):
        return hash(self._fragments)

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
    def unique_word_count(self):
        return len(self.unique_words)

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
    def fragments(self):
        return self._fragments

    @property
    def frequency(self, word_string):
        return self._word_frequency[self._dictionary.get_word(word_string)]

    @property
    def fragment_count(self):
        return len(self._fragments)

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
    def pov(self):
        return self._pov
