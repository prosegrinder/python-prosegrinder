# -*- coding: utf-8 -*-

import os

from prosegrinder import Dictionary, Prose, ReadabilityScores

dictionary = Dictionary()
SHORTSTORY = os.path.join(os.path.dirname(
    __file__), 'resources', 'shortstory.txt')
text = open(SHORTSTORY).read()
prose = Prose(text)

CHARACTER_COUNT = 7008
SYLLABLE_COUNT = 2287
COMPLEX_WORD_COUNT = 202
LONG_WORD_COUNT = 275
SENTENCE_COUNT = 90
WORD_COUNT = 1528
UNIQUE_WORD_COUNT = 526
POV_INDICATOR_COUNT = 113  # was 104
FIRST_PERSON_INDICATOR_COUNT = 8  # was 6
SECOND_PERSON_INDICATOR_COUNT = 74  # was 73
THIRD_PERSON_INDICATOR_COUNT = 31  # was 25
PARAGRAPH_COUNT = 77


AUTOMATED_READABILITY_INDEX = 0.28090308159411137
COLEMAN_LIAU_INDEX = 9.424502617801043
FLESCH_KINCAID_GRADE_LEVEL = 8.692720767888307
FLESCH_READING_EASE = 62.97938801628857
GUNNING_FOG_INDEX = 12.079069226294358
LIX = 34.97515997673066
RIX = 3.0555555555555554
SMOG = 11.687633713980063


def test_characters():
    assert(CHARACTER_COUNT == prose.character_count)


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


def test_readability_scores():
    assert(AUTOMATED_READABILITY_INDEX ==
           prose.readability_scores.automated_readability_index)
    assert(COLEMAN_LIAU_INDEX == prose.readability_scores.coleman_liau_index)
    assert(FLESCH_KINCAID_GRADE_LEVEL ==
           prose.readability_scores.flesch_kincaid_grade_level)
    assert(FLESCH_READING_EASE == prose.readability_scores.flesch_reading_ease)
    assert(GUNNING_FOG_INDEX == prose.readability_scores.gunning_fog_index)
    assert(LIX == prose.readability_scores.lix)
    assert(RIX == prose.readability_scores.rix)
    assert(SMOG == prose.readability_scores.smog)
