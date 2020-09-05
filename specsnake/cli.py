import click

from specsnake.plotting import Plotter
from specsnake.tools import load_sfg


@click.group()
def cli():
    pass


@cli.command()
@click.argument('filename')
def plot(filename):
    temp = load_sfg()(filename)
    Plotter([temp]).show()
