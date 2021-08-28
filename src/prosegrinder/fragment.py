import re
from collections import Counter

import pointofview

from prosegrinder.dictionary import Dictionary
from prosegrinder.word import Word


class Fragment:
    def __init__(self, text, dictionary=Dictionary()):
        self.text = text
        self.dictionary = dictionary
        self.normalized_sentence = dictionary.normalize_text(text)
        self.words = [
            self.dictionary.get_word(word)
            for word in re.findall(Word.RE_WORD, self.normalized_sentence)
        ]
        self.word_count = len(self.words)
        self.word_character_count = sum([word.character_count for word in self.words])
        pf = Counter()
        pc = 0
        for word in self.words:
            pf.update(word.phone_frequency)
            pc += word.phone_count
        self.phone_frequency = pf
        self.phone_count = pc
        self.syllable_count = sum([word.syllable_count for word in self.words])
        self.complex_word_count = sum([word.is_complex_word for word in self.words])
        self.long_word_count = sum([word.is_long_word for word in self.words])
        self.pov_word_count = sum([word.is_pov_word for word in self.words])
        self.first_person_word_count = sum(
            [word.is_first_person_word for word in self.words]
        )
        self.second_person_word_count = sum(
            [word.is_second_person_word for word in self.words]
        )
        self.third_person_word_count = sum(
            [word.is_third_person_word for word in self.words]
        )
        self.word_frequency = dict(Counter(self.words))
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
        return self.text == other.text

    def __hash__(self):
        """Hash operator for instance variables."""
        return hash(self.text)

    def frequency(self, word_string):
        return self.word_frequency[word_string]

    @property
    def stats(self):
        """Returns a light-weight dict with basic stats about the fragment."""
        return {
            "word_character_count": self.word_character_count,
            "phone_frequency": self.phone_frequency,
            "phone_count": self.phone_count,
            "syllable_count": self.syllable_count,
            "complex_word_count": self.complex_word_count,
            "long_word_count": self.long_word_count,
            "pov_word_count": self.pov_word_count,
            "first_person_word_count": self.first_person_word_count,
            "second_person_word_count": self.second_person_word_count,
            "third_person_word_count": self.third_person_word_count,
            "word_frequency": self.word_frequency,
            "unique_words": self.unique_words,
            "unique_word_count": self.unique_word_count,
            "pov": self.pov,
        }
