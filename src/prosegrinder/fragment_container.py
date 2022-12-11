"""Fragment container class for prosegrinder."""
from collections import Counter

import pointofview

from prosegrinder.dictionary import Dictionary


class FragmentContainer:
    """A container for fragments."""

    def __init__(self, fragments, dictionary=Dictionary()):
        self.dictionary = dictionary
        self.fragments = fragments or []
        self.fragment_count = len(self.fragments)
        self.word_count = sum(fragment.word_count for fragment in self.fragments)
        self.word_character_count = sum(
            fragment.word_character_count for fragment in self.fragments
        )
        self.syllable_count = sum(
            fragment.syllable_count for fragment in self.fragments
        )
        self.complex_word_count = sum(
            fragment.complex_word_count for fragment in self.fragments
        )
        self.long_word_count = sum(
            fragment.long_word_count for fragment in self.fragments
        )
        self.pov_word_count = sum(
            fragment.pov_word_count for fragment in self.fragments
        )
        self.first_person_word_count = sum(
            fragment.first_person_word_count for fragment in self.fragments
        )
        self.second_person_word_count = sum(
            fragment.second_person_word_count for fragment in self.fragments
        )
        self.third_person_word_count = sum(
            fragment.third_person_word_count for fragment in self.fragments
        )
        _wf = Counter()
        _pf = Counter()
        _pc = 0
        for fragment in self.fragments:
            _wf.update(fragment.words)
            _pf.update(fragment.phone_frequency)
            _pc += fragment.phone_count
        self.word_frequency = dict(_wf)
        self.phone_frequency = dict(_pf)
        self.phone_count = _pc
        self.unique_words = self.word_frequency.keys()
        self.unique_word_count = len(self.unique_words)
        self.pov = pointofview.NONE
        if self.first_person_word_count > 0:
            self.pov = pointofview.FIRST
        elif self.second_person_word_count > 0:
            self.pov = pointofview.SECOND
        elif self.third_person_word_count > 0:
            self.pov = pointofview.THIRD

    def __eq__(self, other):
        """Equality operator for instance variables."""
        return self.fragments == other.fragments

    def __hash__(self):
        """Hash operator for instance variables."""
        return hash(self.fragments)

    def frequency(self, word_string):
        """Gets the frequency of a word in the fragment container."""
        return self.word_frequency[self.dictionary.get_word(word_string)]
