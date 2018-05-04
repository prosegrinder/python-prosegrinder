# -*- coding: utf-8 -*-

from bookworm import Dictionary
from bookworm import Sentence

dictionary = Dictionary()
text = "This is a sentence of twelve words, and let's add some complexity."

def test_sentence():
    sentence = Sentence(text, dictionary)
    assert(sentence.word_count == 12)
    assert(sentence.character_count == 53)
    assert(sentence.syllable_count == 16)
    assert(sentence.complex_word_count == 1)
