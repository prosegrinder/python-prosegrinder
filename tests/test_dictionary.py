# -*- coding: utf-8 -*-

from prosegrinder import Dictionary
from prosegrinder import Word

dictionary = Dictionary()

def test_syllable_count():
    assert(dictionary.syllable_count("frowning") == 2)
    assert(dictionary.syllable_count("zurkuhlen") == 3)
    assert(dictionary.syllable_count("cafe") == 2)
    assert(dictionary.syllable_count("20,012.12") == 7)
    assert(dictionary.syllable_count("1,904") == 4)
    assert(dictionary.syllable_count("0.2315") == 5)
    assert(dictionary.syllable_count("-503,012.12") == 9)

def test_get_word():
    frowning = Word('frowning', 2, True, False)
    assert(frowning == dictionary.get_word('frowning'))
    cafe = Word('cafe', 2, True, False)
    assert(cafe == dictionary.get_word('cafe'))
    zurkuhlen = Word('zurkuhlen', 3, True, False)
    assert(zurkuhlen == dictionary.get_word('zurkuhlen'))
    num1904 = Word('1,904', 4, False, True)
    assert(num1904 == dictionary.get_word('1,904'))
