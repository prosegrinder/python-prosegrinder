import re
from collections import Counter

import pointofview


class Word():

    """A Word, the base unit for measuring fiction prose."""

    MIN_SYLLABLES_COMPLEX_WORD = 3
    MIN_CHARS_LONG_WORD = 7
    # See: https://en.wikipedia.org/wiki/List_of_Unicode_characters
    RE_WORD = re.compile(
        "[\\w’'\u0391-\u03ce\u0400-\u0481\u048a-\u04ff]+")

    def __init__(self, text, phones, normalized_phones,
            syllable_count, is_dictionary_word, is_numeric):
        """
        Word constructor.

        Arguments:
        ---------
        text: a single word, normalized
        phones: the word's phones with syllable marks
        normalized_phones: the word's phone without syllable marks
        syllable_count: number of syllables in the word
        is_dictionary_word: is it in the underlying dictionary
        is_numeric: is it a word representing a number

        """
        # Assumes text is a single word, normalized.
        self.text = text
        self.character_count = len(self.text)
        self.phones = phones
        self.normalized_phones = normalized_phones
        self.phone_count = len(self.normalized_phones)
        self.phone_frequency = dict(Counter(self.normalized_phones))
        self.syllable_count = syllable_count
        self.is_dictionary_word = is_dictionary_word
        self.is_numeric = is_numeric
        self.is_complex_word = \
            self.syllable_count >= Word.MIN_SYLLABLES_COMPLEX_WORD
        self.is_long_word = \
            self.character_count >= Word.MIN_CHARS_LONG_WORD
        self.pov = pointofview.get_word_pov(self.text)
        self.is_first_person_word = \
            (self.pov == pointofview.FIRST)
        self.is_second_person_word = \
            (self.pov == pointofview.SECOND)
        self.is_third_person_word = \
            (self.pov == pointofview.THIRD)
        self.is_pov_word = (
            self.is_first_person_word or
            self.is_second_person_word or
            self.is_third_person_word)

    def __eq__(self, other):
        """Equals overload."""
        return self.__dict__ == other.__dict__

    def __hash__(self):
        """Hash overload."""
        return hash(self.text)
