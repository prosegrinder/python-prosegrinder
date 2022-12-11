"""ProseGrinder

A Python library for analyzing prose.
"""

import sys

from prosegrinder.dictionary import Dictionary
from prosegrinder.paragraph import Paragraph
from prosegrinder.prose import Prose
from prosegrinder.readability_scores import ReadabilityScores
from prosegrinder.sentence import Sentence
from prosegrinder.word import Word

if sys.version_info >= (3, 9):
    from importlib import metadata
else:
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)
