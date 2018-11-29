# -*- coding: utf-8 -*-

import os

from bookworm import Dictionary, Prose

dictionary = Dictionary()
SHORTSTORY = os.path.join(os.path.dirname(
    __file__), 'resources', 'shortstory.txt')
text = open(SHORTSTORY).read()
prose = Prose(text, dictionary)

SYLLABLE_COUNT = 2287  # was 2287
WORD_COUNT = 1528
COMPLEX_WORD_COUNT = 202  # was 202
LONG_WORD_COUNT = 275
UNIQUE_WORD_COUNT = 526
POV_INDICATOR_COUNT = 113  # was 104
FIRST_PERSON_INDICATOR_COUNT = 8  # was 6
SECOND_PERSON_INDICATOR_COUNT = 74  # was 73
THIRD_PERSON_INDICATOR_COUNT = 31  # was 25
SENTENCE_COUNT = 90
PARAGRAPH_COUNT = 77


def test_syllables():
    assert(SYLLABLE_COUNT == prose.syllable_count)


def test_words():
    assert(WORD_COUNT == prose.word_count)
    assert(COMPLEX_WORD_COUNT == prose.complex_word_count)
    assert(LONG_WORD_COUNT == prose.long_word_count)
    assert(UNIQUE_WORD_COUNT == prose.unique_word_count)


def test_pov():
    assert(POV_INDICATOR_COUNT == prose.pov_word_count)
    assert(FIRST_PERSON_INDICATOR_COUNT == prose.first_person_word_count)
    assert(SECOND_PERSON_INDICATOR_COUNT == prose.second_person_word_count)
    assert(THIRD_PERSON_INDICATOR_COUNT == prose.third_person_word_count)


def test_sentences():
    assert(SENTENCE_COUNT == prose.sentence_count)


def test_paragraphs():
    assert(PARAGRAPH_COUNT == prose.paragrah_count)


def test_dialogue():
    pass


def test_narrative():
    pass
