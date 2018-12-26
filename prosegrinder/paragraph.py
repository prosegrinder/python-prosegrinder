# -*- coding: utf-8 -*-

import re

import narrative

from prosegrinder.dictionary import Dictionary
from prosegrinder.fragment import Fragment
from prosegrinder.fragment_container import FragmentContainer
from prosegrinder.sentence import Sentence


class Paragraph(FragmentContainer):

    RE_PARAGRAPH = re.compile(".*(?=\\n|$)")

    def __init__(self, text, dictionary=Dictionary()):
        self._text = text
        self._dictionary = dictionary
        self._sentences = Sentence.parse_sentences(
            self._text, self._dictionary)
        n = narrative.split(self._text)
        self._dialogue = FragmentContainer(
            [Fragment(fragment_text) for fragment_text in n['dialogue']])
        self._narrative = FragmentContainer(
            [Fragment(fragment_text) for fragment_text in n['narrative']])
        self._pov = self._narrative.pov
        super().__init__(self._sentences, self._dictionary)

    def __eq__(self, other):
        return self._text == other._text

    @property
    def sentence_count(self):
        return self.fragment_count

    @property
    def dialogue(self):
        return self._dialogue

    @property
    def narrative(self):
        return self._narrative

    @property
    def pov(self):
        return self._pov

    @staticmethod
    def parse_paragraphs(text, dictionary=Dictionary()):
        return [Paragraph(paragraph, dictionary) for paragraph in re.findall(
            Paragraph.RE_PARAGRAPH, text)]
