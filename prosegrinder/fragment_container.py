# -*- coding: utf-8 -*-

from collections import Counter

import pointofview

from prosegrinder.dictionary import Dictionary


class FragmentContainer(object):

    def __init__(self, fragments, dictionary=Dictionary()):
        self.dictionary = dictionary
        self.fragments = fragments or []
        self.fragment_count = len(self.fragments)
        self.word_count = sum(
            [fragment.word_count for fragment in self.fragments])
        self.word_character_count = sum(
            [fragment.word_character_count for fragment in self.fragments])
        self.syllable_count = sum(
            [fragment.syllable_count for fragment in self.fragments])
        self.complex_word_count = sum(
            [fragment.complex_word_count for fragment in self.fragments])
        self.long_word_count = sum(
            [fragment.long_word_count for fragment in self.fragments])
        self.pov_word_count = sum(
            [fragment.pov_word_count for fragment in self.fragments])
        self.first_person_word_count = sum(
            [fragment.first_person_word_count for fragment in self.fragments])
        self.second_person_word_count = sum(
            [fragment.second_person_word_count for fragment in self.fragments])
        self.third_person_word_count = sum(
            [fragment.third_person_word_count for fragment in self.fragments])
        wf = Counter()
        pf = Counter()
        pc = 0
        for fragment in self.fragments:
            wf.update(fragment.words)
            pf.update(fragment.phone_frequency)
            pc += fragment.phone_count
        self.word_frequency = dict(wf)
        self.phone_frequency = dict(pf)
        self.phone_count = pc
        self.unique_words = self.word_frequency.keys()
        self.unique_word_count = len(self.unique_words)
        if (self.first_person_word_count > 0):
            self.pov = pointofview.FIRST
        elif (self.second_person_word_count > 0):
            self.pov = pointofview.SECOND
        elif (self.third_person_word_count > 0):
            self.pov = pointofview.THIRD
        else:
            self.pov = pointofview.NONE

    def __eq__(self, other):
        return self.fragments == other.fragments

    def __hash__(self):
        return hash(self.fragments)

    # @property
    # def dictionary(self):
    #     return self.dictionary

    # @property
    # def phone_frequency(self):
    #     return self.phone_frequency

    # @property
    # def phone_count(self):
    #     return self.phone_count

    # @property
    # def word_count(self):
    #     return self.word_count

    # @property
    # def word_character_count(self):
    #     return self.word_character_count

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
    # def unique_word_count(self):
    #     return len(self.unique_words)

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
    # def fragments(self):
    #     return self.fragments

    def frequency(self, word_string):
        return self.word_frequency[self.dictionary.get_word(word_string)]

    # @property
    # def fragment_count(self):
    #     return len(self.fragments)

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
    # def pov(self):
    #     return self.pov
