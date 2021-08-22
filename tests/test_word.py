# -*- coding: utf-8 -*-

from prosegrinder import Word


def test_equality():
    w1 = Word(
        "frowning",
        ["F", "R", "AW1", "N", "IH0", "NG"],
        ["F", "R", "AW", "N", "IH", "NG"],
        2,
        True,
        False,
    )
    w2 = Word(
        "frowning",
        ["F", "R", "AW1", "N", "IH0", "NG"],
        ["F", "R", "AW", "N", "IH", "NG"],
        2,
        True,
        False,
    )
    w3 = Word("cafe", ["K", "AH0", "F", "EY1"], ["K", "AH", "F", "EY"], 2, True, False)
    assert w1 == w2
    assert w1 != w3
    assert w2 != w3
