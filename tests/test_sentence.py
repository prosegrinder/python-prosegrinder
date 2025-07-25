# -*- coding: utf-8 -*-

from prosegrinder import Dictionary, Sentence

DICTIONARY = Dictionary()
TEXT = "This is a sentence of twelve words, and let's add some complexity."
SENTENCE = Sentence(TEXT, DICTIONARY)

WORD_CHARACTER_COUNT = 53
WORD_COUNT = 12
PHONES = [
    "DH",
    "IH1",
    "S",
    "IH1",
    "Z",
    "AH0",
    "S",
    "EH1",
    "N",
    "T",
    "AH0",
    "N",
    "S",
    "AH1",
    "V",
    "T",
    "W",
    "EH1",
    "L",
    "V",
    "W",
    "ER1",
    "D",
    "Z",
    "AH0",
    "N",
    "D",
    "L",
    "EH1",
    "T",
    "S",
    "AE1",
    "D",
    "S",
    "AH1",
    "M",
    "K",
    "AH0",
    "M",
    "P",
    "L",
    "EH1",
    "K",
    "S",
    "AH0",
    "T",
    "IY0",
]
SYLLABLE_COUNT = 16
COMPLEX_WORD_COUNT = 1


def test_sentence():
    assert WORD_COUNT == SENTENCE.word_count
    assert WORD_CHARACTER_COUNT == SENTENCE.word_character_count
    assert len(PHONES) == SENTENCE.phone_count
    assert SYLLABLE_COUNT == SENTENCE.syllable_count
    assert COMPLEX_WORD_COUNT == SENTENCE.complex_word_count
