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
        self.text = text
        self.dictionary = dictionary
        self.sentences = Sentence.parse_sentences(
            self.text, self.dictionary)
        self.sentence_count = len(self.sentences)
        n = narrative.split(self.text)
        self.dialogue = FragmentContainer(
            [Fragment(fragment_text) for fragment_text in n['dialogue']])
        self.narrative = FragmentContainer(
            [Fragment(fragment_text) for fragment_text in n['narrative']])
        self.pov = self.narrative.pov
        super().__init__(self.sentences, self.dictionary)

    def __eq__(self, other):
        return self.text == other.text

    # @property
    # def sentence_count(self):
    #     return self.fragment_count

    # @property
    # def dialogue(self):
    #     return self.dialogue

    # @property
    # def narrative(self):
    #     return self.narrative

    # @property
    # def pov(self):
    #     return self.pov

    @staticmethod
    def parse_paragraphs(text, dictionary=Dictionary()):
        return [Paragraph(paragraph, dictionary) for paragraph in re.findall(
            Paragraph.RE_PARAGRAPH, text)]
