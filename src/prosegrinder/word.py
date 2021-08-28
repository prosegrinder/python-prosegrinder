import re
from collections import Counter

import pointofview


class Word:

    """
    A class to represent a natural-language word.

    Attributes
    ----------
    text : str
        a single word, normalized
    character_count : int
        number of characters in the word
    phones : list[str]
        the word's phones with syllable marks
    normalized_phones : list[str]
        the word's phone without syllable marks
    phone_count : int
        number of phones in the word
    phone_frequency : dict
    syllable_count : int
        number of syllables in the word
    is_dictionary_word : bool
        is it in the underlying dictionary
    is_numeric : bool
        is it a word representing a number
    is_complex_word : bool
        is it a complex word (>= 3 syllables)
    is_long_word : bool
        is it a long word (>= 7 characters)
    pov : str
        the word's point of view
    is_first_person_word : bool
        is the word a first person pov indicator
    is_second_person_word : bool
        is the word a second person pov indicator
    is_third_person_word : bool
        is the word a third person pov indicator
    is_pov_word : bool
        is the word a pov indicator

    """

    MIN_SYLLABLES_COMPLEX_WORD = 3
    MIN_CHARS_LONG_WORD = 7
    # See: https://en.wikipedia.org/wiki/List_of_Unicode_characters
    RE_WORD = re.compile("[\\w’'\u0391-\u03ce\u0400-\u0481\u048a-\u04ff]+")

    # pylint:disable=too-many-arguments
    def __init__(
        self,
        text,
        phones,
        normalized_phones,
        syllable_count,
        is_dictionary_word,
        is_numeric,
    ):
        """
        Word constructor.

        Argument:
        --------
        text : str
            a single word, normalized
        phones : list[str]
            the word's phones with syllable marks
        normalized_phones : list[str]
            the word's phone without syllable marks
        syllable_count : int
            umber of syllables in the word
        is_dictionary_word : bool
            is it in the underlying dictionary
        is_numeric : bool
            is it a word representing a number

        """
        # pylint:disable=too-many-instance-attributes
        self.text = text
        self.character_count = len(self.text)
        self.phones = phones
        self.normalized_phones = normalized_phones
        self.phone_count = len(self.normalized_phones)
        self.phone_frequency = dict(Counter(self.normalized_phones))
        self.syllable_count = syllable_count
        self.is_dictionary_word = is_dictionary_word
        self.is_numeric = is_numeric
        self.is_complex_word = self.syllable_count >= Word.MIN_SYLLABLES_COMPLEX_WORD
        self.is_long_word = self.character_count >= Word.MIN_CHARS_LONG_WORD
        self.pov = pointofview.get_word_pov(self.text)
        self.is_first_person_word = self.pov == pointofview.FIRST
        self.is_second_person_word = self.pov == pointofview.SECOND
        self.is_third_person_word = self.pov == pointofview.THIRD
        self.is_pov_word = (
            self.is_first_person_word
            or self.is_second_person_word
            or self.is_third_person_word
        )

    def __eq__(self, other):
        """Equality operator for instance variables."""
        return self.__dict__ == other.__dict__

    def __hash__(self):
        """Hash operator for instance variables."""
        return hash(self.text)
