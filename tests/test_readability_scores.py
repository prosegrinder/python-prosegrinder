# -*- coding: utf-8 -*-

from bookworm import ReadabilityScores


COMPLEX_WORD_COUNT = 202
LONG_WORD_COUNT = 275
SENTENCE_COUNT = 90
SYLLABLE_COUNT = 2287
WORD_COUNT = 1528
CHARACTER_COUNT = 7008

AUTOMATED_READABILITY_INDEX = 0.28090308159411137
COLEMAN_LIAU_INDEX = 9.424502617801043
FLESCH_KINCAID_GRADE_LEVEL = 8.692720767888307
FLESCH_READING_EASE = 62.97938801628857
GUNNING_FOG_INDEX = 12.079069226294358
LIX = 34.97515997673066
RIX = 3.0555555555555554
SMOG = 11.687633713980063


def test_calculate_automated_readability_index():
    score = ReadabilityScores.calculate_automated_readability_index(
        CHARACTER_COUNT, WORD_COUNT, SENTENCE_COUNT)
    assert(AUTOMATED_READABILITY_INDEX == score)


def test_calculate_coleman_liau_index():
    score = ReadabilityScores.calculate_coleman_liau_index(
        CHARACTER_COUNT, WORD_COUNT, SENTENCE_COUNT)
    assert(COLEMAN_LIAU_INDEX == score)


def test_calculate_flesch_kincaid_grade_level():
    score = ReadabilityScores.calculate_flesch_kincaid_grade_level(
        SYLLABLE_COUNT, WORD_COUNT, SENTENCE_COUNT)
    assert(FLESCH_KINCAID_GRADE_LEVEL == score)


def test_calculate_flesch_reading_ease():
    score = ReadabilityScores.calculate_flesch_reading_ease(
        SYLLABLE_COUNT, WORD_COUNT, SENTENCE_COUNT)
    assert(FLESCH_READING_EASE == score)


def test_calculate_gunning_fog_index():
    score = ReadabilityScores.calculate_gunning_fog_index(
        WORD_COUNT, COMPLEX_WORD_COUNT, SENTENCE_COUNT)
    assert(GUNNING_FOG_INDEX == score)


def test_calculate_lix():
    score = ReadabilityScores.calculate_lix(
        WORD_COUNT, LONG_WORD_COUNT, SENTENCE_COUNT)
    assert(LIX == score)


def test_calculate_rix():
    score = ReadabilityScores.calculate_rix(LONG_WORD_COUNT, SENTENCE_COUNT)
    assert(RIX == score)


def test_calculate_smog():
    score = ReadabilityScores.calculate_smog(
        COMPLEX_WORD_COUNT, SENTENCE_COUNT)
    assert(SMOG == score)
