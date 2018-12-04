# -*- coding: utf-8 -*-

from prosegrinder import Word

def test_equality():
    w1 = Word('frowning', 2, True, False)
    w2 = Word('frowning', 2, True, False)
    w3 = Word('cafe', 2, True, False)
    assert(w1 == w2)
    assert(w1 != w3)
    assert(w2 != w3)
