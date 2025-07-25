"""Sentence class for prosegrinder."""

import re

from prosegrinder.dictionary import Dictionary
from prosegrinder.fragment import Fragment


class Sentence(Fragment):
    """A sentence."""

    RE_SENTENCE = re.compile(
        """
        # Match a sentence ending in punctuation or EOS.
        [^.!?…\\s]        # First char is non-punct, non-ws
        [^.!?…]*          # Greedily consume up to punctuation.
        (?:               # Group for unrolling the loop.
        [.!?…]            # (special) inner punctuation ok if
        (?!['\")]?\\s|$)  # not followed by ws or EOS.
        [^.!?…]*          # Greedily consume up to punctuation.
        )*                # Zero or more (special normal*)
        [.!?…]            # Ending punctuation.
        ['\")]?           # Optional closing quote.
        (?=\\s|$)
        """,
        flags=re.MULTILINE | re.VERBOSE,
    )

    RE_SMART_QUOTES: re.Pattern = re.compile("[“”]")

    @staticmethod
    def parse_sentences(text: str, dictionary: Dictionary = Dictionary()):
        """Parses a text into a list of Sentence objects."""
        return [
            Sentence(sentence, dictionary)
            for sentence in re.findall(Sentence.RE_SENTENCE, text)
        ]

    @property
    def stats(self):
        """Returns a light-weight dict with basic stats about the sentence."""
        return super().stats
