Prosegrinder
===============

.. image:: https://img.shields.io/pypi/v/prosegrinder.svg
  :target: https://pypi.python.org/pypi/prosegrinder
  :alt: Latest PyPI version

.. image:: https://travis-ci.org/prosegrinder/python-prosegrinder.svg?branch=master
  :target: https://travis-ci.org/prosegrinder/python-prosegrinder
  :alt: Latest Travis CI build status

.. image:: https://api.codacy.com/project/badge/Grade/d005ccb2840340718fcf3ab3a383a225
  :target: https://www.codacy.com/app/ProseGrinder/python-prosegrinder?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=prosegrinder/python-prosegrinder&amp;utm_campaign=Badge_Grade
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
