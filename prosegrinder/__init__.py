import pkg_resources

from prosegrinder.dictionary import Dictionary
from prosegrinder.paragraph import Paragraph
from prosegrinder.prose import Prose
from prosegrinder.readability_scores import ReadabilityScores
from prosegrinder.sentence import Sentence
from prosegrinder.word import Word

__version__ = (
    pkg_resources.resource_string("prosegrinder", "VERSION").decode("utf-8").strip()
)
