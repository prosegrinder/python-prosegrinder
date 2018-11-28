# -*- coding: utf-8 -*-

from bookworm import Dictionary
from bookworm import Paragraph

dictionary = Dictionary()
text = """For easy readability, limit your choice of font to either Courier or Times New Roman. Courier (my strong preference) is a monospaced font, which means that every character is exactly as wide as every other. It's easier for an editor to detect spelling errors in a monospaced font than in a proportional font like Times New Roman (in which the "i" uses less horizontal space than the "m" does). With a monospaced font, there will also be fewer characters on each line, which can make your manuscript easier to scan. Still, many writers have come to prefer Times New Roman, and either is usually acceptable. (If in doubt, consult your intended market's submission guidelines.) Set your font size to 12 points."""


def test_paragraph():
    paragraph = Paragraph(text, dictionary)
    assert(paragraph.sentence_count == 7)
    assert(paragraph.word_count == 121)
    assert(paragraph.character_count == 563)
    assert(paragraph.syllable_count == 192)
    assert(paragraph.complex_word_count == 22)
