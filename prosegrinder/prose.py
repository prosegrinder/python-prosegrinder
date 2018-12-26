# -*- coding: utf-8 -*-

from collections import Counter

import narrative

from prosegrinder.dictionary import Dictionary
from prosegrinder.fragment import Fragment
from prosegrinder.fragment_container import FragmentContainer
from prosegrinder.paragraph import Paragraph
from prosegrinder.readability_scores import ReadabilityScores


class Prose():

    def __init__(self, text, dictionary=Dictionary()):
        self._text = text
        self._dictionary = dictionary
        self._paragraphs = Paragraph.parse_paragraphs(
            self._text, self._dictionary)
        self._word_character_count = sum(
            [paragraph.word_character_count for paragraph in self._paragraphs])
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
            self._word_character_count, self._syllable_count, self._word_count,
            self._complex_word_count, self._long_word_count, self._sentence_count)
        n = narrative.split(self._text)
        self._dialogue = FragmentContainer(
            [Fragment(fragment_text) for fragment_text in n['dialogue']])
        self._narrative = FragmentContainer(
            [Fragment(fragment_text) for fragment_text in n['narrative']])
        self._pov = self._narrative.pov

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
    def word_character_count(self):
        return self._word_character_count

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

    @property
    def pov(self):
        return self._pov

    @property
    def text(self):
        return self._text
