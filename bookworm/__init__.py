# -*- coding: utf-8 -*-

import pkg_resources

from bookworm.word import Word
from bookworm.dictionary import Dictionary


__version__ = pkg_resources.resource_string(
    'bookworm', 'VERSION').decode('utf-8').strip()
