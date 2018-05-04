# -*- coding: utf-8 -*-

import re
from collections import Counter

from bookworm.paragraph import Paragraph


class Prose():

    def __init__(self, prose_string, dictionary):
        self._prose_string = prose_string
        self._dictionary = dictionary
        self._paragraphs = [paragraph for paragraph in re.findall(
            Paragraph.RE_PARAGRAPH, self._prose_string)]
        self._word_count = sum([paragraph.word_count()
                                for paragraph in self._paragraphs])
        self._character_count = sum(
            [paragraph.character_count() for paragraph in self._paragraphs])
        self._syllable_count = sum(
            [paragraph.syllable_count() for paragraph in self._paragraphs])
        self._complex_word_count = sum(
            [paragraph.complex_word_count() for paragraph in self._paragraphs])
        self._long_word_count = sum(
            [paragraph.long_word_count() for paragraph in self._paragraphs])
        self._pov_word_count = sum(
            [paragraph.pov_word_count() for paragraph in self._paragraphs])
        self._first_person_word_count = sum(
            [paragraph.first_person_word_count() for paragraph in self._paragraphs])
        self._second_person_word_count = sum(
            [paragraph.second_person_word_count() for paragraph in self._paragraphs])
        self._third_person_word_count = sum(
            [paragraph.third_person_word_count() for paragraph in self._paragraphs])
        self._word_frequency = sum(
            [paragraph.word_frequency() for paragraph in self._paragraphs])