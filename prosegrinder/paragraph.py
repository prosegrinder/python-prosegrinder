# -*- coding: utf-8 -*-

import re
from collections import Counter

from prosegrinder.dictionary import Dictionary
from prosegrinder.sentence import Sentence
import narrative


class Paragraph():

    RE_PARAGRAPH = re.compile(".*(?=\\n|$)")

    def __init__(self, paragraph_string, dictionary=None):
        self._paragraph_string = paragraph_string
        self._dictionary = dictionary if dictionary else Dictionary()
        self._sentences = [Sentence(sentence, self._dictionary) for sentence in re.findall(
            Sentence.RE_SENTENCE, self._paragraph_string)]
        self._word_count = sum([sentence.word_count
                                for sentence in self._sentences])
        self._character_count = sum(
            [sentence.character_count for sentence in self._sentences])
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
        self._pov = None
        self._dialogue = {'character_count': 0, 'syllable_count': 0,
                          'word_count': 0, 'first_person_word_count': 0,
                          'second_person_word_count': 0, 'third_person_word_count': 0,
                          'pov': None, 'fragments': []}
        self._narrative = {'character_count': 0, 'syllable_count': 0,
                          'word_count': 0, 'first_person_word_count': 0,
                          'second_person_word_count': 0, 'third_person_word_count': 0,
                          'pov': None, 'fragments': []}
        n = narrative.split(paragraph_string)
        for dialogue_fragment in n['dialogue']:
            dialogue_sentence = Sentence(dialogue_fragment, self._dictionary)
            self._dialogue['fragments'].append(dialogue_sentence)
            self._dialogue['character_count'] += dialogue_sentence.character_count
            self._dialogue['syllable_count'] += dialogue_sentence.syllable_count
            self._dialogue['word_count'] += dialogue_sentence.word_count
            self._dialogue['first_person_word_count'] += dialogue_sentence.first_person_word_count
            self._dialogue['second_person_word_count'] += dialogue_sentence.second_person_word_count
            self._dialogue['third_person_word_count'] += dialogue_sentence.third_person_word_count
            self._dialogue['pov'] = None
            if (self._dialogue['first_person_word_count'] > 0):
                self._dialogue['pov'] = 'first'
            elif (self._dialogue['second_person_word_count'] > 0):
                self._dialogue['pov'] = 'second'
            elif (self._dialogue['third_person_word_count'] > 0):
                self._dialogue['pov'] = 'third'
        for narrative_fragment in n['narrative']:
            narrative_sentence = Sentence(narrative_fragment, self._dictionary)
            self._narrative['fragments'].append(narrative_sentence)
            self._narrative['character_count'] += narrative_sentence.character_count
            self._narrative['syllable_count'] += narrative_sentence.syllable_count
            self._narrative['word_count'] += narrative_sentence.word_count
            self._narrative['first_person_word_count'] += narrative_sentence.first_person_word_count
            self._narrative['second_person_word_count'] += narrative_sentence.second_person_word_count
            self._narrative['third_person_word_count'] += narrative_sentence.third_person_word_count
            self._narrative['pov'] = None
            if (self._narrative['first_person_word_count'] > 0):
                self._narrative['pov'] = 'first'
            elif (self._narrative['second_person_word_count'] > 0):
                self._narrative['pov'] = 'second'
            elif (self._narrative['third_person_word_count'] > 0):
                self._narrative['pov'] = 'third'

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self._paragraph_string == other._paragraph_string

    def __hash__(self):
        return hash(self._paragraph_string)

    @property
    def word_count(self):
        return self._word_count

    @property
    def character_count(self):
        return self._character_count

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
    def paragraph_string(self):
        return self._paragraph_string

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
