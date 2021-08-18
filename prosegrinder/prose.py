# -*- coding: utf-8 -*-

from collections import Counter
import hashlib

import narrative

from prosegrinder.dictionary import Dictionary
from prosegrinder.fragment import Fragment
from prosegrinder.fragment_container import FragmentContainer
from prosegrinder.paragraph import Paragraph
from prosegrinder.readability_scores import ReadabilityScores


class Prose(object):

    def __init__(self, text, dictionary=Dictionary()):
        self.text = text
        self.sha256 = hashlib.sha256(self.text.encode()).hexdigest()
        self.dictionary = dictionary
        self.paragraphs = Paragraph.parse_paragraphs(
            self.text, self.dictionary)
        self.word_character_count = sum(
            [paragraph.word_character_count for paragraph in self.paragraphs])
        self.syllable_count = sum(
            [paragraph.syllable_count for paragraph in self.paragraphs])
        self.word_count = sum(
            [paragraph.word_count for paragraph in self.paragraphs])
        self.complex_word_count = sum(
            [paragraph.complex_word_count for paragraph in self.paragraphs])
        self.long_word_count = sum(
            [paragraph.long_word_count for paragraph in self.paragraphs])
        self.pov_word_count = sum(
            [paragraph.pov_word_count for paragraph in self.paragraphs])
        self.first_person_word_count = sum(
            [paragraph.first_person_word_count for paragraph in self.paragraphs])
        self.second_person_word_count = sum(
            [paragraph.second_person_word_count for paragraph in self.paragraphs])
        self.third_person_word_count = sum(
            [paragraph.third_person_word_count for paragraph in self.paragraphs])
        wf = Counter()
        pf = Counter()
        pc = 0
        for paragraph in self.paragraphs:
            wf.update(paragraph.word_frequency)
            pf.update(paragraph.phone_frequency)
            pc += paragraph.phone_count
        self.word_frequency = dict(wf)
        self.phone_frequency = dict(pf)
        self.phone_count = pc
        self.unique_words = self.word_frequency.keys()
        self.unique_word_count = len(self.unique_words)
        self.sentence_count = sum(
            [paragraph.sentence_count for paragraph in self.paragraphs])
        self.paragraph_count = len(self.paragraphs)
        self.readability_scores = ReadabilityScores(
            self.word_character_count, self.syllable_count, self.word_count,
            self.complex_word_count, self.long_word_count, self.sentence_count)
        n = narrative.split(self.text)
        self.dialogue = FragmentContainer(
            [Fragment(fragment_text) for fragment_text in n['dialogue']])
        self.narrative = FragmentContainer(
            [Fragment(fragment_text) for fragment_text in n['narrative']])
        self.pov = self.narrative.pov

    def __eq__(self, other):
        return self.text == other.text

    def __hash__(self):
        return hash(self.text)

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
    # def word_character_count(self):
    #     return self.word_character_count

    # @property
    # def syllable_count(self):
    #     return self.syllable_count

    # @property
    # def word_count(self):
    #     return self.word_count

    # @property
    # def complex_word_count(self):
    #     return self.complex_word_count

    # @property
    # def long_word_count(self):
    #     return self.long_word_count

    # @property
    # def unique_word_count(self):
    #     return len(self.word_frequency)

    # @property
    # def pov_word_count(self):
    #     return self.pov_word_count

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
    # def sentence_count(self):
    #     return self.sentence_count

    # @property
    # def paragraph_count(self):
    #     return self.paragraph_count

    # @property
    # def readability_scores(self):
    #     return self.readability_scores

    # @property
    # def dialogue(self):
    #     return self.dialogue

    # @property
    # def narrative(self):
    #     return self.narrative

    # @property
    # def pov(self):
    #     return self.pov

    # @property
    # def text(self):
    #     return self.text

    # @property
    # def sha256(self):
    #     return self.sha256
