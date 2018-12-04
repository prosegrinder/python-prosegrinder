# -*- coding: utf-8 -*-

import pkg_resources

from prosegrinder.word import Word
from prosegrinder.dictionary import Dictionary
from prosegrinder.sentence import Sentence
from prosegrinder.paragraph import Paragraph
from prosegrinder.prose import Prose
from prosegrinder.readability_scores import ReadabilityScores


__version__ = pkg_resources.resource_string(
    'prosegrinder', 'VERSION').decode('utf-8').strip()
