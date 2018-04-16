# -*- coding: utf-8 -*-

from bookworm import Dictionary
from bookworm import Sentence

dictionary = Dictionary()
text = "This is a sentence of seven words, and let's add some complexity."

def test_sentence():
    sentence = Sentence(text, dictionary)
    assert(sentence.word_count == 12)
    assert(sentence.character_count == 52)
    assert(sentence.syllable_count == 17)
    assert(sentence.complex_word_count == 1)
