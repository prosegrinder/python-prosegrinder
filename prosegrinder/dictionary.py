# -*- coding: utf-8 -*-

import re

import cmudict
import syllables

from prosegrinder.word import Word


class Dictionary():
    """A reference containing Words."""

    RE_NUMERIC = re.compile("^[+-]{0,1}\\d{1,3}(?:[,]\\d{3})*(?:[.]\\d*)*$")

    @staticmethod
    def normalize_text(text):
        return text.strip().lower()

    @staticmethod
    def is_numeric(word):
        return re.match(Dictionary.RE_NUMERIC, word) != None

    def __init__(self, cmudict=cmudict.dict()):
        self._cmudict = cmudict

    def syllable_count(self, word):
        syllable_count = 0
        if word in self._cmudict:
            phones = self._cmudict[word][0]
            # There's a more Pythonic way of doing this.
            for phone in phones:
                syllable_count += len(re.sub("[^012]", "", phone))
        elif self.is_numeric(word):
            syllable_count = len(re.sub('[^\\d\\+-]', '', word))
        else:
            syllable_count = syllables.estimate(word)
        return syllable_count

    @property
    def cmudict(self):
        return self._cmudict

    def get_word(self, word):
        normalized_word = self.normalize_text(word)
        syllable_count = self.syllable_count(normalized_word)
        is_dictionary_word = normalized_word in self._cmudict
        is_numeric = self.is_numeric(normalized_word)
        word = Word(normalized_word, syllable_count,
                    is_dictionary_word, is_numeric)
        return word
