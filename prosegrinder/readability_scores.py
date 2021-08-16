# -*- coding: utf-8 -*-

from math import sqrt


class ReadabilityScores(object):

    NDIGITS = 3  # Default for round(number,[ndigits])

    def __init__(self, word_character_count, syllable_count, word_count,
                 complex_word_count, long_word_count, sentence_count, ndigits=NDIGITS):
        self._word_character_count = word_character_count
        self._syllable_count = syllable_count
        self._word_count = word_count
        self._complex_word_count = complex_word_count
        self._long_word_count = long_word_count
        self._sentence_count = sentence_count
        self._ndigits = ndigits

        self._automated_readability_index = self.calculate_automated_readability_index(
            self._word_character_count, self._word_count, self._sentence_count, self._ndigits
        )
        self._coleman_liau_index = self.calculate_coleman_liau_index(
            self._word_character_count, self._word_count, self._sentence_count, self._ndigits
        )
        self._flesch_kincaid_grade_level = self.calculate_flesch_kincaid_grade_level(
            self._syllable_count, self._word_count, self._sentence_count, self._ndigits
        )
        self._flesch_reading_ease = self.calculate_flesch_reading_ease(
            self._syllable_count, self._word_count, self._sentence_count, self._ndigits
        )
        self._gunning_fog_index = self.calculate_gunning_fog_index(
            self._word_count, self._complex_word_count, self._sentence_count, self._ndigits
        )
        self._linsear_write = self.calculate_linsear_write(
            self._word_count, self._complex_word_count, self._sentence_count, self._ndigits
        )
        self._lix = self.calculate_lix(
            self._word_count, self._long_word_count, self._sentence_count, self._ndigits
        )
        self._rix = self.calculate_rix(
            self._long_word_count, self._sentence_count, self._ndigits
        )
        self._smog = self.calculate_smog(
            self._complex_word_count, self._sentence_count, self._ndigits
        )

    @property
    def ndigits(self):
        return self._ndigits

    @property
    def automated_readability_index(self):
        return self._automated_readability_index

    @staticmethod
    def calculate_automated_readability_index(word_character_count, word_count, sentence_count, ndigits=NDIGITS):
        score = 0.0
        if (word_count > 0):
            avg_characters_per_word = word_character_count / word_count
            avg_words_per_sentence = word_count / word_character_count
            score = (4.71 * avg_characters_per_word) + \
                (0.5 * avg_words_per_sentence) - 21.43
        return round(score, ndigits)

    @property
    def coleman_liau_index(self):
        return self._coleman_liau_index

    @staticmethod
    def calculate_coleman_liau_index(word_character_count, word_count, sentence_count, ndigits=NDIGITS):
        score = 0.0
        if (word_count > 0):
            avg_letters_per_word = word_character_count / word_count * 100.0
            avg_sentences_per_word = sentence_count / word_count * 100.0
            score = (0.0588 * avg_letters_per_word) - \
                (0.296 * avg_sentences_per_word) - 15.8
        return round(score, ndigits)

    @property
    def flesch_kincaid_grade_level(self):
        return self._flesch_kincaid_grade_level

    @staticmethod
    def calculate_flesch_kincaid_grade_level(syllable_count, word_count, sentence_count, ndigits=NDIGITS):
        score = 0.0
        if (word_count > 0):
            avg_sentence_length = word_count / sentence_count
            avg_syllables_per_word = syllable_count / word_count
            score = (0.39 * avg_sentence_length) + \
                (11.8 * avg_syllables_per_word) - 15.59
        return round(score, ndigits)

    @property
    def flesch_reading_ease(self):
        return self._flesch_reading_ease

    @staticmethod
    def calculate_flesch_reading_ease(syllable_count, word_count, sentence_count, ndigits=NDIGITS):
        score = 0.0
        if (word_count > 0):
            avg_sentence_length = word_count / sentence_count
            avg_syllables_per_word = syllable_count / word_count
            score = 206.835 - (1.015 * avg_sentence_length) - \
                (84.6 * avg_syllables_per_word)
        return round(score, ndigits)

    @property
    def gunning_fog_index(self):
        return self._gunning_fog_index

    @staticmethod
    def calculate_gunning_fog_index(word_count, complex_word_count, sentence_count, ndigits=NDIGITS):
        score = 0.0
        if (word_count > 0):
            avg_sentence_length = word_count / sentence_count
            pct_hard_words = complex_word_count / word_count * 100.0
            score = 0.4 * (avg_sentence_length + pct_hard_words)
        return round(score, ndigits)

    @property
    def linsear_write(self):
        return self._linsear_write

    @staticmethod
    def calculate_linsear_write(word_count, complex_word_count, sentence_count, ndigits=NDIGITS):
        score = 0.0
        hard_word_count = complex_word_count
        easy_word_count = (word_count - complex_word_count)
        if (sentence_count > 0):
            r = (easy_word_count + (hard_word_count * 3)) / sentence_count
            if (r <= 20):
                r = r - 2
            score = r / 2
        return round(score, ndigits)

    @property
    def lix(self):
        return self._lix

    @staticmethod
    def calculate_lix(word_count, long_word_count, sentence_count, ndigits=NDIGITS):
        score = 0.0
        if (word_count > 0):
            score = word_count / sentence_count + \
                (100 * long_word_count) / word_count
        return round(score, ndigits)

    @property
    def rix(self):
        return self._rix

    @staticmethod
    def calculate_rix(long_word_count, sentence_count, ndigits=NDIGITS):
        score = 0.0
        if (sentence_count > 0):
            score = long_word_count / sentence_count
        return round(score, ndigits)

    @property
    def smog(self):
        return self._smog

    @staticmethod
    def calculate_smog(complex_word_count, sentence_count, ndigits=NDIGITS):
        score = 0.0
        if (sentence_count > 0):
            score = (1.0430 * sqrt(complex_word_count *
                                   (30 / sentence_count))) + 3.1291
        return round(score, ndigits)
