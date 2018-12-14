# -*- coding: utf-8 -*-

import re
from collections import Counter

import narrative
import pointofview

from prosegrinder.dictionary import Dictionary
from prosegrinder.fragment import Fragment
from prosegrinder.fragment_container import FragmentContainer
from prosegrinder.sentence import Sentence


class Paragraph():

    RE_PARAGRAPH = re.compile(".*(?=\\n|$)")

    def __init__(self, text, dictionary=Dictionary()):
        self._text = text
        self._dictionary = dictionary
        self._sentences = Sentence.parse_sentences(
            self._text, self._dictionary)
        self._word_count = sum([sentence.word_count
                                for sentence in self._sentences])
        self._word_character_count = sum(
            [sentence.word_character_count for sentence in self._sentences])
        self._syllable_count = sum(
            [sentence.syllable_count for sentence in self._sentences])
        self._complex_word_count = sum(
            [sentence.complex_word_count for sentence in self._sentences])
        self._long_word_count = sum(
            [sentence.long_word_count for sentence in self._sentences])
        self._pov_word_count = sum(
            [sentence.pov_word_count for sentence in self._sentences])
        self._first_person_word_count = sum(
            [sentence.first_person_word_count for sentence in self._sentences])
        self._second_person_word_count = sum(
            [sentence.second_person_word_count for sentence in self._sentences])
        self._third_person_word_count = sum(
            [sentence.third_person_word_count for sentence in self._sentences])
        wf = Counter()
        for sentence in self._sentences:
            wf.update(sentence.words)
        self._word_frequency = dict(wf)
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
    def text(self):
        return self._text

    @property
    def frequency(self, word_string):
        return self._word_frequency[self._dictionary.get_word(word_string)]

    @property
    def sentence_count(self):
        return len(self._sentences)

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

    @property
    def dialogue(self):
        return self._dialogue

    @property
    def narrative(self):
        return self._narrative

    @staticmethod
    def parse_paragraphs(text, dictionary=Dictionary()):
        return [Paragraph(paragraph, dictionary) for paragraph in re.findall(
            Paragraph.RE_PARAGRAPH, text)]
