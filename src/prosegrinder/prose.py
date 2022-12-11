"""Prose class for prosegrinder."""
import hashlib
from collections import Counter

import narrative

from prosegrinder.dictionary import Dictionary
from prosegrinder.fragment import Fragment
from prosegrinder.fragment_container import FragmentContainer
from prosegrinder.paragraph import Paragraph
from prosegrinder.readability_scores import ReadabilityScores


class Prose:
    """A piece of prose."""

    def __init__(self, text, dictionary=Dictionary()):
        self.text = text
        self.sha256 = hashlib.sha256(self.text.encode()).hexdigest()
        self.dictionary = dictionary
        self.paragraphs = Paragraph.parse_paragraphs(self.text, self.dictionary)
        self.word_character_count = sum(
            paragraph.word_character_count for paragraph in self.paragraphs
        )
        self.syllable_count = sum(
            paragraph.syllable_count for paragraph in self.paragraphs
        )
        self.word_count = sum(paragraph.word_count for paragraph in self.paragraphs)
        self.complex_word_count = sum(
            paragraph.complex_word_count for paragraph in self.paragraphs
        )
        self.long_word_count = sum(
            paragraph.long_word_count for paragraph in self.paragraphs
        )
        self.pov_word_count = sum(
            paragraph.pov_word_count for paragraph in self.paragraphs
        )
        self.first_person_word_count = sum(
            paragraph.first_person_word_count for paragraph in self.paragraphs
        )
        self.second_person_word_count = sum(
            paragraph.second_person_word_count for paragraph in self.paragraphs
        )
        self.third_person_word_count = sum(
            paragraph.third_person_word_count for paragraph in self.paragraphs
        )
        _wf = Counter()
        _pf = Counter()
        _pc = 0
        for paragraph in self.paragraphs:
            _wf.update(paragraph.word_frequency)
            _pf.update(paragraph.phone_frequency)
            _pc += paragraph.phone_count
        self.word_frequency = dict(_wf)
        self.phone_frequency = dict(_pf)
        self.phone_count = _pc
        self.unique_words = self.word_frequency.keys()
        self.unique_word_count = len(self.unique_words)
        self.sentence_count = sum(
            paragraph.sentence_count for paragraph in self.paragraphs
        )
        self.paragraph_count = len(self.paragraphs)
        self.readability_scores = ReadabilityScores(
            self.word_character_count,
            self.syllable_count,
            self.word_count,
            self.complex_word_count,
            self.long_word_count,
            self.sentence_count,
        )
        _n = narrative.split(self.text)
        self.dialogue = FragmentContainer(
            [Fragment(fragment_text) for fragment_text in _n["dialogue"]]
        )
        self.narrative = FragmentContainer(
            [Fragment(fragment_text) for fragment_text in _n["narrative"]]
        )
        self.pov = self.narrative.pov

    def __eq__(self, other):
        """Equality operator for instance variables."""
        return self.text == other.text

    def __hash__(self):
        """Hash operator for instance variables."""
        return hash(self.text)

    @property
    def stats(self):
        """Returns a light-weight dict with basic stats about the prose."""
        return {
            "sha256": self.sha256,
            "word_character_count": self.word_character_count,
            "phone_count": self.phone_count,
            "syllable_count": self.syllable_count,
            "word_count": self.word_count,
            "sentence_count": self.sentence_count,
            "paragraph_count": self.paragraph_count,
            "complex_word_count": self.complex_word_count,
            "long_word_count": self.long_word_count,
            "pov_word_count": self.pov_word_count,
            "first_person_word_count": self.first_person_word_count,
            "second_person_word_count": self.second_person_word_count,
            "third_person_word_count": self.third_person_word_count,
            "pov": self.pov,
            "readability_scores": {
                "automated_readability_index": self.readability_scores.automated_readability_index,
                "coleman_liau_index": self.readability_scores.coleman_liau_index,
                "flesch_kincaid_grade_level": self.readability_scores.flesch_kincaid_grade_level,
                "flesch_reading_ease": self.readability_scores.flesch_reading_ease,
                "gunning_fog_index": self.readability_scores.gunning_fog_index,
                "linsear_write": self.readability_scores.linsear_write,
                "lix": self.readability_scores.lix,
                "rix": self.readability_scores.rix,
                "smog": self.readability_scores.smog,
            },
        }
