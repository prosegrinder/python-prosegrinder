# -*- coding: utf-8 -*-

import pkg_resources

from bookworm.word import Word
from bookworm.dictionary import Dictionary
from bookworm.sentence import Sentence
from bookworm.paragraph import Paragraph


__version__ = pkg_resources.resource_string(
    'bookworm', 'VERSION').decode('utf-8').strip()
