# -*- coding: utf-8 -*-

from prosegrinder import ReadabilityScores


COMPLEX_WORD_COUNT = 202
LONG_WORD_COUNT = 275
SENTENCE_COUNT = 90
SYLLABLE_COUNT = 2287
WORD_COUNT = 1528
CHARACTER_COUNT = 7008

AUTOMATED_READABILITY_INDEX = 0.281
COLEMAN_LIAU_INDEX = 9.425
FLESCH_KINCAID_GRADE_LEVEL = 8.693
FLESCH_READING_EASE = 62.979
GUNNING_FOG_INDEX = 12.079
LINSEAR_WRITE = 10.733
LIX = 34.975
RIX = 3.056
SMOG = 11.688


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


def test_linsear_write():
    score = ReadabilityScores.calculate_linsear_write(
        WORD_COUNT, COMPLEX_WORD_COUNT,SENTENCE_COUNT)
    assert(LINSEAR_WRITE == score)

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
