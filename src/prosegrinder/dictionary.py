import re

import cmudict
import syllables

from prosegrinder.word import Word


class Dictionary:

    """A reference containing Words."""

    RE_NUMERIC = re.compile("^[+-]{0,1}\\d{1,3}(?:[,]\\d{3})*(?:[.]\\d*)*$")

    @staticmethod
    def normalize_text(text):
        return text.strip().lower()

    @staticmethod
    def normalize_phones(phones):
        return [re.sub(r"\d", "", phone) for phone in phones]

    @staticmethod
    def is_numeric(word):
        return re.match(Dictionary.RE_NUMERIC, word) is not None

    def __init__(self, cmudictdict=None):
        """
        Dictionary constructor.

        Arguments:
        ---------
        cmudictdict: a cmudict-compatible dictionary

        """
        self.cmudictdict = cmudictdict or cmudict.dict()

    def phones(self, word):
        if word in self.cmudictdict:
            return self.cmudictdict[word][0]
        return ["?"]

    def syllable_count(self, word):
        syllable_count = 0
        if word in self.cmudictdict:
            phones = self.cmudictdict[word][0]
            # There's a more Pythonic way of doing this.
            for phone in phones:
                syllable_count += len(re.sub("[^012]", "", phone))
        elif self.is_numeric(word):
            syllable_count = len(re.sub("[^\\d\\+-]", "", word))
        else:
            syllable_count = syllables.estimate(word)
        return syllable_count

    def get_word(self, word):
        normalized_word = self.normalize_text(word)
        phones = self.phones(normalized_word)
        normalized_phones = self.normalize_phones(phones)
        syllable_count = self.syllable_count(normalized_word)
        is_dictionary_word = normalized_word in self.cmudictdict
        is_numeric = self.is_numeric(normalized_word)
        word = Word(
            normalized_word,
            phones,
            normalized_phones,
            syllable_count,
            is_dictionary_word,
            is_numeric,
        )
        return word
