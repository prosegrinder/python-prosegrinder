# -*- coding: utf-8 -*-

from prosegrinder import Dictionary
from prosegrinder import Sentence

dictionary = Dictionary()
text = "This is a sentence of twelve words, and let's add some complexity."
sentence = Sentence(text, dictionary)

WORD_CHARACTER_COUNT = 53
WORD_COUNT = 12
SYLLABLE_COUNT = 16
COMPLEX_WORD_COUNT = 1

def test_sentence():
    assert(WORD_COUNT == sentence.word_count)
    assert(WORD_CHARACTER_COUNT == sentence.word_character_count)
    assert(SYLLABLE_COUNT == sentence.syllable_count)
    assert(COMPLEX_WORD_COUNT == sentence.complex_word_count)
