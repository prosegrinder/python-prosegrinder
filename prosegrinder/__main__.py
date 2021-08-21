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
        "filename": filename,
        "statistics": p.stats
    }
    j = json.dumps(d, indent=indent)
    if (save):
        save.write(j)
    else:
        click.echo(j)
