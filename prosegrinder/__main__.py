# -*- coding: utf-8 -*-

import click
import json

from prosegrinder.prose import Prose

@click.command()
@click.option('-f', '--file', required=True, type=click.File())
def cli(file):
    click.echo("Grinding {}".format(click.format_filename(file.name)))
    text = file.read()
    # click.echo(text)
    p = Prose(text)
    click.echo(p.readability_scores)
