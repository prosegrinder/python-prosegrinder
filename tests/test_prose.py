# -*- coding: utf-8 -*-

import os
from collections import Counter

from prosegrinder import Dictionary, Prose

dictionary = Dictionary()
SHORTSTORY = os.path.join(os.path.dirname(
    __file__), 'resources', 'shortstory.txt')
text = open(SHORTSTORY).read()
prose = Prose(text)

WORD_CHARACTER_COUNT = 7008
SYLLABLE_COUNT = 2287
COMPLEX_WORD_COUNT = 202
LONG_WORD_COUNT = 275
SENTENCE_COUNT = 90
WORD_COUNT = 1528
UNIQUE_WORD_COUNT = 526
POV_WORD_COUNT = 113  # was 104
FIRST_PERSON_INDICATOR_COUNT = 8  # was 6
SECOND_PERSON_INDICATOR_COUNT = 74  # was 73
THIRD_PERSON_INDICATOR_COUNT = 31  # was 25
PARAGRAPH_COUNT = 77

AUTOMATED_READABILITY_INDEX = 0.281
COLEMAN_LIAU_INDEX = 9.425
FLESCH_KINCAID_GRADE_LEVEL = 8.693
FLESCH_READING_EASE = 62.979
GUNNING_FOG_INDEX = 12.079
LIX = 34.975
RIX = 3.056
SMOG = 11.688


def test_characters():
    assert(WORD_CHARACTER_COUNT == prose.word_character_count)


def test_syllables():
    assert(SYLLABLE_COUNT == prose.syllable_count)


def test_words():
    assert(WORD_COUNT == prose.word_count)
    assert(COMPLEX_WORD_COUNT == prose.complex_word_count)
    assert(LONG_WORD_COUNT == prose.long_word_count)
    assert(UNIQUE_WORD_COUNT == prose.unique_word_count)


def test_pov():
    assert(POV_WORD_COUNT == prose.pov_word_count)
    assert(FIRST_PERSON_INDICATOR_COUNT == prose.first_person_word_count)
    assert(SECOND_PERSON_INDICATOR_COUNT == prose.second_person_word_count)
    assert(THIRD_PERSON_INDICATOR_COUNT == prose.third_person_word_count)


def test_sentences():
    assert(SENTENCE_COUNT == prose.sentence_count)


def test_paragraphs():
    assert(PARAGRAPH_COUNT == prose.paragrah_count)


def test_dialogue_narrative():
    assert(WORD_CHARACTER_COUNT == prose.dialogue.word_character_count +
           prose.narrative.word_character_count)
    assert(SYLLABLE_COUNT == prose.dialogue.syllable_count +
           prose.narrative.syllable_count)
    assert(WORD_COUNT == prose.dialogue.word_count +
           prose.narrative.word_count)
    assert(LONG_WORD_COUNT == prose.dialogue.long_word_count +
           prose.narrative.long_word_count)
    assert(COMPLEX_WORD_COUNT == prose.dialogue.complex_word_count +
           prose.narrative.complex_word_count)
    combined_word_frequency = Counter()
    combined_word_frequency.update(prose.dialogue.word_frequency)
    combined_word_frequency.update(prose.narrative.word_frequency)
    assert(UNIQUE_WORD_COUNT == len(combined_word_frequency))
    assert(POV_WORD_COUNT == prose.dialogue.pov_word_count +
           prose.narrative.pov_word_count)
    assert(FIRST_PERSON_INDICATOR_COUNT == prose.dialogue.first_person_word_count +
           prose.narrative.first_person_word_count)
    assert(SECOND_PERSON_INDICATOR_COUNT == prose.dialogue.second_person_word_count +
           prose.narrative.second_person_word_count)
    assert(THIRD_PERSON_INDICATOR_COUNT == prose.dialogue.third_person_word_count +
           prose.narrative.third_person_word_count)


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
