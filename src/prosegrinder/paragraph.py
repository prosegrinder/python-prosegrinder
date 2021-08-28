import re

import narrative

from prosegrinder.dictionary import Dictionary
from prosegrinder.fragment import Fragment
from prosegrinder.fragment_container import FragmentContainer
from prosegrinder.sentence import Sentence


class Paragraph(FragmentContainer):

    RE_PARAGRAPH = re.compile(".*(?=\\n|$)")

    def __init__(self, text, dictionary=Dictionary()):
        self.text = text
        self.dictionary = dictionary
        self.sentences = Sentence.parse_sentences(self.text, self.dictionary)
        self.sentence_count = len(self.sentences)
        n = narrative.split(self.text)
        self.dialogue = FragmentContainer(
            [Fragment(fragment_text) for fragment_text in n["dialogue"]]
        )
        self.narrative = FragmentContainer(
            [Fragment(fragment_text) for fragment_text in n["narrative"]]
        )
        self.pov = self.narrative.pov
        super().__init__(self.sentences, self.dictionary)

    def __eq__(self, other):
        """Equality operator for instance variables."""
        return self.text == other.text

    @staticmethod
    def parse_paragraphs(text, dictionary=Dictionary()):
        return [
            Paragraph(paragraph, dictionary)
            for paragraph in re.findall(Paragraph.RE_PARAGRAPH, text)
        ]

    @property
    def stats(self):
        """Returns a light-weight dict with basic stats about the paragraph."""
        return {
            "sentence_count": self.sentence_count,
            "word_count": self.word_count,
            "word_character_count": self.word_character_count,
            "syllable_count": self.syllable_count,
            "complex_word_count": self.complex_word_count,
            "long_word_count": self.long_word_count,
            "pov_word_count": self.pov_word_count,
            "first_person_word_count": self.first_person_word_count,
            "second_person_word_count": self.second_person_word_count,
            "third_person_word_count": self.third_person_word_count,
            "word_frequency": self.word_frequency,
            "phone_frequency": self.phone_frequency,
            "phone_count": self.phone_count,
            "unique_words": self.unique_words,
            "unique_word_count": self.unique_word_count,
        }
