# -*- coding: utf-8 -*-

from bookworm import Dictionary
from bookworm import Word

def test_heuristic_syllable_count():
    dictionary = Dictionary()
    assert(dictionary._heuristic_syllable_count("frowning") == 2)   # nosec
    assert(dictionary._heuristic_syllable_count("zurkuhlen") == 3)  # nosec
    assert(dictionary._heuristic_syllable_count("cafe") == 2)       # nosec
    assert(dictionary._heuristic_syllable_count("20,012.12") == 7)  # nosec
    assert(dictionary._heuristic_syllable_count("1,904") == 4)      # nosec
    assert(dictionary._heuristic_syllable_count("0.2315") == 5)     # nosec
    assert(dictionary._heuristic_syllable_count("-503,012.12") == 9)# nosec

def test_syllable_count():
    dictionary = Dictionary()
    assert(dictionary._syllable_count("frowning") == 2)   # nosec
    assert(dictionary._syllable_count("zurkuhlen") == 3)  # nosec
    assert(dictionary._syllable_count("cafe") == 2)       # nosec
    assert(dictionary._syllable_count("20,012.12") == 7)  # nosec
    assert(dictionary._syllable_count("1,904") == 4)      # nosec
    assert(dictionary._syllable_count("0.2315") == 5)     # nosec
    assert(dictionary._syllable_count("-503,012.12") == 9)# nosec

def test_get_word():
    dictionary = Dictionary()
    frowning = Word('frowning', 2, True, False)
    assert(frowning == dictionary.get_word('frowning'))
    cafe = Word('cafe', 2, True, False)
    assert(cafe == dictionary.get_word('cafe'))
    zurkuhlen = Word('zurkuhlen', 3, True, False)
    assert(zurkuhlen == dictionary.get_word('zurkuhlen'))
    num1904 = Word('1,904', 4, False, True)
    assert(num1904 == dictionary.get_word('1,904'))
