# -*- coding: utf-8 -*-

import re
from collections import Counter

from prosegrinder.dictionary import Dictionary
from prosegrinder.paragraph import Paragraph
from prosegrinder.readability_scores import ReadabilityScores
import narrative


class Prose():

    def __init__(self, prose_string, dictionary=None):
        self._prose_string = prose_string
        self._dictionary = dictionary if dictionary else Dictionary()
        self._paragraphs = [Paragraph(paragraph, self._dictionary) for paragraph in re.findall(
            Paragraph.RE_PARAGRAPH, self._prose_string)]
        n = narrative.split(prose_string)
        self._dialogue = [frag != '' for frag in n['dialogue']]
        self._narrative = [frag != '' for frag in n['narrative']]
        self._character_count = sum(
            [paragraph.character_count for paragraph in self._paragraphs])
        self._syllable_count = sum(
            [paragraph.syllable_count for paragraph in self._paragraphs])
        self._word_count = sum(
            [paragraph.word_count for paragraph in self._paragraphs])
        self._complex_word_count = sum(
            [paragraph.complex_word_count for paragraph in self._paragraphs])
        self._long_word_count = sum(
            [paragraph.long_word_count for paragraph in self._paragraphs])
        self._pov_word_count = sum(
            [paragraph.pov_word_count for paragraph in self._paragraphs])
        self._first_person_word_count = sum(
            [paragraph.first_person_word_count for paragraph in self._paragraphs])
        self._second_person_word_count = sum(
            [paragraph.second_person_word_count for paragraph in self._paragraphs])
        self._third_person_word_count = sum(
            [paragraph.third_person_word_count for paragraph in self._paragraphs])
        wf = Counter()
        for paragraph in self._paragraphs:
            wf.update(paragraph.word_frequency)
        self._word_frequency = dict(wf)
        self._sentence_count = sum(
            [paragraph.sentence_count for paragraph in self._paragraphs])
        self._paragraph_count = len(self._paragraphs)
        self._readability_scores = ReadabilityScores(
            self._character_count, self._syllable_count, self._word_count,
            self._complex_word_count, self._long_word_count, self._sentence_count)

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self._prose_string == other._prose_string

    def __hash__(self):
        return hash(self._prose_string)

    @property
    def character_count(self):
        return self._character_count

    @property
    def syllable_count(self):
        return self._syllable_count

    @property
    def word_count(self):
        return self._word_count

    @property
    def complex_word_count(self):
        return self._complex_word_count

    @property
    def long_word_count(self):
        return self._long_word_count

    @property
    def unique_word_count(self):
        return len(self._word_frequency)

    @property
    def pov_word_count(self):
        return self._pov_word_count

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
    def sentence_count(self):
        return self._sentence_count

    @property
    def paragrah_count(self):
        return self._paragraph_count

    @property
    def readability_scores(self):
        return self._readability_scores

    @property
    def dialogue(self):
        return self._dialogue

    @property
    def narrative(self):
        return self._narrative
