# -*- coding: utf-8 -*-

import click
import json

from prosegrinder.prose import Prose

@click.command()
@click.argument('file', required=True, type=click.File('r'))
@click.option('-i', '--indent', required=False,
    type=int, default=2, help="Python pretty-print json indent level.")
@click.option('-s', '--save', required=False,
    type=click.File('w'), help="File to save output to.")
def cli(file, save, indent):
    filename = click.format_filename(file.name)
    text = file.read()
    p = Prose(text)
    d = {
        "filename":
            filename,
        "sha256":
            p.sha256,
        "word_character_count":
            p.word_character_count,
        "phone_count":
            p.phone_count,
        "syllable_count":
            p.syllable_count,
        "word_count":
            p.word_count,
        "sentence_count":
            p.sentence_count,
        "paragraph_count":
            p.paragraph_count,
        "complex_word_count":
            p.complex_word_count,
        "long_word_count":
            p.long_word_count,
        "pov_word_count":
            p.pov_word_count,
        "first_person_word_count":
            p.first_person_word_count,
        "second_person_word_count":
            p.second_person_word_count,
        "third_person_word_count":
            p.third_person_word_count,
        "pov":
            p.pov,
        "readability_scores": {
            "automated_readability_index":
                p.readability_scores.automated_readability_index,
            "coleman_liau_index":
                p.readability_scores.coleman_liau_index,
            "flesch_kincaid_grade_level":
                p.readability_scores.flesch_kincaid_grade_level,
            "flesch_reading_ease":
                p.readability_scores.flesch_reading_ease,
            "gunning_fog_index":
                p.readability_scores.gunning_fog_index,
            "linsear_write":
                p.readability_scores.linsear_write,
            "lix":
                p.readability_scores.lix,
            "rix":
                p.readability_scores.rix,
            "smog":
                p.readability_scores.smog
        }
    }
    if (save):
        save.write(json.dumps(d, indent=indent))
    else:
        click.echo(json.dumps(d, indent=indent))
