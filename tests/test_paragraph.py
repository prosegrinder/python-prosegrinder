# -*- coding: utf-8 -*-

from collections import Counter

from prosegrinder import Dictionary, Paragraph

dictionary = Dictionary()
text = """For easy readability, limit your choice of font to either Courier or Times New Roman. Courier (my strong preference) is a monospaced font, which means that every character is exactly as wide as every other. It's easier for an editor to detect spelling errors in a monospaced font than in a proportional font like Times New Roman (in which the "i" uses less horizontal space than the "m" does). With a monospaced font, there will also be fewer characters on each line, which can make your manuscript easier to scan. Still, many writers have come to prefer Times New Roman, and either is usually acceptable. (If in doubt, consult your intended market's submission guidelines.) Set your font size to 12 points."""
paragraph = Paragraph(text, dictionary)

WORD_CHARACTER_COUNT = 563
SYLLABLE_COUNT = 195
WORD_COUNT = 121
COMPLEX_WORD_COUNT = 22
LONG_WORD_COUNT = 22
UNIQUE_WORD_COUNT = 83
POV_WORD_COUNT = 6
FIRST_PERSON_INDICATOR_COUNT = 1
SECOND_PERSON_INDICATOR_COUNT = 4
THIRD_PERSON_INDICATOR_COUNT = 1
SENTENCE_COUNT = 7


def test_characters():
    assert(WORD_CHARACTER_COUNT == paragraph.word_character_count)


def test_syllables():
    assert(SYLLABLE_COUNT == paragraph.syllable_count)


def test_words():
    assert(WORD_COUNT == paragraph.word_count)
    assert(COMPLEX_WORD_COUNT == paragraph.complex_word_count)
    assert(LONG_WORD_COUNT == paragraph.long_word_count)
    assert(UNIQUE_WORD_COUNT == paragraph.unique_word_count)


def test_pov():
    assert(POV_WORD_COUNT == paragraph.pov_word_count)
    assert(FIRST_PERSON_INDICATOR_COUNT == paragraph.first_person_word_count)
    assert(SECOND_PERSON_INDICATOR_COUNT == paragraph.second_person_word_count)
    assert(THIRD_PERSON_INDICATOR_COUNT == paragraph.third_person_word_count)


def test_sentences():
    assert(SENTENCE_COUNT == paragraph.sentence_count)


def test_dialogue_narrative():
    assert(WORD_CHARACTER_COUNT == paragraph.dialogue.word_character_count +
           paragraph.narrative.word_character_count)
    assert(SYLLABLE_COUNT == paragraph.dialogue.syllable_count +
           paragraph.narrative.syllable_count)
    assert(WORD_COUNT == paragraph.dialogue.word_count +
           paragraph.narrative.word_count)
    assert(LONG_WORD_COUNT == paragraph.dialogue.long_word_count +
           paragraph.narrative.long_word_count)
    assert(COMPLEX_WORD_COUNT == paragraph.dialogue.complex_word_count +
           paragraph.narrative.complex_word_count)
    combined_word_frequency = Counter()
    combined_word_frequency.update(paragraph.dialogue.word_frequency)
    combined_word_frequency.update(paragraph.narrative.word_frequency)
    assert(UNIQUE_WORD_COUNT == len(combined_word_frequency))
    assert(POV_WORD_COUNT == paragraph.dialogue.pov_word_count +
           paragraph.narrative.pov_word_count)
    assert(FIRST_PERSON_INDICATOR_COUNT == paragraph.dialogue.first_person_word_count +
           paragraph.narrative.first_person_word_count)
    assert(SECOND_PERSON_INDICATOR_COUNT == paragraph.dialogue.second_person_word_count +
           paragraph.narrative.second_person_word_count)
    assert(THIRD_PERSON_INDICATOR_COUNT == paragraph.dialogue.third_person_word_count +
           paragraph.narrative.third_person_word_count)
