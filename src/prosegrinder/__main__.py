"""Command line interface for prosegrinder."""

import json

import click

from prosegrinder.prose import Prose


@click.command()
@click.argument("files", nargs=-1, required=True, type=click.File("r"))
@click.option(
    "-i",
    "--indent",
    required=False,
    type=int,
    default=2,
    help="Python pretty-print json indent level.",
)
@click.option(
    "-s", "--save", required=False, type=click.File("w"), help="File to save output to."
)
def cli(files, save, indent):
    """Setup the command line interface"""
    processed_files = []
    for file in files:
        filename = click.format_filename(file.name)
        text = file.read()
        _p = Prose(text)
        _d = {"filename": filename, "statistics": _p.stats}
        processed_files.append(_d)
    _j = json.dumps(processed_files, indent=indent)
    if save:
        save.write(_j)
    else:
        click.echo(_j)
