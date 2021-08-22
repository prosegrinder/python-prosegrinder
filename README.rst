Prosegrinder
===============

.. image:: https://img.shields.io/pypi/v/prosegrinder.svg
    :target: https://pypi.python.org/pypi/prosegrinder
    :alt: Latest PyPI version

.. image:: https://github.com/prosegrinder/python-prosegrinder/workflows/Python%20CI/badge.svg?branch=main
    :target: https://github.com/prosegrinder/python-prosegrinder/actions?query=workflow%3A%22Python+CI%22+branch%3Amain
    :alt: GitHub Workflow Status

.. image:: https://app.codacy.com/project/badge/Grade/fbb22c1d33a34aa3bee095fc3ff62bc9
    :target: https://www.codacy.com/gh/prosegrinder/python-prosegrinder?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=prosegrinder/python-prosegrinder&amp;utm_campaign=Badge_Grade
    :alt: Latest Codacy Coverage Report

A relatively fast, functional prose text counter with readability scoring.

Installation
------------

``prosegrinder`` is available on PyPI. Simply install it with ``pip``::

    $ pip install prosegrinder

Usage
-----

The main use is via the prosegrinder.Prose object.

    >>> from prosegrinder import Prose
    >>> p = Prose("Some lengthy text that's actual prose, like a novel or article.")

The Prose object will parse everything down and compute basic staticstics, including word count,
sentence count, paragraph count, syllable count, point of view, dialogue, narrative, and a set
of readabilit scores. All objects and attributes should be treated as immutable.

I know this isn't great documentation, but it should be enough to get you going.

Command Line Interaface
~~~~~~~~~~~~~~~~~~~~~~~

Prosegrinder now includes a simple CLI for analyzing text in a file:::

    Usage: prosegrinder [OPTIONS] FILES...

      Setup the command line interface

    Options:
      -i, --indent INTEGER  Python pretty-print json indent level.
      -s, --save FILENAME   File to save output to.
      --help                Show this message and exit.

Will provide basic statistics on text from a file or set of files including the filename and sh256 of text in each file analyzed. Output is json to help facilitate use in automation:::

    [
      {
        "filename": "shortstory.txt",
        "statistics": {
          "sha256": "5b756dea7c7f0088ff3692e402466af7f4fc493fa357c1ae959fa4493943fc03",
          "word_character_count": 7008,
          "phone_count": 5747,
          "syllable_count": 2287,
          "word_count": 1528,
          "sentence_count": 90,
          "paragraph_count": 77,
          "complex_word_count": 202,
          "long_word_count": 275,
          "pov_word_count": 113,
          "first_person_word_count": 8,
          "second_person_word_count": 74,
          "third_person_word_count": 31,
          "pov": "first",
          "readability_scores": {
            "automated_readability_index": 0.281,
            "coleman_liau_index": 9.425,
            "flesch_kincaid_grade_level": 8.693,
            "flesch_reading_ease": 62.979,
            "gunning_fog_index": 12.079,
            "linsear_write": 10.733,
            "lix": 34.975,
            "rix": 3.056,
            "smog": 11.688
          }
        }
      },
      {
        "filename": "copyright.txt",
        "statistics": {
          "sha256": "553bfd087a2736e4bbe2f312e3d3a5b763fb57caa54e3626da03b0fd3f42e017",
          "word_character_count": 222,
          "phone_count": 169,
          "syllable_count": 78,
          "word_count": 46,
          "sentence_count": 7,
          "paragraph_count": 16,
          "complex_word_count": 10,
          "long_word_count": 12,
          "pov_word_count": 1,
          "first_person_word_count": 1,
          "second_person_word_count": 0,
          "third_person_word_count": 0,
          "pov": "first",
          "readability_scores": {
            "automated_readability_index": 1.404,
            "coleman_liau_index": 8.073,
            "flesch_kincaid_grade_level": 6.982,
            "flesch_reading_ease": 56.713,
            "gunning_fog_index": 11.324,
            "linsear_write": 3.714,
            "lix": 32.658,
            "rix": 1.714,
            "smog": 9.957
          }
        }
      }
    ]





Readbility scores
~~~~~~~~~~~~~~~~~

The set of scores automatically calculated:

* Automated Readability Index
* Coleman Liau Index
* Flesch Kincaid Grade Level
* Flesch Reading Ease
* Gunning Fog Index
* Linsear Write
* LIX
* RIX
* SMOG
