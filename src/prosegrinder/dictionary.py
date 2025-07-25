"""Dictionary class for prosegrinder."""

import re

import cmudict
import syllables

from prosegrinder.word import Word


class Dictionary:
    """A reference containing Words."""

    RE_NUMERIC = re.compile("^[+-]{0,1}\\d{1,3}(?:[,]\\d{3})*(?:[.]\\d*)*$")

    @staticmethod
    def normalize_text(text):
        """Normalizes text
        Parameters:
        ----------
        text : str
            the text to normalize
        Returns:
        -------
        str
            the normalized text
        """
        return text.strip().lower()

    @staticmethod
    def normalize_phones(phones):
        """Normalizes phones
        Parameters:
        ----------
        phones : list
            list of phones to normalize
        Returns:
        -------
        list
            list of normalized phones
        """
        return [re.sub(r"\d", "", phone) for phone in phones]

    @staticmethod
    def is_numeric(word):
        """Checks if word is numeric
        Parameters:
        ----------
        word : str
            word to check
        Returns:
        -------
        bool
            whether word is numeric
        """
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
        """Gets the phones for a word.
        Parameters:
        ----------
        word : str
            word to get phones for
        Returns:
        -------
        list
            phones for word (returns "?" if word is not in dictionary)
        """
        if word in self.cmudictdict:
            return self.cmudictdict[word][0]
        return ["?"]

    def syllable_count(self, word):
        """Guesses the number of syllables in a word.
        Parameters:
        ----------
        word : str
            word to check
        Returns:
        -------
        int
            number of syllables in word
        """
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
        """Gets a Word object for a word.
        Parameters:
        ----------
        word : str
            word to retrieve
        Returns:
        -------
        Word
            Word object for word
        """
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
